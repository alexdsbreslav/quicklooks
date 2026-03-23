"""Validate a quicklooks code cell against the canonical skill templates.

Call ``ql.validate_cell(cell_source)`` after generating a quicklooks cell
to catch template deviations before the user sees them.
"""

from __future__ import annotations

import ast
import re
from typing import List


REFERENCE_COMMENT = (
    "# https://github.com/alexdsbreslav/quicklooks/blob/main/"
    "quicklooks/skill/reference.md"
)

# Ordered parameter names for each function (excluding the positional `chart`).
# These must match the canonical templates in SKILL.md exactly.
EXPECTED_PARAMS: dict[str, list[str]] = {
    "chart": [
        "title", "xlabel", "ylabel",
        "x_min_max", "y_min_max",
        "xtick_interval", "ytick_interval",
        "size", "colors", "font",
        "xtick_labels", "ytick_labels",
        "horizontal_gridlines", "vertical_gridlines",
    ],
    "line": [
        "x", "y", "color", "yerror",
        "linewidth", "linestyle", "marker",
        "opacity", "label", "end_label", "layer_order",
    ],
    "bar": [
        "xlabels", "y", "color", "yerror",
        "bars_per_group", "bar_index",
        "opacity", "label", "layer_order",
    ],
    "scatter": [
        "x", "y", "color", "x_error", "y_error",
        "marker", "opacity", "label", "layer_order",
    ],
    "dist": [
        "data", "color", "dist_type", "auto_fit",
        "distribution_min_max", "bin_interval",
        "opacity", "label", "layer_order",
    ],
    "refline": [
        "direction", "location", "color",
        "linewidth", "linestyle", "marker",
        "opacity", "label", "end_label", "layer_order",
    ],
    "legend": ["location", "frame"],
    "text": [
        "text", "x", "y", "size", "color",
        "horizontal_align", "vertical_align",
        "rotation", "box", "layer_order",
    ],
    "save": ["name", "folder", "format"],
}

ALL_QL_FUNCS = set(EXPECTED_PARAMS.keys())
DATA_ELEMENT_FUNCS = {"line", "bar", "scatter", "dist"}

# Build the valid-color-name lookup from _colors.py so it stays in sync
# automatically when new palettes or colors are added.
_UTILITY_COLORS = {"default"}  # "default" is always valid (uses library default)

def _build_library_colors() -> dict[str, set[str]]:
    try:
        from . import _colors as _c
        result = {}
        for lib_name, lib_obj in _c.COLOR_LIBRARIES.items():
            result[lib_name] = set(lib_obj.list_colors()) | _UTILITY_COLORS
        return result
    except Exception:
        return {}

LIBRARY_COLORS: dict[str, set[str]] = _build_library_colors()


def validate_cell(source: str) -> List[str]:
    """Check *source* (a single notebook cell's code) for skill violations.

    Returns a list of human-readable violation strings. An empty list means
    the cell passes all checks.
    """
    violations: List[str] = []
    lines = source.strip().splitlines()

    if not lines:
        return ["Cell is empty."]

    # --- Rule 1: reference link comment on the first line ---
    first_line = lines[0].strip()
    if not first_line.startswith("# http") or "reference.md" not in first_line:
        violations.append(
            "First line must be the reference link comment: "
            f"{REFERENCE_COMMENT}"
        )

    # --- Parse ql.* calls ---
    calls = _extract_ql_calls(source)

    if not calls:
        violations.append("No ql.* calls found in cell.")
        return violations

    # --- Rule 2: ql.chart() must come first ---
    func_names = [c["func"] for c in calls]
    if func_names[0] != "chart":
        violations.append(
            "ql.chart() must be the first ql.* call in the cell, "
            f"but found ql.{func_names[0]}() first."
        )

    # --- Determine active color library from ql.chart() ---
    active_library: str | None = None
    chart_call = next((c for c in calls if c["func"] == "chart"), None)
    if chart_call:
        raw = chart_call["kwvalues"].get("colors", "")
        lib_name = raw.strip('"\'')
        if lib_name in LIBRARY_COLORS:
            active_library = lib_name

    # --- Per-call checks ---
    has_end_label_false = False
    has_legend = False

    for call in calls:
        func = call["func"]
        kw_names = call["kwargs"]

        if func not in ALL_QL_FUNCS:
            violations.append(f"Unknown function: ql.{func}()")
            continue

        expected = EXPECTED_PARAMS[func]

        # Check for unexpected keyword arguments
        unexpected = [k for k in kw_names if k not in expected]
        if unexpected:
            violations.append(
                f"ql.{func}() has unexpected parameter(s): "
                f"{', '.join(unexpected)}. "
                f"Expected: {', '.join(expected)}"
            )

        # Check for missing keyword arguments (all params should be explicit)
        missing = [k for k in expected if k not in kw_names]
        if missing:
            violations.append(
                f"ql.{func}() is missing parameter(s): "
                f"{', '.join(missing)}. "
                "All parameters must be included explicitly."
            )

        # Check that color= value is valid for the active library.
        # Only validate when the value is a string literal (starts with a quote);
        # variable references like region_colors[i] can't be checked statically.
        if active_library and "color" in call["kwvalues"]:
            raw = call["kwvalues"]["color"].strip()
            if raw and raw[0] in ('"', "'"):
                color_name = raw.strip('"\'')
                valid = LIBRARY_COLORS[active_library]
                if color_name not in valid:
                    violations.append(
                        f"ql.{func}() color=\"{color_name}\" is not a valid color "
                        f"in the \"{active_library}\" library. "
                        f"Available: {', '.join(sorted(valid - _UTILITY_COLORS))}, "
                        f"plus utility colors: {', '.join(sorted(_UTILITY_COLORS))}."
                    )

        # Check parameter order matches the template
        filtered = [k for k in kw_names if k in expected]
        expected_order = [k for k in expected if k in filtered]
        if filtered != expected_order:
            violations.append(
                f"ql.{func}() parameters are in the wrong order. "
                f"Expected: {', '.join(expected_order)}. "
                f"Got: {', '.join(filtered)}"
            )

        # Track end_label/legend state for line calls
        if func == "line" and "end_label" in kw_names:
            val = call["kwvalues"].get("end_label")
            if val == "False":
                has_end_label_false = True

        if func == "legend":
            has_legend = True

    # --- Rule: if any line has end_label=False, legend should be present ---
    if has_end_label_false and not has_legend:
        violations.append(
            "At least one ql.line() has end_label=False but no ql.legend() "
            "call was found. Add a legend when end labels are disabled."
        )

    # --- Formatting checks (line-by-line) ---
    violations.extend(_check_formatting(source))

    return violations


def _extract_ql_calls(source: str) -> List[dict]:
    """Parse ql.func(...) calls from source, returning func name and kwargs."""
    calls = []
    pattern = re.compile(
        r'ql\.(\w+)\s*\(',
    )

    for match in pattern.finditer(source):
        func_name = match.group(1)
        start = match.end()

        paren_depth = 1
        pos = start
        while pos < len(source) and paren_depth > 0:
            if source[pos] == '(':
                paren_depth += 1
            elif source[pos] == ')':
                paren_depth -= 1
            pos += 1

        args_str = source[start:pos - 1]

        kw_names = []
        kw_values = {}
        for kw_match in re.finditer(r'(\w+)\s*=\s*([^,\n]+)', args_str):
            name = kw_match.group(1)
            value = kw_match.group(2).strip().rstrip(',')
            kw_names.append(name)
            kw_values[name] = value

        calls.append({
            "func": func_name,
            "kwargs": kw_names,
            "kwvalues": kw_values,
        })

    return calls


def _check_formatting(source: str) -> List[str]:
    """Check formatting rules: semicolons, no external imports."""
    violations = []
    lines = source.strip().splitlines()

    # Check for external imports
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("import ") or stripped.startswith("from "):
            if "quicklooks" not in stripped and "ql" not in stripped:
                violations.append(
                    f"No external imports allowed in quicklooks cells: "
                    f"'{stripped}'"
                )

    # Check that each ql.* call ends with a semicolon.
    # Look for lines containing closing ");" or just ")" without ";"
    call_end_pattern = re.compile(r'^\s*\)\s*;?\s*$')
    for line in lines:
        if call_end_pattern.match(line):
            if ';' not in line:
                violations.append(
                    "Every ql.* call must end with a semicolon. "
                    f"Found closing ')' without ';': '{line.strip()}'"
                )

    return violations

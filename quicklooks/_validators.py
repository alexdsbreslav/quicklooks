"""Reusable input validators with clear, structured error messages.

Every error message starts with the function name and parameter so that
both humans and AI agents can immediately identify what to fix.
"""

from __future__ import annotations

from typing import Any, Sequence

import numpy as np


def validate_option(
    value: Any,
    valid_options: Sequence,
    param_name: str,
    func_name: str,
) -> None:
    """Raise ``ValueError`` if *value* is not in *valid_options*."""
    if value not in valid_options:
        options_str = ", ".join(
            repr(v) for v in valid_options
        )
        raise ValueError(
            f'ql.{func_name}() error: invalid value for \'{param_name}\': {value!r}\n\n'
            f"Valid options for {param_name}: {options_str}"
        )


def validate_type(
    value: Any,
    expected_types: tuple,
    param_name: str,
    func_name: str,
) -> None:
    """Raise ``TypeError`` if *value* is not an instance of *expected_types*."""
    if not isinstance(value, expected_types):
        type_names = " or ".join(t.__name__ for t in expected_types)
        raise TypeError(
            f"ql.{func_name}() error: '{param_name}' must be {type_names}, "
            f"but received {type(value).__name__}.\n\n"
            f"Value: {value!r}"
        )


def validate_bool(
    value: Any,
    param_name: str,
    func_name: str,
) -> None:
    """Raise ``TypeError`` if *value* is not a bool."""
    if not isinstance(value, bool):
        raise TypeError(
            f"ql.{func_name}() error: '{param_name}' must be True or False, "
            f"but received {type(value).__name__}: {value!r}"
        )


def validate_1d_array(
    value: Any,
    param_name: str,
    func_name: str,
) -> None:
    """Raise if *value* is not a 1-D array-like."""
    if isinstance(value, (str, int, float, bool)):
        raise TypeError(
            f"ql.{func_name}() error: '{param_name}' must be a 1D array, "
            f"but received a single {type(value).__name__} value ({value!r}).\n\n"
            f"Pass an array-like (list, numpy array, or pandas Series) instead."
        )
    shape = np.shape(value)
    if len(shape) == 0:
        raise TypeError(
            f"ql.{func_name}() error: '{param_name}' must be a 1D array, "
            f"but received a scalar.\n\n"
            f"Pass an array-like (list, numpy array, or pandas Series) instead."
        )
    if len(shape) != 1:
        raise ValueError(
            f"ql.{func_name}() error: '{param_name}' must be a 1D array, "
            f"but received a {len(shape)}D array with shape {shape}.\n\n"
            f"Ensure your data is 1-dimensional."
        )


def validate_matching_shapes(
    a: Any,
    b: Any,
    name_a: str,
    name_b: str,
    func_name: str,
) -> None:
    """Raise ``ValueError`` if *a* and *b* have different shapes."""
    shape_a = np.shape(a)
    shape_b = np.shape(b)
    if shape_a != shape_b:
        raise ValueError(
            f"ql.{func_name}() error: '{name_a}' and '{name_b}' have different "
            f"shapes — {name_a} has {shape_a[0]} values, "
            f"{name_b} has {shape_b[0]} values.\n\n"
            f"Both arrays must have the same length. Check that your data is "
            f"aligned and that no extra rows were included."
        )


def validate_chart(chart: Any, func_name: str) -> None:
    """Raise if *chart* is not a valid Chart object with an active axes."""
    if not hasattr(chart, "ax") or chart.ax is None:
        raise ValueError(
            f"ql.{func_name}() error: the first argument must be a Chart "
            f"object created by ql.chart().\n\n"
            f"Create a chart first:\n"
            f"  cs = ql.chart(title=\"My Chart\", ...)"
        )


def validate_optional_1d_array(
    value: Any,
    param_name: str,
    func_name: str,
) -> None:
    """Raise if *value* is not None and not a valid 1-D array-like."""
    if value is None:
        return
    if isinstance(value, (str, int, float, bool)):
        raise TypeError(
            f"ql.{func_name}() error: '{param_name}' must be a 1D array or None, "
            f"but received a single {type(value).__name__} value ({value!r}).\n\n"
            f"If you don't need {param_name}, set it to None. Otherwise, "
            f"pass an array-like (list, numpy array, or pandas Series)."
        )
    shape = np.shape(value)
    if len(shape) != 1:
        raise ValueError(
            f"ql.{func_name}() error: '{param_name}' must be a 1D array or None, "
            f"but received a {len(shape)}D array with shape {shape}.\n\n"
            f"Ensure your data is 1-dimensional."
        )


def validate_tuple_pair(
    value: Any,
    param_name: str,
    func_name: str,
) -> None:
    """Raise if *value* is not a 2-element tuple with second > first (numeric)."""
    if not isinstance(value, tuple) or len(value) != 2:
        raise TypeError(
            f"ql.{func_name}() error: '{param_name}' must be a tuple of two "
            f"values, e.g. (0, 100).\n\n"
            f"Received: {value!r}"
        )

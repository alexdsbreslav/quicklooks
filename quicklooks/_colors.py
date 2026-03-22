"""Color libraries and color resolution for quicklooks.

Each color is a 3-tuple of hex strings: (fill/light, line/mid, edge/dark).
The ``resolve_color`` function converts a user-facing color name (e.g. "blue")
into the concrete 3-tuple from the active color library.
"""

from __future__ import annotations

from typing import Dict, List, Sequence, Tuple, Union


ColorTuple = Tuple[str, str, str]


class ColorLibrary:
    """A named collection of color palettes.

    Args:
        name: Human-readable library name.
        background: Background hex color.
        text: Default text hex color.
        default_color_name: Key in *colors* used when color="default".
        colors: Mapping of color name -> (fill, line, edge) tuples.
        iterable_keys: Ordered subset of *colors* keys for iteration.
    """

    def __init__(
        self,
        name: str,
        background: str,
        text: str,
        default_color_name: str,
        colors: Dict[str, ColorTuple],
        iterable_keys: Sequence[str],
    ) -> None:
        self.name = name
        self.background = background
        self.text = text
        self._default_color_name = default_color_name
        self._colors = colors
        self._iterable_keys = list(iterable_keys)

    @property
    def default(self) -> ColorTuple:
        return self._colors[self._default_color_name]

    @property
    def iterable(self) -> Dict[str, ColorTuple]:
        return {k: self._colors[k] for k in self._iterable_keys}

    def get(self, name: str) -> ColorTuple:
        """Return the color tuple for *name*, or raise ``KeyError``."""
        if name == "default":
            return self.default
        if name in self._colors:
            return self._colors[name]
        raise KeyError(name)

    def list_colors(self) -> List[str]:
        """Return all available color names."""
        return list(self._colors.keys())


# ---------------------------------------------------------------------------
# Shared utility colors (gray / black / white)
# ---------------------------------------------------------------------------

_GRAY_COLORS: Dict[str, ColorTuple] = {
    "light_gray": ("#f1f3f5", "#e9ecef", "#dee2e6"),
    "gray": ("#ced4da", "#adb5bd", "#868e96"),
    "dark_gray": ("#495057", "#343a40", "#212529"),
    "black": ("#000000", "#000000", "#000000"),
    "white": ("#ffffff", "#ffffff", "#ffffff"),
}


# ---------------------------------------------------------------------------
# Extended  (based on Open Color — https://yeun.github.io/open-color/)
# ---------------------------------------------------------------------------

_EXTENDED_COLORS: Dict[str, ColorTuple] = {
    "light_red": ("#ffe3e3", "#ffc9c9", "#ffa8a8"),
    "red": ("#ff8787", "#ff6b6b", "#fa5252"),
    "dark_red": ("#f03e3e", "#e03131", "#c92a2a"),
    "light_pink": ("#ffdeeb", "#fcc2d7", "#faa2c1"),
    "pink": ("#f783ac", "#f06595", "#e64980"),
    "dark_pink": ("#d6336c", "#c2255c", "#a61e4d"),
    "light_grape": ("#f3d9fa", "#eebefa", "#e599f7"),
    "grape": ("#da77f2", "#cc5de8", "#be4bdb"),
    "dark_grape": ("#ae3ec9", "#9c36b5", "#862e9c"),
    "light_violet": ("#e5dbff", "#d0bfff", "#b197fc"),
    "violet": ("#9775fa", "#845ef7", "#7950f2"),
    "dark_violet": ("#7048e8", "#6741d9", "#5f3dc4"),
    "light_indigo": ("#dbe4ff", "#bac8ff", "#91a7ff"),
    "indigo": ("#748ffc", "#5c7cfa", "#4c6ef5"),
    "dark_indigo": ("#4263eb", "#3b5bdb", "#364fc7"),
    "light_blue": ("#d0ebff", "#a5d8ff", "#74c0fc"),
    "blue": ("#4dabf7", "#339af0", "#228be6"),
    "dark_blue": ("#1c7ed6", "#1971c2", "#1864ab"),
    "light_cyan": ("#c5f6fa", "#99e9f2", "#66d9e8"),
    "cyan": ("#3bc9db", "#22b8cf", "#15aabf"),
    "dark_cyan": ("#1098ad", "#0c8599", "#0b7285"),
    "light_teal": ("#c3fae8", "#96f2d7", "#63e6be"),
    "teal": ("#38d9a9", "#20c997", "#12b886"),
    "dark_teal": ("#0ca678", "#099268", "#087f5b"),
    "light_green": ("#d3f9d8", "#b2f2bb", "#8ce99a"),
    "green": ("#69db7c", "#51cf66", "#40c057"),
    "dark_green": ("#37b24d", "#2f9e44", "#2b8a3e"),
    "light_lime": ("#e9fac8", "#d8f5a2", "#c0eb75"),
    "lime": ("#a9e34b", "#94d82d", "#82c91e"),
    "dark_lime": ("#74b816", "#66a80f", "#5c940d"),
    "light_yellow": ("#fff3bf", "#ffec99", "#ffe066"),
    "yellow": ("#ffd43b", "#fcc419", "#fab005"),
    "dark_yellow": ("#f59f00", "#f08c00", "#e67700"),
    "light_orange": ("#ffe8cc", "#ffd8a8", "#ffc078"),
    "orange": ("#ffa94d", "#ff922b", "#fd7e14"),
    "dark_orange": ("#f76707", "#e8590c", "#d9480f"),
    **_GRAY_COLORS,
}

EXTENDED = ColorLibrary(
    name="extended",
    background="#ffffff",
    text="#000000",
    default_color_name="blue",
    colors=_EXTENDED_COLORS,
    iterable_keys=[
        "light_red", "red", "dark_red",
        "light_pink", "pink", "dark_pink",
        "light_grape", "grape", "dark_grape",
        "light_violet", "violet", "dark_violet",
        "light_indigo", "indigo", "dark_indigo",
        "light_blue", "blue", "dark_blue",
        "light_cyan", "cyan", "dark_cyan",
        "light_teal", "teal", "dark_teal",
        "light_green", "green", "dark_green",
        "light_lime", "lime", "dark_lime",
        "light_yellow", "yellow", "dark_yellow",
        "light_orange", "orange", "dark_orange",
    ],
)


# ---------------------------------------------------------------------------
# Neon
# ---------------------------------------------------------------------------

_NEON_COLORS: Dict[str, ColorTuple] = {
    "blue": ("#93C5FD", "#3B82F6", "#1D4ED8"),
    "slate": ("#94A3B8", "#475569", "#1E293B"),
    "teal": ("#67E8F9", "#06B6D4", "#0E7490"),
    "indigo": ("#818CF8", "#4F46E5", "#3730A3"),
    "green": ("#86EFAC", "#22C55E", "#15803D"),
    "purple": ("#C4B5FD", "#8B5CF6", "#6D28D9"),
    "orange": ("#FDBA74", "#F97316", "#C2410C"),
    "pink": ("#F9A8D4", "#EC4899", "#BE185D"),
    **_GRAY_COLORS,
}

NEON = ColorLibrary(
    name="neon",
    background="#ffffff",
    text="#000000",
    default_color_name="blue",
    colors=_NEON_COLORS,
    iterable_keys=[
        "blue", "slate", "teal", "indigo",
        "green", "purple", "orange", "pink",
    ],
)


# ---------------------------------------------------------------------------
# Gouache  (inspired by Amber Vittoria)
# ---------------------------------------------------------------------------

_GOUACHE_COLORS: Dict[str, ColorTuple] = {
    "red": ("#F9B4AB", "#E63946", "#B91C1C"),
    "green": ("#A7F3D0", "#10B981", "#047857"),
    "yellow": ("#FEF08A", "#FACC15", "#A16207"),
    "blue": ("#BAE6FD", "#0EA5E9", "#0369A1"),
    "pink": ("#FBCFE8", "#EC4899", "#9D174D"),
    "orange": ("#FED7AA", "#F97316", "#9A3412"),
    "lavender": ("#DDD6FE", "#A78BFA", "#6D28D9"),
    "teal": ("#99F6E4", "#14B8A6", "#0F766E"),
    **_GRAY_COLORS,
}

GOUACHE = ColorLibrary(
    name="gouache",
    background="#ffffff",
    text="#000000",
    default_color_name="red",
    colors=_GOUACHE_COLORS,
    iterable_keys=[
        "red", "green", "yellow", "blue",
        "pink", "orange", "lavender", "teal",
    ],
)


# ---------------------------------------------------------------------------
# Bloom
# ---------------------------------------------------------------------------

_BLOOM_COLORS: Dict[str, ColorTuple] = {
    "purple": ("#B887FD", "#A261FC", "#8835FD"),
    "periwinkle": ("#EFEBFE", "#C6BAFD", "#B29EFA"),
    "blue": ("#888AFC", "#5659FB", "#383BFA"),
    "cornflower": ("#C6D9FB", "#6B9DF4", "#2E75EF"),
    "yellow": ("#FED35D", "#FEC62E", "#FEBD0B"),
    "green": ("#27CE6F", "#20A85B", "#1A894A"),
    "coral": ("#FEB5AF", "#FD857B", "#FD6B5D"),
    "red": ("#F17255", "#EE4F2A", "#E23912"),
    **_GRAY_COLORS,
}

BLOOM = ColorLibrary(
    name="bloom",
    background="#ffffff",
    text="#000000",
    default_color_name="blue",
    colors=_BLOOM_COLORS,
    iterable_keys=[
        "purple", "periwinkle", "blue", "cornflower",
        "yellow", "green", "coral", "red",
    ],
)


# ---------------------------------------------------------------------------
# Hockney  (inspired by David Hockney)
# ---------------------------------------------------------------------------

_HOCKNEY_COLORS: Dict[str, ColorTuple] = {
    "cobalt": ("#89CFF0", "#2E86DE", "#1B4F72"),
    "turquoise": ("#A3E4D7", "#1ABC9C", "#0E6655"),
    "pink": ("#F8B4D9", "#E84393", "#9B2C6B"),
    "navy": ("#A3B8D0", "#2C3E6B", "#1A2744"),
    "scarlet": ("#F5B7B1", "#E74C3C", "#922B21"),
    "cognac": ("#F0C89D", "#C0792A", "#6E3B12"),
    "cream": ("#FDF6E3", "#E8D5B5", "#C4A97D"),
    "golden": ("#FEF3C7", "#F59E0B", "#B45309"),
    **_GRAY_COLORS,
}

HOCKNEY = ColorLibrary(
    name="hockney",
    background="#ffffff",
    text="#000000",
    default_color_name="cobalt",
    colors=_HOCKNEY_COLORS,
    iterable_keys=[
        "cobalt", "turquoise", "pink", "navy",
        "scarlet", "cognac", "cream", "golden",
    ],
)


# ---------------------------------------------------------------------------
# Registry — maps user-facing string names to library instances
# ---------------------------------------------------------------------------

COLOR_LIBRARIES: Dict[str, ColorLibrary] = {
    "extended": EXTENDED,
    "neon": NEON,
    "gouache": GOUACHE,
    "bloom": BLOOM,
    "hockney": HOCKNEY,
}


def get_library(name: str, func_name: str = "chart") -> ColorLibrary:
    """Return the ``ColorLibrary`` for *name*, or raise with helpful message."""
    if name in COLOR_LIBRARIES:
        return COLOR_LIBRARIES[name]
    options = ", ".join(f'"{k}"' for k in COLOR_LIBRARIES)
    raise ValueError(
        f'ql.{func_name}() error: invalid value for \'colors\': "{name}"\n\n'
        f"Valid options for colors: {options}"
    )


def resolve_color(
    library: ColorLibrary,
    color: Union[str, tuple, list],
    func_name: str,
) -> ColorTuple:
    """Resolve a user-facing color value to a concrete (fill, line, edge) tuple.

    Accepted inputs:
        - A color name string (e.g. ``"blue"``) looked up in the library.
        - The special name ``"default"`` for the library's default color.
        - A raw hex string (e.g. ``"#ff0000"``) used for all three slots.
        - A 3-element tuple/list of hex strings passed through as-is.
    """
    if isinstance(color, str):
        if color.startswith("#"):
            return (color, color, color)
        try:
            return library.get(color)
        except KeyError:
            available = ", ".join(f'"{c}"' for c in library.list_colors())
            raise ValueError(
                f'ql.{func_name}() error: invalid value for \'color\': "{color}"\n\n'
                f"Available colors in the {library.name} library: {available}"
            )
    if isinstance(color, (list, tuple)) and len(color) == 3:
        return (color[0], color[1], color[2])
    raise TypeError(
        f"ql.{func_name}() error: 'color' must be a color name string "
        f'(e.g., "blue") or a tuple of 3 hex strings.\n\n'
        f"Received: {type(color).__name__} = {color!r}"
    )

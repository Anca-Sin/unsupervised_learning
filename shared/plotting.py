"""Plot style, the colors, and the save helper."""
from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.figure import Figure

# eight colors, selected by number
PALETTE: list[str] = [
    "#1f77b4",  # 0: blue
    "#d62728",  # 1: red, MPV
    "#2ca02c",  # 2: green
    "#9467bd",  # 3: purple
    "#ff7f0e",  # 4: orange
    "#8c564b",  # 5: brown
    "#e377c2",  # 6: pink
    "#7f7f7f",  # 7: gray
]

# the classes' colors, class j in CLASS_COLORS[j]: the palette, with the smallest class (7) in black
CLASS_COLORS: list[str] = [*PALETTE[:7], "#000000"]
# one dot for every picture of the deaths by class (the MDS picture, the US map): its size and opacity
CLASS_DOT_SIZE: float = 3
CLASS_DOT_ALPHA: float = 0.8


def setup_plotting() -> None:
    """The shared plot style: seaborn's white background with a light grid,
    10x6-inch figures, and the label font size."""
    sns.set_theme(style="whitegrid")
    plt.rcParams["figure.figsize"] = (10, 6)
    plt.rcParams["axes.labelsize"] = 11


def save_fig(fig: Figure, name: str, out_dir: Path, show: bool = True) -> None:
    """Save `fig` as `out_dir/<name>.png` at 200 dpi, then show it under the cell (`show=False`: saved only).
    Creates `out_dir` if needed.
    """
    out_dir.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_dir / f"{name}.png", dpi=200, bbox_inches="tight")
    if show:
        plt.show()
    else:
        plt.close(fig)

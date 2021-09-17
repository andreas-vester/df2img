from pathlib import Path
from typing import Optional, List, Literal

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


def df2img(
    df: pd.DataFrame,
    file: Optional[Path] = None,
    show_fig: bool = False,
    title: str = None,
    title_loc: Literal["center", "left", "right"] = "center",
    header_rows: int = 1,
    header_cols: int = 1,
    header_color: str = "black",
    header_bgcolor: str = "white",
    row_bgcolors: List[str] = None,
    edge_color: str = "gray",
    col_width: float = 3.0,
    row_height: float = 0.625,
    font_size: float = 14.0,
) -> (plt.figure, plt.table):
    """
    Converts a Pandas DataFrame into a matplotlib table and saves it as an
    image file (e.g. png or jpy).

    `df.index` will be plotted as the index column. This column's header will be
    equivalent to `df.index.name`. Likewise, `df.columns` will be used for the column
    headings.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame that will be converted into image file.
    file : Path, optional, default None
        If `None`, converted DataFrame will not be saved.
        If not `None`, filename of image file.
    show_fig : bool, default False
        If True, plot will be displayed.
    title : Literal["center", "left", "right"], default None
        Title text.
    title_loc : str, default "center"
        Set location of `title`. Can be either "center", "left", or "right"
    header_rows : int, default False
        Number of rows that will be treated as headers. These rows do have a
        different background color (`header_bgcolor`).
    header_cols : int, default False
        Number of columns that will be treated as headers. These columns will be
        printed in bold.
    header_color : str, default "white"
        Text color in headers.
    header_bgcolor : str, default "#DB0011"
        Color in HEX format.
    row_bgcolors : List[str] = ["#d7d8d6", "#ffffff"]
        If `row_bgcolors` contains more than one element, the row background colors
        will alternate.
    edge_color : str, default "white"
        Grid color of the DataFrame.
    col_width : float, default 3,0
        Column width.
    row_height : float, default 0.625
        Row height.
    font_size : float, default 14.0
        Font size.

    Returns
    -------
    (plt.fig, plt.Table)
    """
    # some basic input parsing
    assert title is None or isinstance(title, str), "`title` must be of type `str`."
    assert title_loc in [
        "center",
        "left",
        "right",
    ], "`title_loc` must be in ['center', 'left', 'right']"
    assert isinstance(header_rows, int), "`header_rows` must be of type `int`."
    assert isinstance(header_cols, int), "`header_cols` must be of type `int`."
    assert isinstance(header_color, str), "`header_color` must be of type `str`."
    assert isinstance(header_bgcolor, str), "`header_bgcolor` must be of type `str`."
    assert row_bgcolors is None or isinstance(
        row_bgcolors, list
    ), "`row_bgcolors` must be of type `List[str]`."
    assert isinstance(edge_color, str), "`edge_color` must be of type `str`."
    assert isinstance(col_width, float), "`col_width` must be of type `float`."
    assert isinstance(row_height, float), "`row_height` must be of type `float`."
    assert isinstance(font_size, float), "`font_size` must be of type `float`."

    if row_bgcolors is None:
        row_bgcolors = ["white"]

    df = df.reset_index()  # reset the dataframe index to allow for plotting it

    bbox = [0, 0, 1, 1]  # bounding box to draw the table into

    # compute image size according to number of rows and columns
    size = (np.array(df.shape[::-1]) + np.array([0, 1])) * np.array(
        [col_width, row_height]
    )

    # create actual figure
    fig, ax = plt.subplots(figsize=size)
    ax.axis("off")  # turn off axis labels
    mpl_table = ax.table(
        cellText=df.values,
        colLabels=df.columns,
        bbox=bbox,
    )
    mpl_table.auto_set_font_size(False)
    mpl_table.set_fontsize(font_size)

    # format header rows and cols and alternate every other row's color
    for k, cell in mpl_table.get_celld().items():  # k returns (row, col) tuple
        cell.set_edgecolor(edge_color)
        cell.set_facecolor(row_bgcolors[k[0] % len(row_bgcolors)])
        if k[0] in range(header_rows):  # check if current row is header row
            cell.set_text_props(
                weight="bold",
                color=header_color,
                horizontalalignment="center",
            )
            cell.set_facecolor(header_bgcolor)
        if k[1] in range(header_cols):  # check if current column is header column
            cell.set_text_props(
                weight="bold",
                horizontalalignment="left",
            )

    if title:
        ax.set_title(
            title,
            fontdict=dict(fontsize=font_size + 1, fontweight="bold"),
            loc=title_loc,
        )

    plt.tight_layout()

    if show_fig:
        plt.show()

    if file:
        fig.savefig(file)

    return fig, mpl_table

from pathlib import Path
from typing import Optional, List, Literal, Union

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
    fig_width: Union[int, float] = 7.0,
    auto_col_width: bool = True,
    col_width: Optional[List[Union[int, float]]] = None,
    row_height: Union[int, float] = 0.5,
    font_size: Union[int, float] = 10.0,
) -> (plt.figure, plt.table):
    """
    Converts a Pandas DataFrame into a matplotlib table and saves it as an
    image file (e.g. png or jpg).

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
    fig_width : float, default 7,0
        Column width.
    auto_col_width : bool, default True
        If True, auto-sizes the column widths.
        Takes precedence over `col_width`.
    col_width : List[float], default None
        List of `float` specifying the relative column width. For example,
        if the dataframe has three columns, `[0.25, 0.5, 0.25]` would indicate that
        the second column's width is double the width of the first and third column.
        If `None`, all columns will have the same width.
        If `auto_col_width` is True, `col_width` will be ignored.
    row_height : float, default 0.5
        Row height.
    font_size : float, default 10.0
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
    assert isinstance(
        fig_width, (int, float)
    ), "`fig_width` must be of type `int` or `float`."
    if col_width is not None:
        assert isinstance(
            col_width, list
        ), "`col_width` must be of a `list` containing `int` or `float`"
    if col_width is not None:
        assert len(col_width) == len(df.columns) + 1, (
            f"len(col_width) == {len(col_width)}, while len(df.columns) == "
            f"{len(df.columns) + 1}. "
            f"Please provide a value for every column in your dataframe."
        )
    assert isinstance(
        row_height, (int, float)
    ), "`row_height` must be of type `int` or `float`."
    assert isinstance(
        font_size, (int, float)
    ), "`font_size` must be of type `int` or `float`."

    if row_bgcolors is None:
        row_bgcolors = ["white"]

    df = df.reset_index()  # reset the dataframe index to allow for plotting it

    bbox = [0, 0, 1, 1]  # bounding box to draw the table into

    # compute image size according to number of rows and columns
    size = (fig_width, len(df) * row_height)

    # create actual figure
    fig, ax = plt.subplots(figsize=size)
    ax.axis("off")  # turn off axis labels
    mpl_table = ax.table(
        cellText=df.values,
        colLabels=df.columns,
        bbox=bbox,
        colWidths=col_width,
    )
    mpl_table.auto_set_font_size(False)
    mpl_table.set_fontsize(font_size)
    if auto_col_width:
        mpl_table.auto_set_column_width(col=list(range(len(df.columns))))

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

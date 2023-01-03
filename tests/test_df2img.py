"""Test functions in df2img.py."""

from pathlib import Path

import pandas as pd
import plotly.graph_objects as go
import pytest

import df2img


@pytest.fixture(scope="module")
def df_without_index() -> pd.DataFrame:
    """Return `pd.DataFrame` with string and float columns without index column."""
    return pd.DataFrame(
        data={
            "float_col": [1.4, float("NaN"), 250, 24.65],
            "str_col": ("string1", "string2", float("NaN"), "string4"),
        },
    )


@pytest.fixture(scope="module")
def df_with_index_even_row_count() -> pd.DataFrame:
    """Return `pd.DataFrame` with an even number (4) of rows."""
    return pd.DataFrame(
        data={
            "float_col": [1.4, float("NaN"), 250, 24.65],
            "str_col": ("string1", "string2", float("NaN"), "string4"),
        },
        index=["row1", "row2", "row3_with_a_long_string", "row4"],
    )


@pytest.fixture(scope="module")
def df_with_index_odd_row_count() -> pd.DataFrame:
    """Return `pd.DataFrame` with an odd number (5) of rows."""
    return pd.DataFrame(
        data={
            "float_col": [1.4, float("NaN"), 250, 24.65, 100],
            "str_col": ("string1", "string2", float("NaN"), "string4", "last_string"),
        },
        index=["row1", "row2", "row3_with_a_long_string", "row4", "last_row"],
    )


def test_version() -> None:
    """It checks the correct version number."""
    assert df2img.__version__ == "0.2.9"


# noinspection PyUnresolvedReferences
def test_plot_dataframe_without_args(df_without_index: pd.DataFrame) -> None:
    """It plots a dataframe without providing any additional arguments."""
    fig = df2img.plot_dataframe(df=df_without_index, print_index=False, show_fig=False)

    assert isinstance(fig, go.Figure)
    assert fig.layout.title.__getattribute__("text") is None
    assert fig.data[0].header.values == ("<b>float_col<b>", "<b>str_col<b>")


# noinspection PyUnresolvedReferences
def test_plot_dataframe_without_args_print_index(
    df_with_index_even_row_count: pd.DataFrame,
) -> None:
    """It plots a dataframe with the index column."""
    fig = df2img.plot_dataframe(
        df=df_with_index_even_row_count, print_index=True, show_fig=False
    )

    assert isinstance(fig, go.Figure)
    assert fig.layout.title.__getattribute__("text") is None
    assert fig.data[0].header.values == ("<b><b>", "<b>float_col<b>", "<b>str_col<b>")


def test_plot_dataframe_title_text(df_with_index_even_row_count: pd.DataFrame) -> None:
    """It plots a dataframe with a title."""
    fig = df2img.plot_dataframe(
        df=df_with_index_even_row_count,
        print_index=True,
        title={
            "font_color": "red",
            "font_family": "Arial",
            "font_size": 20,
            "text": "This is a title",
            "x": 0.1,
            "xanchor": "right",
        },
        show_fig=False,
    )

    assert fig.layout.title.font.color == "red"
    assert fig.layout.title.font.family == "Arial"
    assert fig.layout.title.font.size == 20
    assert fig.layout.title.text == "This is a title"
    assert fig.layout.title.x == 0.1
    assert fig.layout.title.xanchor == "right"


def test_plot_dataframe_header(df_with_index_even_row_count: pd.DataFrame) -> None:
    """It plots a dataframe with formatted column headers."""
    fig = df2img.plot_dataframe(
        df=df_with_index_even_row_count,
        tbl_header={
            "align": "right",
            "fill_color": "blue",
            "font_color": "white",
            "font_family": "Arial",
            "font_size": 14,
            "height": 20,
            "line_width": 2,
        },
        show_fig=False,
    )

    assert fig.data[0].header.align == "right"
    assert fig.data[0].header.fill.color == "blue"
    assert fig.data[0].header.font.color == "white"
    assert fig.data[0].header.font.family == "Arial"
    assert fig.data[0].header.font.size == 14
    assert fig.data[0].header.height == 20
    assert fig.data[0].header.line.width == 2


def test_plot_dataframe_header_invisible(
    df_with_index_even_row_count: pd.DataFrame,
) -> None:
    """`table_header_visible` argument takes precedence over `tbl_header`."""
    fig = df2img.plot_dataframe(
        df=df_with_index_even_row_count,
        tbl_header_visible=False,
        tbl_header={
            "align": "right",
            "fill_color": "blue",
            "font_color": "black",
            "line_color": "gray",
            "font_family": "Arial",
            "font_size": 14,
            "height": 100,
            "line_width": 2,
        },
        show_fig=False,
    )

    assert fig.data[0].header.fill.color == "white"
    assert fig.data[0].header.font.color == "white"
    assert fig.data[0].header.line.color == "white"
    assert fig.data[0].header.height == 1


def test_plot_dataframe_cells(df_with_index_even_row_count: pd.DataFrame) -> None:
    """It plots a dataframe with formatted cells."""
    fig = df2img.plot_dataframe(
        df=df_with_index_even_row_count,
        tbl_cells={
            "align": "left",
            "fill_color": "darkred",
            "font_color": "lightblue",
            "font_family": "Times New Roman",
            "font_size": 10,
            "height": 30,
            "line_width": 1.5,
        },
        show_fig=False,
    )

    assert fig.data[0].cells.align == "left"
    assert fig.data[0].cells.fill.color == "darkred"
    assert fig.data[0].cells.font.color == "lightblue"
    assert fig.data[0].cells.font.family == "Times New Roman"
    assert fig.data[0].cells.font.size == 10
    assert fig.data[0].cells.height == 30
    assert fig.data[0].cells.line.width == 1.5


def test_plot_dataframe_row_fill_color_even_row_count(
    df_with_index_even_row_count: pd.DataFrame,
) -> None:
    """It plots a dataframe with even row numbers with alternating row colors."""
    fig = df2img.plot_dataframe(
        df=df_with_index_even_row_count,
        row_fill_color=("white", "lightgray"),
        show_fig=False,
    )

    assert fig.data[0].cells.fill.color == (
        ["white", "lightgray", "white", "lightgray"],
        ["white", "lightgray", "white", "lightgray"],
        ["white", "lightgray", "white", "lightgray"],
        ["white", "lightgray", "white", "lightgray"],
    )


def test_plot_dataframe_row_fill_color_odd_row_count(
    df_with_index_odd_row_count: pd.DataFrame,
) -> None:
    """It plots a dataframe with odd row numbers with alternating row colors."""
    fig = df2img.plot_dataframe(
        df=df_with_index_odd_row_count,
        row_fill_color=("white", "lightgray"),
        show_fig=False,
    )

    assert fig.data[0].cells.fill.color == (
        ["white", "lightgray", "white", "lightgray", "white"],
        ["white", "lightgray", "white", "lightgray", "white"],
        ["white", "lightgray", "white", "lightgray", "white"],
        ["white", "lightgray", "white", "lightgray", "white"],
        ["white", "lightgray", "white", "lightgray", "white"],
    )


def test_plot_dataframe_col_width(df_with_index_even_row_count: pd.DataFrame) -> None:
    """It plots a dataframe with different column widths."""
    fig = df2img.plot_dataframe(
        df=df_with_index_even_row_count,
        col_width=[3, 2, 1],
        show_fig=False,
    )

    assert fig.data[0].columnwidth == (3, 2, 1)


def test_plot_dataframe_fig_size(df_with_index_even_row_count: pd.DataFrame) -> None:
    """It plots a dataframe with specified figure size."""
    fig = df2img.plot_dataframe(
        df=df_with_index_even_row_count,
        fig_size=(400, 200),
        show_fig=False,
    )

    assert fig.layout.width == 400
    assert fig.layout.height == 200


def test_plot_dataframe_paper_bgcolor_rgba(
    df_with_index_even_row_count: pd.DataFrame,
) -> None:
    """It plots a dataframe with background color specified as RGB values."""
    fig = df2img.plot_dataframe(
        df=df_with_index_even_row_count,
        paper_bgcolor="rgba(0, 0, 0, 0)",
        show_fig=False,
    )

    assert fig.layout.paper_bgcolor == "rgba(0, 0, 0, 0)"


def test_plot_dataframe_paper_bgcolor_string(
    df_with_index_even_row_count: pd.DataFrame,
) -> None:
    """It plots a dataframe with background color specified as string value."""
    fig = df2img.plot_dataframe(
        df=df_with_index_even_row_count,
        paper_bgcolor="yellow",
        show_fig=False,
    )

    assert fig.layout.paper_bgcolor == "yellow"


def test_save_dataframe(df_without_index: pd.DataFrame) -> None:
    """It saves a dataframe as 'testfile.png'."""
    fig = df2img.plot_dataframe(df=df_without_index, show_fig=False)

    filename = Path(__file__).parent.joinpath("testfile.png")
    df2img.save_dataframe(fig=fig, filename=filename)

    assert filename.is_file()
    filename.unlink()  # delete file


def test_show_fig_without_error(df_without_index: pd.DataFrame) -> None:
    """It shows the figure using the default renderer."""
    df2img.plot_dataframe(df=df_without_index, show_fig=True)

import pandas as pd
import pytest

from df2img import __version__
from df2img.df2img import df2img
from matplotlib import pyplot as plt


@pytest.fixture(scope="module")
def df_without_index():
    return pd.DataFrame(
        data=dict(
            float_col=[1.4, float("NaN"), 250, 24.65],
            str_col=("string1", "string2", float("NaN"), "string4"),
        ),
    )


@pytest.fixture(scope="module")
def df_with_index():
    return pd.DataFrame(
        data=dict(
            float_col=[1.4, float("NaN"), 250, 24.65],
            str_col=("string1", "string2", float("NaN"), "string4"),
        ),
        index=["row1", "row2", "row3_with_a_long_string", "row4"],
    )


def test_version():
    assert __version__ == "0.1.0"


# noinspection PyTypeChecker
def test_title_assertion(df_with_index):
    with pytest.raises(AssertionError) as err:
        df2img(df=df_with_index, title=123)

    assert str(err.value) == "`title` must be of type `str`."


# noinspection PyTypeChecker
def test_title_loc_assertion(df_with_index):
    with pytest.raises(AssertionError) as err:
        df2img(df=df_with_index, title_loc="foo")

    assert str(err.value) == "`title_loc` must be in ['center', 'left', 'right']"

    assert df2img(df=df_with_index, title_loc="center")
    assert df2img(df=df_with_index, title_loc="left")
    assert df2img(df=df_with_index, title_loc="right")
    plt.close()


# noinspection PyTypeChecker
def test_header_rows_assertion(df_with_index):
    with pytest.raises(AssertionError) as err:
        df2img(df=df_with_index, header_rows="foo")

    assert str(err.value) == "`header_rows` must be of type `int`."


# noinspection PyTypeChecker
def test_header_cols_assertion(df_with_index):
    with pytest.raises(AssertionError) as err:
        df2img(df=df_with_index, header_cols="foo")

    assert str(err.value) == "`header_cols` must be of type `int`."


# noinspection PyTypeChecker
def test_header_color_assertion(df_with_index):
    with pytest.raises(AssertionError) as err:
        df2img(df=df_with_index, header_color=123)

    assert str(err.value) == "`header_color` must be of type `str`."


# noinspection PyTypeChecker
def test_header_bgcolor_assertion(df_with_index):
    with pytest.raises(AssertionError) as err:
        df2img(df=df_with_index, header_bgcolor=123)

    assert str(err.value) == "`header_bgcolor` must be of type `str`."


# noinspection PyTypeChecker
def test_row_bgcolors_assertion(df_with_index):
    with pytest.raises(AssertionError) as err:
        df2img(df=df_with_index, row_bgcolors=123)

    assert str(err.value) == "`row_bgcolors` must be of type `List[str]`."


# noinspection PyTypeChecker
def test_edge_color_assertion(df_with_index):
    with pytest.raises(AssertionError) as err:
        df2img(df=df_with_index, edge_color=123)

    assert str(err.value) == "`edge_color` must be of type `str`."


# noinspection PyTypeChecker
def test_col_width_assertion(df_with_index):
    with pytest.raises(AssertionError) as err:
        df2img(df=df_with_index, col_width="3")

    assert str(err.value) == "`col_width` must be of type `float`."


# noinspection PyTypeChecker
def test_row_height_assertion(df_with_index):
    with pytest.raises(AssertionError) as err:
        df2img(df=df_with_index, row_height="foo")

    assert str(err.value) == "`row_height` must be of type `float`."


# noinspection PyTypeChecker
def test_font_size_assertion(df_with_index):
    with pytest.raises(AssertionError) as err:
        df2img(df=df_with_index, font_size="foo")

    assert str(err.value) == "`font_size` must be of type `float`."


def test_original_index_name(df_without_index):
    _, tbl = df2img(df=df_without_index)

    assert tbl.get_celld()[0, 0]._text.get_text() == "index"
    plt.close()


def test_renamed_index_name(df_with_index):
    df_with_index.index.name = "foo"
    _, tbl = df2img(df=df_with_index)

    assert tbl.get_celld()[0, 0]._text.get_text() == "foo"
    plt.close()


def test_header_rows_content(df_without_index):
    _, tbl = df2img(df=df_without_index)

    assert tbl.get_celld()[0, 0]._text.get_text() == "index"
    assert tbl.get_celld()[0, 1]._text.get_text() == "float_col"
    assert tbl.get_celld()[0, 2]._text.get_text() == "str_col"
    plt.close()


def test_cell_content(df_without_index):
    _, tbl = df2img(df=df_without_index)

    assert tbl.get_celld()[1, 1]._text.get_text() == "1.4"
    assert tbl.get_celld()[2, 1]._text.get_text() == "nan"
    assert tbl.get_celld()[2, 2]._text.get_text() == "string2"
    plt.close()


@pytest.mark.parametrize("header_rows", [1, 2])
def test_header_rows_fontweight(df_with_index, header_rows):
    _, tbl = df2img(df=df_with_index, header_rows=header_rows)

    for i in range(header_rows):
        for j in range(df_with_index.shape[1]):
            assert tbl.get_celld()[i, j].get_text().get_fontweight() == "bold"
    plt.close()


@pytest.mark.parametrize("header_rows", [1, 2])
def test_header_rows_horizontalalignment(df_with_index, header_rows):
    _, tbl = df2img(df=df_with_index, header_rows=header_rows)

    for i in range(header_rows):
        for j in range(df_with_index.shape[1]):
            if j == 0:
                assert (
                    tbl.get_celld()[i, j].get_text().get_horizontalalignment() == "left"
                )
            else:
                assert (
                    tbl.get_celld()[i, j].get_text().get_horizontalalignment()
                    == "center"
                )
    plt.close()


@pytest.mark.parametrize("header_cols", [1, 2])
def test_header_cols_fontweight(df_with_index, header_cols):
    _, tbl = df2img(df=df_with_index, header_cols=header_cols)

    for i in range(df_with_index.shape[0]):
        for j in range(header_cols):
            assert tbl.get_celld()[i, j].get_text().get_fontweight() == "bold"
    plt.close()


@pytest.mark.parametrize("header_cols", [1, 2])
def test_header_cols_horizontalalignment(df_with_index, header_cols):
    _, tbl = df2img(df=df_with_index, header_cols=header_cols)

    # skip first row as we defined the first row as header row with
    # horizontalalignment == "center"
    for i in range(1, df_with_index.shape[0]):
        for j in range(header_cols):
            assert tbl.get_celld()[i, j].get_text().get_horizontalalignment() == "left"
    plt.close()


def test_title(df_with_index):
    fig, tbl = df2img(df_with_index, title="Title text")

    assert fig.gca().get_title() == "Title text"
    plt.close()

# df2img: Save a Pandas DataFrame as image

![img](https://img.shields.io/pypi/v/df2img)
![img](https://img.shields.io/pypi/pyversions/df2img)
![img](https://img.shields.io/github/license/andreas-vester/df2img)
![img](https://img.shields.io/github/issues/andreas-vester/df2img)
![img](https://img.shields.io/github/stars/andreas-vester/df2img)

## What is it all about?

Have you ever tried to save a ``pd.DataFrame`` into an image file? This is not a straightforward process at all. Unfortunately, ``pandas`` itself doesn't provide this functionality out of the box.

**df2img** tries to fill the gap. It is a Python library that greatly simplifies the process of saving a ``pd.DataFrame`` into an image file (e.g. ``png`` or ``jpg``).

It is a wrapper/convenience function in order to create a ``plotly`` Table. That is, one can use ``plotly``'s styling function to format the table.


## Dependencies

**df2img** has a limited number of dependencies, namely

- ``pandas``
- ``plotly``
- ``kaleido``


## Documentation

An extensive documentation is available at https://df2img.dev.

## Quickstart

You can install the package via ``pip``.

```bash
pip install df2img
```

Let's create a simple ``pd.DataFrame`` with some dummy data:

```python
import pandas as pd

import df2img

df = pd.DataFrame(
    data=dict(
        float_col=[1.4, float("NaN"), 250, 24.65],
        str_col=("string1", "string2", float("NaN"), "string4"),
    ),
    index=["row1", "row2", "row3", "row4"],
)
```
```python
      float_col  str_col
row1       1.40  string1
row2        NaN  string2
row3     250.00      NaN
row4      24.65  string4
```

### Basics

Saving ``df`` into a png-file now takes just two lines of code including some styling out of the box.

* First, we create a ``plotly`` figure.
* Second, we save the figure to disk.

```python
fig = df2img.plot_dataframe(df, fig_size=(500, 140))

df2img.save_dataframe(fig=fig, filename="plot1.png")
```

![img](https://github.com/andreas-vester/df2img/blob/main/docs/img/plot1.png?raw=true)


### Formatting

You can control the settings for the header row via the ``tbl_header`` input argument. This accepts a regular ``dict``. This ``dict`` can comprise various key/value pairs that are also accepted by ``plotly``. All available key/value pairs can be seen at ``plotly``'s website at https://plotly.com/python/reference/table/#table-header.

Let's set the header row in a different color and size. Also, let's set the alignment to "left".

```python
fig = df2img.plot_dataframe(
    df,
    tbl_header=dict(
        align="left",
        fill_color="blue",
        font_color="white",
        font_size=14,
    ),
    fig_size=(500, 140),
)
```
![img](https://github.com/andreas-vester/df2img/blob/main/docs/img/plot2.png?raw=true)


Controlling the table body (cells) is basically the same. Just use the ``tbl_cells`` input argument, which happens to be a ``dict``, too.
See https://plotly.com/python/reference/table/#table-cells for all the possible key/value pairs.

Let's print the table cell values in yellow on a green background and align them "right".

```python
fig = df2img.plot_dataframe(
    df,
    tbl_cells=dict(
        align="right",
        fill_color="green",
        font_color="yellow",
    ),
    fig_size=(500, 140),
)
```

![img](https://github.com/andreas-vester/df2img/blob/main/docs/img/plot3.png?raw=true)


You can alternate row colors for better readability by using the ``row_fill_color`` input argument. Using HEX colors is also possible:

```python
fig = df2img.plot_dataframe(
    df,
    row_fill_color=("#ffffff", "#d7d8d6"),
    fig_size=(500, 140),
)
```

![img](https://github.com/andreas-vester/df2img/blob/main/docs/img/plot4.png?raw=true)


Setting the title will be controlled via the ``title`` input argument. You can find the relevant key/value pairs here: https://plotly.com/python/reference/layout/#layout-title.

Let's put the title in a different font and size. In addition, we can control the alignment via the ``x`` key/value pair. It sets the x (horizontal) position in normalized coordinates from "0" (left) to "1" (right).

```python
  fig = df2img.plot_dataframe(
      df,
      title=dict(
          font_color="darkred",
          font_family="Times New Roman",
          font_size=24,
          text="This is a title starting at the x-value x=0.1",
          x=0.1,
          xanchor="left",
      ),
      fig_size=(500, 140),
  )
  ```

![img](https://github.com/andreas-vester/df2img/blob/main/docs/img/plot5.png?raw=true)


You can also control relative column width via the ``col_width`` argument. Let's set the first column's width triple the width of the third column and the second column's width double the width of the third column.

```python
fig = df2img.plot_dataframe(
    df,
    col_width=[3, 2, 1],
    fig_size=(500, 140),
)
```

![img](https://github.com/andreas-vester/df2img/blob/main/docs/img/plot6.png?raw=true)

## Contributing to df2img

If you consider to contribute to **df2img**, please read the [Contributing to df2img](./CONTRIBUTING.md) section in the documentation. This document is supposed to guide you through the whole process.

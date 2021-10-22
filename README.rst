########################################
df2img: Save a Pandas DataFrame as image
########################################

What is it all about?
*********************
| Have you ever tried to save a ``pd.DataFrame`` into an image file? This is not a straightforward process at all. Unfortunately, ``pandas`` itself doesn't provide this functionality out of the box.
| **df2img** tries to fill the gap. It is a Python library that greatly simplifies the process of saving a ``pd.DataFrame`` into an image file (e.g. ``png`` or ``jpg``).

Dependencies
************
**df2img** has a limited number of dependencies, namely

- ``pandas``
- ``matplotlib``

Quickstart
**********

You can install the package via ``pip``.

.. code-block:: python

    pip install df2img

Let's create a simple ``pd.DataFrame`` with some dummy data:

.. code-block:: python

    import pandas as pd

    from df2img import df2img

    df = pd.DataFrame(
        data=dict(
            float_col=[1.4, float("NaN"), 250, 24.65],
            str_col=("string1", "string2", float("NaN"), "string4"),
        ),
        index=["row1", "row2", "row3", "row4"],
    )

.. code-block:: python

          float_col  str_col
    row1       1.40  string1
    row2        NaN  string2
    row3     250.00      NaN
    row4      24.65  string4

Basics
------

Saving ``df`` into a png-file is now a one-liner.

.. code-block:: python

    df2img(df, file="plot1.png")

.. image:: https://github.com/andreas-vester/df2img/blob/main/docs/plot1.png?raw=true
    :alt: plot1.png

Formatting
----------

Setting the header row in a different color:

.. code-block:: python

    df2img(
        df,
        file="plot2.png",
        header_color="white",
        header_bgcolor="darkred",
    )

.. image:: https://github.com/andreas-vester/df2img/blob/main/docs/plot2.png?raw=true
    :alt: plot2.png


You can alternate row colors for better readability. Using HEX colors is also possible:

.. code-block:: python

    df2img(
        df,
        file="plot3.png",
        header_color="white",
        header_bgcolor="darkred",
        row_bgcolors=["#d7d8d6", "#ffffff"],
    )

.. image:: https://github.com/andreas-vester/df2img/blob/main/docs/plot3.png?raw=true
    :alt: plot3.png


You can set the title and font size.

.. code-block:: python

    df2img(
        df,
        file="plot4.png",
        title="This is a title",
        title_loc="left",
        header_color="white",
        header_bgcolor="darkred",
        row_bgcolors=["#d7d8d6", "#ffffff"],
        font_size=15.0,
    )

.. image:: https://github.com/andreas-vester/df2img/blob/main/docs/plot4.png?raw=true
    :alt: plot4.png


When turning off ``auto_col_width``, you can also control relative column width via the ``col_width`` argument. Let's set the first column's width triple the width of the third column and the second column's width double the width of the third column.

.. code-block:: python

    df2img(
        df,
        file="plot5.png",
        title="This is a title",
        title_loc="left",
        header_color="white",
        header_bgcolor="darkred",
        row_bgcolors=["#d7d8d6", "#ffffff"],
        font_size=8.0,
        auto_col_width=False,
        col_width=[3, 2, 1,],
    )

.. image:: https://github.com/andreas-vester/df2img/blob/main/docs/plot5.png?raw=true
    :alt: plot5.png


Too much white-space? - Let's reduce the width of the overall figure.

.. code-block:: python

    df2img(
        df,
        file="plot6.png",
        title="This is a title",
        title_loc="right",
        header_color="white",
        header_bgcolor="darkred",
        row_bgcolors=["#d7d8d6", "#ffffff"],
        font_size=8.0,
        auto_col_width=False,
        col_width=[3, 2, 1,],
        fig_width=3.5,
    )

.. image:: https://github.com/andreas-vester/df2img/blob/main/docs/plot6.png?raw=true
    :alt: plot6.png

Contributing to df2img
**********************
All bug reports and bug fixes, improvements to the documentation, or general ideas are welcome. Simply open an `issue <https://github.com/andreas-vester/df2img/issues>`_.


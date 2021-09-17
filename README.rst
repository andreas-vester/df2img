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

.. code:: python

    pip install df2img

Let's create a simple ``pd.DataFrame`` with some dummy data:

.. code:: python

    import pandas as pd

    from df2img import df2img

    df = pd.DataFrame(
        data=dict(
            float_col=[1.4, float("NaN"), 250, 24.65],
            str_col=("string1", "string2", float("NaN"), "string4"),
        ),
        index=["row1", "row2", "row3", "row4"],
    )

.. code::

          float_col  str_col
    row1       1.40  string1
    row2        NaN  string2
    row3     250.00      NaN
    row4      24.65  string4

Basics
------

Saving ``df`` into a png-file is now a one-liner.

.. code:: python

    df2img(df, file="plot1.png")

.. image:: https://github.com/andreas-vester/df2img/blob/main/docs/plot1.png?raw=true
    :alt: plot1.png

Formatting
----------

Setting the header row in a different color:

.. code:: python

    df2img(
        df,
        file="plot2.png",
        header_color="white",
        header_bgcolor="darkred",
    )

.. image:: https://github.com/andreas-vester/df2img/blob/main/docs/plot2.png?raw=true
    :alt: plot2.png


| You can alternate row colors for better readability. Using HEX colors is also possible:

.. code:: python

    df2img(
        df,
        file="plot3.png",
        header_color="white",
        header_bgcolor="darkred",
        row_bgcolors=["#d7d8d6", "#ffffff"],
    )

.. image:: https://github.com/andreas-vester/df2img/blob/main/docs/plot3.png?raw=true
    :alt: plot3.png


| Setting the title, font size, column width, and row height:

.. code:: python

    df2img(
        df,
        file="plot4.png",
        title="This is a title",
        title_loc="left",
        header_color="white",
        header_bgcolor="darkred",
        row_bgcolors=["#d7d8d6", "#ffffff"],
        font_size=10.0,
        col_width=1.5,
        row_height=0.3
    )

.. image:: https://github.com/andreas-vester/df2img/blob/main/docs/plot4.png?raw=true
    :alt: plot4.png

Contributing to df2img
**********************
All bug reports and bug fixes, improvements to the documentation, or general ideas are welcome. Simply open an `issue <https://github.com/andreas-vester/df2img/issues>`_.


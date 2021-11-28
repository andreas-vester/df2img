.. df2img documentation master file, created by
   sphinx-quickstart on Sat Nov 20 17:25:05 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

df2img: Save a Pandas DataFrame as image
########################################

What is it all about?
*********************
Have you ever tried to save a ``pd.DataFrame`` into an image file? This is not a straightforward process at all.
Unfortunately, ``pandas`` itself doesn't provide this functionality out of the box.

**df2img** tries to fill the gap. It is a Python library that greatly simplifies the process of saving a
``pd.DataFrame`` into an image file (e.g. ``png`` or ``jpg``).

It provides wrapper/convenience functions in order to create a table using the excellent `plotly`_ library. As a
result, one can use `plotly's styling functions`_ to format the table.

.. _plotly: https://plotly.com/python/
.. _plotly's styling functions: https://plotly.com/python/reference/table/

Dependencies
************
**df2img** has a limited number of dependencies, namely

- ``pandas``
- ``plotly``
- ``kaleido``

.. toctree::
   :maxdepth: 1
   :caption: Contents:

   installation
   getting_started
   control_index
   formatting
   api_reference
   changelog

Contributing to df2img
**********************
The source code of **df2img** is available at `GitHub <https://github.com/andreas-vester/df2img>`_. All bug reports and
bug fixes, improvements to the documentation, or general ideas are welcome. Simply open an
`issue <https://github.com/andreas-vester/df2img/issues>`_.
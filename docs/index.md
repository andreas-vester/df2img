# df2img: Save a Pandas DataFrame as image

![img](https://img.shields.io/pypi/v/df2img)
![img](https://img.shields.io/pypi/pyversions/df2img)
![img](https://img.shields.io/github/license/andreas-vester/df2img)
![img](https://img.shields.io/github/issues/andreas-vester/df2img)
![img](https://img.shields.io/github/stars/andreas-vester/df2img)

## What is it all about?

Have you ever tried to save a ``pd.DataFrame`` into an image file? This is not a straightforward process at all. Unfortunately, ``pandas`` itself doesn't provide this functionality out of the box.

**df2img** (dataframe-to-image) tries to fill the gap. It is a Python library that greatly simplifies the process of saving a ``pd.DataFrame`` into an image file (e.g. ``png`` or ``jpg``).

It is a wrapper/convenience function in order to create a ``plotly`` Table. That is, one can use ``plotly``'s styling function to format the table.


## Dependencies

**df2img** has a limited number of dependencies, namely

- ``pandas``
- ``plotly``
- ``kaleido``

## Contents

* [Installation](installation.md)
* [Getting started](getting_started.ipynb)
* [Controlling the index column](control_index.ipynb)
* [Formatting](formatting.ipynb)
* [API Reference](api_reference.md)
* [Changelog](changelog.md)

## Contributing to df2img

All bug reports and bug fixes, improvements to the documentation, or general ideas are welcome. Simply open an [issue](https://github.com/andreas-vester/df2img/issues).

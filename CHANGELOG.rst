*********
Changelog
*********

The format is based on `Keep a changelog <https://keepachangelog.com/de/1.0.0/>`_.
This project adheres to `Semantic Versioning <https://semver.org/>`_.


[v0.2.5] - 2022-06-02
=====================

Changed
-------
- Integrated ``pre-commit`` with the following hooks:
  - id: trailing-whitespace
  - id: end-of-file-fixer
  - id: check-yaml
  - id: check-added-large-files
  - id: black
  - id: flake8
  - id: isort
- Updated dependencies (tested with pandas v1.4.2 and plotly v5.8.0).


[v0.2.4] - 2022-01-22
=====================

Changed
-------
- Updated extra dependencies.


[v0.2.3] - 2022-01-04
=====================

Added
-----
- | Added input argument ``**layout_kwargs`` to the ``plot_dataframe`` function.
  | This allows the user to make use of ``plotly``'s vast layout settings via passing through ``plotly`` related keyword arguments.
  | Further information can be found at https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html.


[v0.2.2] - 2021-11-28
=====================

Added
-----
- Added input argument ``plotly_renderer`` in order to select the appropriate renderer. For more information about
  ``plotly``'s renderers, visit the respective website at https://plotly.com/python/renderers/.
- Extensive documentation now available at https://df2img.readthedocs.io/en/latest/


[v0.2.1] - 2021-11-13
=====================

Added
-----
- | Possibility to hide the header row.
  | Added input argument ``tbl_header_visible`` to the ``plot_dataframe`` function, which controls the behavior. If set to `False`, the table header will
    be invisible. ``tbl_header_visible`` takes precedence over ``tbl_header`` input argument. That is, if you set it to
    `False`, it doesn't matter whether you provide the ``tbl_header`` argument.


[v0.2.0] - 2021-10-26
=====================

Changed
-------
| **BREAKING CHANGES**!
| Changed the backend from ``matplotlib`` to ``plotly``. As a result, function names and signature completely changed.

- Possibility to set various title formats/styles.
- Possibility to set various table header row formats/styles.
- Possibility to set various table cell formats/styles.
- Possibility to set figure size.

Added
-----
- Possibility to set alignment for individual columns
  (`GitHub issue #2 <https://github.com/andreas-vester/df2img/issues/2>`_).
- Possibility to set relative column widths (`GitHub issue #3 <https://github.com/andreas-vester/df2img/issues/3>`_).

Removed
-------
- | Function ``df2img``.
  | Has been replaced with ``plot_dataframe`` and ``save_dataframe``.


[v0.1.1] - 2021-10-02
=====================

Fixed
-----
- Input arguments ``col_width``, ``row_height``, and ``font_size`` now accept ``int``
  (`GitHub issue #1 <https://github.com/andreas-vester/df2img/issues/1>`_).


[v0.1.0] - 2021-09-17
=====================

Initial release.

Added
-----
- Possibility to save ``pd.DataFrame`` into image file (e.g. png or jpg).
- Possibility to add title to the image.
- Possibility to define the number of header rows and header columns.
- Possibility to change colors for header rows.
- Possibility to alternate row colors for better readability.
- Possibility to change column width and row height.
- Possibility to change font size.

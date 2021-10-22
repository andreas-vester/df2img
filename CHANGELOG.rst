*********
Changelog
*********

The format is based on `Keep a changelog <https://keepachangelog.com/de/1.0.0/>`_. This project adheres to `Semantic Versioning <https://semver.org/>`_.

[v0.2.0] - 2021-xx-xx
=====================

Added
-----
- | Input argument ``auto_col_width`` (`GitHub issue #3 <https://github.com/andreas-vester/df2img/issues/3>`_).
  | If set to ``True``, the column width of all columns will be automatically set.

Changed
-------
- | Input argument ``col_width`` (`GitHub issue #3 <https://github.com/andreas-vester/df2img/issues/3>`_).
  | Can be used to specify relative column width. For example,
        if the dataframe has three columns, ``[0.25, 0.5, 0.25]`` would indicate that
        the second column's width is double the width of the first and third column.

Contributors
------------
A total of 1 people contributed to this release. People with a "+" by their names contributed a patch for the first time.

- Andreas Vester

[v0.1.1] - 2021-10-02
=====================

Fixed
-----
- Input arguments ``col_width``, ``row_height``, and ``font_size`` now accept ``int`` (`GitHub issue #1 <https://github.com/andreas-vester/df2img/issues/1>`_).

Contributors
------------
A total of 1 people contributed to this release. People with a "+" by their names contributed a patch for the first time.

- Andreas Vester

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

Contributors
------------
A total of 1 people contributed to this release. People with a "+" by their names contributed a patch for the first time.

- Andreas Vester +
# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.2.15] - 2023-11-23
### Changed
- Make kaleido version dependent on operating system.

## [0.2.14] - 2023-11-08
### Fixed
- Issue with kaleido.

## [0.2.13] - 2023-11-06
### Changed
- Python 3.8 no longer supported.
- Updated dependencies.

## [0.2.12] - 2023-08-07
### Changed
- Replaced `poetry` with `pdm`.

### Fixed
- Issue with `kaleido` when using Windows that leads to a crash when using `df2img.save_dataframe` ([GH issue #58](https://github.com/andreas-vester/df2img/issues/58)).

### Security
- Updated dependencies.

## [0.2.11] - 2023-05-16
### Security
- Updated dependencies.

## [0.2.10] - 2023-04-05
### Improved
- Transitioned from [flake8](https://pypi.org/project/flake8/) to [ruff](https://pypi.org/project/ruff/).

### Security
- Updated dependencies.

## [0.2.9] - 2023-01-03
### Security
- Updated dependencies.

## [0.2.8] - 2022-11-01
### Improved
- Introduce **Contributing** section and **Code of conduct** to documentation.
- Using [nox](https://nox.thea.codes/) for testing:
    - Unit testing using pytest
    - Added pytest coverage report.
    - Linting using [flake8](https://flake8.pycqa.org/en/latest/).
    - Formatting using [black](https://black.readthedocs.io/en/stable/).
    - Type checking using [mypy](http://mypy-lang.org/)
- Increased test coverage to 100%.
- Use [python-kacl](https://pypi.org/project/python-kacl/) to maintain CHANGELOG.md.

## [0.2.7] - 2022-08-03
### Security
- Bumps [mistune](https://github.com/lepture/mistune) from 0.8.4 to 2.0.3.
  - [Release notes](https://github.com/lepture/mistune/releases)
  - [Changelog](https://github.com/lepture/mistune/blob/master/docs/changes.rst)
  - [Commits](https://github.com/lepture/mistune/compare/v0.8.4...v2.0.3)

  updated-dependencies:
  - dependency-name: mistune
    dependency-type: indirect

## [0.2.6] - 2022-08-03
### Improved
- Bumped direct dependencies
  - Bumps [pandas](https://github.com/pandas-dev/pandas) from 1.4.2 to 1.4.3.

    - [Release notes](https://pandas.pydata.org/pandas-docs/stable/whatsnew/index.html#version-1-4)
    - [Commits](https://github.com/pandas-dev/pandas/compare/v1.4.2...v1.4.3)

    updated-dependencies:
    - dependency-name: pandas
      dependency-type: direct

  - Bumps [plotly](https://github.com/plotly/plotly.py) from 5.8.0 to 5.9.0.

    - [Release notes](https://github.com/plotly/plotly.py/releases)
    - [Commits](https://github.com/plotly/plotly.py/compare/v5.8.0...5.9.0)

    updated-dependencies:
    - dependency-name: plotly
      dependency-type: direct
- Bumps various indirect dependencies to latest versions.

## [0.2.5] - 2022-06-02
### Improved
- Integrated ``pre-commit`` with the following hooks:
  - id: trailing-whitespace
  - id: end-of-file-fixer
  - id: check-yaml
  - id: check-added-large-files
  - id: black
  - id: flake8
  - id: isort
- Updated dependencies (tested with pandas v1.4.2 and plotly v5.8.0).

## [0.2.4] - 2022-01-22
### Improved
- Updated extra dependencies.

## [0.2.3] - 2022-01-04
### Added
- Input argument ``**layout_kwargs`` added to ``plot_dataframe`` function.
  This allows the user to make use of ``plotly``'s vast layout settings via passing through ``plotly`` related keyword arguments.
  Further information can be found at https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html.

## [0.2.2] - 2021-11-28
### Added
- Input argument ``plotly_renderer`` added in order to select the appropriate renderer.
For more information about ``plotly``'s renderers, visit the respective website at https://plotly.com/python/renderers/.
- Extensive documentation now available at https://df2img.dev.

## [0.2.1] - 2021-11-13
### Added
- Possibility to hide the header row.
  Added input argument ``tbl_header_visible`` to the ``plot_dataframe`` function, which controls the behavior. If set to `False`, the table header will be invisible. ``tbl_header_visible`` takes precedence over ``tbl_header`` input argument. That is, if you set it to `False`, it doesn't matter whether you provide the ``tbl_header`` argument.

## [0.2.0] - 2021-10-26
### Added
- Possibility to set alignment for individual columns
  ([GH #2](https://github.com/andreas-vester/df2img/issues/2)).
- Possibility to set relative column widths ([GH #3](https://github.com/andreas-vester/df2img/issues/3)).

### Changed
- **BREAKING CHANGES**: Changed the backend from ``matplotlib`` to ``plotly``. As a result, function names and signature completely changed.
- Possibility to set various title formats/styles.
- Possibility to set various table header row formats/styles.
- Possibility to set various table cell formats/styles.
- Possibility to set figure size.

### Removed
- Function ``df2img``.
  Has been replaced with ``plot_dataframe`` and ``save_dataframe``.

## [0.1.1] - 2021-10-02
### Fixed
- Input arguments ``col_width``, ``row_height``, and ``font_size`` now accept ``int`` ([GH issue #1](https://github.com/andreas-vester/df2img/issues/1)).

## [0.1.0] - 2021-09-17
### Added
- Possibility to save ``pd.DataFrame`` into image file (e.g. png or jpg).
- Possibility to add title to the image.
- Possibility to define the number of header rows and header columns.
- Possibility to change colors for header rows.
- Possibility to alternate row colors for better readability.
- Possibility to change column width and row height.
- Possibility to change font size.

[Unreleased]: https://github.com/andreas-vester/df2img/compare/v0.2.15...HEAD
[0.2.15]: https://github.com/andreas-vester/df2img/compare/v0.2.14...v0.2.15
[0.2.14]: https://github.com/andreas-vester/df2img/compare/v0.2.13...v0.2.14
[0.2.13]: https://github.com/andreas-vester/df2img/compare/v0.2.12...v0.2.13
[0.2.12]: https://github.com/andreas-vester/df2img/compare/v0.2.11...v0.2.12
[0.2.11]: https://github.com/andreas-vester/df2img/compare/v0.2.10...v0.2.11
[0.2.10]: https://github.com/andreas-vester/df2img/compare/v0.2.9...v0.2.10
[0.2.9]: https://github.com/andreas-vester/df2img/compare/0.2.8...0.2.9
[0.2.8]: https://github.com/andreas-vester/df2img/compare/v0.2.7...v0.2.8
[0.2.7]: https://github.com/andreas-vester/df2img/compare/v0.2.6...v0.2.7
[0.2.6]: https://github.com/andreas-vester/df2img/compare/v0.2.5...v0.2.6
[0.2.5]: https://github.com/andreas-vester/df2img/compare/v0.2.4...v0.2.5
[0.2.4]: https://github.com/andreas-vester/df2img/compare/v0.2.3...v0.2.4
[0.2.3]: https://github.com/andreas-vester/df2img/compare/v0.2.2...v0.2.3
[0.2.2]: https://github.com/andreas-vester/df2img/compare/v0.2.1...v0.2.2
[0.2.1]: https://github.com/andreas-vester/df2img/compare/v0.2.0...v0.2.1
[0.2.0]: https://github.com/andreas-vester/df2img/compare/v0.1.1...v0.2.0
[0.1.1]: https://github.com/andreas-vester/df2img/compare/v0.1.0...v0.1.1
[0.1.0]: https://github.com/andreas-vester/df2img/releases/tag/v0.1.0

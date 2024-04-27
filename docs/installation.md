# Installation

**df2img** is available at [pypi.org](https://pypi.org/project/df2img).

You can install the package via ``pip``.

```bash
pip install df2img
```
Using ``poetry`` or ``pdm``?

```bash
poetry add df2img
pdm add df2img
```

## Important note
The ``kaleido`` dependency is needed to save a ``pd.DataFrame``. Right now there is an
issue when using the latest version of ``kaleido``.
This project requires ``kaleido==v0.2.1`` when you are installing ``df2img`` on a
machine other than Windows.
However, when you're on a Windows machine, you must use ``kaleido==v0.1.0.post1``.
The dependency specification in the ``pyproject.toml`` file takes care of this.

Having said this, if you're not on Windows and using the
[pdm](https://pdm-project.org/en/stable/) package manager, ``kaleido`` won't get
installed at all due to a [bug](https://github.com/pdm-project/pdm/issues/46) in
[pdm](https://pdm-project.org/en/stable/). In that case the following workaround might
be helpful:
- activate your virtual environment: ``source .venv/bin/activate``
- use ``pip`` in order to install ``kaleido`` separately: ``pip install kaleido==0.2.1``

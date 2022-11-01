"""Configuration file for `nox`."""

import tempfile
from typing import Any

import nox
from nox.sessions import Session

locations = "src", "tests", "./noxfile.py"
nox.options.sessions = "pre-commit", "tests", "mypy"
python_versions = ["3.8", "3.9", "3.10", "3.11"]


def install_with_constraints(session: Session, *args: str, **kwargs: Any) -> None:
    """
    Install packages constrained by Poetry's lock file.

    This function is a wrapper for nox.sessions.Session.install. It invokes pip to
    install packages inside the session's virtualenv.
    Additionally, pip is passed a constraints file generated from Poetry's lock file,
    to ensure that the packages are pinned to the versions specified in poetry.lock.
    This allows you to manage the packages as Poetry development dependencies.

    Parameters
    ----------
    session
        The Session object.
    args
        Command-line arguments for pip.
    kwargs
        Additional keyword arguments for Session.install.

    """
    with tempfile.NamedTemporaryFile() as requirements:
        session.run(
            "poetry",
            "export",
            "--without-hashes",
            "--format=requirements.txt",
            f"--output={requirements.name}",
            external=True,
        )
        session.install(f"--constraint={requirements.name}", *args, **kwargs)


@nox.session(python=python_versions)
def tests(session: Session) -> None:
    """Run the test suite using pytest."""
    args = session.posargs or ["--cov"]
    session.run("poetry", "install", "--without", "docs,dev", external=True)
    install_with_constraints(session, "coverage[toml]", "pytest", "pytest-cov")
    session.run("pytest", *args)


@nox.session(name="pre-commit", python=python_versions[-1])
def precommit(session: Session) -> None:
    """Lint using pre-commit."""
    args = session.posargs or [
        "run",
        "--all-files",
    ]
    install_with_constraints(
        session,
        "autoflake",
        "black",
        "flake8",
        "flake8-annotations",
        "flake8-bandit",
        "flake8-bugbear",
        "flake8-builtins",
        "flake8-comprehensions",
        "flake8-docstrings",
        "flake8-eradicate",
        "isort",
        "mypy",
        "pep8-naming",
        "pre-commit",
    )
    session.run("pre-commit", *args)


@nox.session(python=python_versions)
def mypy(session: Session) -> None:
    """Type-check using mypy."""
    args = session.posargs or locations
    install_with_constraints(session, "mypy")
    session.run("mypy", *args)

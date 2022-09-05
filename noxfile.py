"""Configuration file for `nox`."""

import tempfile
from typing import Any

import nox
from nox.sessions import Session

locations = "src", "tests", "./noxfile.py"
nox.options.sessions = "lint", "mypy", "tests"


def install_with_constraints(session: Session, *args: str, **kwargs: Any) -> None:
    """
    Install packages constrained by Poetry's lock file.

    This function is a wrapper for nox.sessions.Session.install. It invokes pip to
    install packages inside of the session's virtualenv.
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


@nox.session(python="3.10.6")
def black(session: Session) -> None:
    """Run black code formatter."""
    args = session.posargs or locations
    install_with_constraints(session, "black")
    session.run("black", *args)


@nox.session(python="3.10.6")
def lint(session: Session) -> None:
    """Lint using flake8."""
    args = session.posargs or locations
    install_with_constraints(
        session,
        "flake8",
        "flake8-annotations",
        "flake8-bandit",
        "flake8-black",
        "flake8-bugbear",
        "flake8-docstrings",
        "flake8-isort",
    )
    session.run("flake8", *args)


@nox.session(python=["3.11", "3.10.6", "3.9", "3.8"])
def mypy(session: Session) -> None:
    """Type-check using mypy."""
    args = session.posargs or locations
    install_with_constraints(session, "mypy")
    session.run("mypy", *args)


@nox.session(python=["3.10.6", "3.9", "3.8"])
def tests(session: Session) -> None:
    """Run the test suite using pytest."""
    args = session.posargs or ["--cov"]
    session.run("poetry", "install", "--without", "docs,dev", external=True)
    install_with_constraints(session, "coverage[toml]", "pytest", "pytest-cov")
    session.run("pytest", *args)

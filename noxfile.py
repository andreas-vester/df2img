"""Nox sessions."""

import os

import nox
from nox.sessions import Session

os.environ.update({"PDM_IGNORE_SAVED_PYTHON": "1"})
nox.options.sessions = [
    "pre-commit",
    "tests",
]
PYTHON_VERSIONS = ["3.9", "3.10", "3.11", "3.12"]


@nox.session(name="pre-commit", python=PYTHON_VERSIONS)
def precommit(session: Session) -> None:
    """Lint using pre-commit."""
    args = session.posargs or [
        "run",
        "--all-files",
        "--hook-stage=manual",
    ]

    session.run_always("pdm", "install", "-G", "lint", external=True)
    session.run("pre-commit", "install")
    session.run("pre-commit", *args)


@nox.session(name="tests", python=PYTHON_VERSIONS)
def tests(session: Session) -> None:
    """Run the test suite."""
    args = session.posargs or ["--cov"]

    session.run_always("pdm", "install", "-G", "test", external=True)
    session.run("pytest", *args)

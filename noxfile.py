import nox


@nox.session(python=["3.10", "3.9", "3,8"])
def tests(session):
    args = session.posargs or ["--cov"]
    session.run("poetry", "install", "-E", "docs", external=True)
    session.run("pytest", *args)

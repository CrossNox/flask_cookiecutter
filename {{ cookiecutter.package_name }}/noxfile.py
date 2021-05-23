"""Entrypoint for nox."""

import nox


@nox.session(reuse_venv=True)
def tests(session):
    """Run all tests."""
    session.install("poetry")
    session.run("poetry", "install", "-E", "testing")

    cmd = ["poetry", "run", "pytest", "-n", "auto"]

    if session.posargs:
        cmd.extend(session.posargs)

    session.run(*cmd)


@nox.session(reuse_venv=True)
def cop(session):
    """Run all pre-commit hooks."""
    session.install("poetry")
    session.run("poetry", "install")

    session.run("poetry", "run", "pre-commit", "install")
    session.run(
        "poetry", "run", "pre-commit", "run", "--show-diff-on-failure", "--all-files"
    )


@nox.session(reuse_venv=True)
def bandit(session):
    """Run all pre-commit hooks."""
    session.install("poetry")
    session.run("poetry", "install")

    session.run("poetry", "run", "bandit", "-r", "{{cookiecutter.package_name}}/", "-ll", "-c", "bandit.yaml")


@nox.session(reuse_venv=True)
def pyreverse(session):
    """Create class diagrams."""
    session.install("poetry")

    # TODO: create smaller diagrams with portions of the project.
    session.run("poetry", "run", "pyreverse", "{{cookiecutter.package_name}}", "-o", "png")

    session.run(
        "mv", "packages.png", "docs/images/packages_dependencies.png", external=True
    )
    session.run("mv", "classes.png", "docs/images/project_classes.png", external=True)

# Flask App Cookiecutter

This is a cookiecutter for flask app/microservices.

# Dependencies

The only dependency required to use this template is [cookiecutter](https://cookiecutter.readthedocs.io/en/1.7.2/). The recommended method to install it is through [pipx](https://pipxproject.github.io/pipx/installation/).

A more traditional approach is to install it through `pip`:

```bash
pip3 install --user -r requirements.txt
```

# Usage

To generate a new project:
```
$ cookiecutter https://github.com/7552-2020C2-grupo5/flask_cookiecutter
```

Or you can point to your local clone of the repo.

# Components

## `flask-restx`
[flask-restx](https://flask-restx.readthedocs.io/en/latest/) defines themselves as:

> an extension for Flask that adds support for quickly building REST APIs

It provides several useful components, such as [resourceful routing](https://flask-restx.readthedocs.io/en/latest/quickstart.html#resourceful-routing), [argument parsing](https://flask-restx.readthedocs.io/en/latest/quickstart.html#argument-parsing), [response marshalling](https://flask-restx.readthedocs.io/en/latest/marshalling.html), [error handling](https://flask-restx.readthedocs.io/en/latest/errors.html), [swagger documentation](https://flask-restx.readthedocs.io/en/latest/swagger.html) and more.

## `flask-migrate`
[flask-migrate](https://flask-migrate.readthedocs.io/en/latest/) defines themselves as:

> an extension that handles SQLAlchemy database migrations for Flask applications using Alembic

Which allows for incremental database operations over the schema.

## `flask-sqlalchemy`
[flask-sqlalchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) is a flask extensin adding `SQLAlchemy` support for flask apps.

## `pre-commit`
[pre-commit](https://pre-commit.com) is:

> A framework for managing and maintaining multi-language pre-commit hooks.

You can set several hooks to be run on `pre-commit` or `push` events, say linters for `pre-commit` and tests on `push` stage. This allows for easier development cycles and helps improve code quality.

## `nox`
[nox](https://nox.thea.codes/en/stable/) is a tool alike [tox](https://tox.readthedocs.io/en/latest/). The main difference is that `nox` uses a python file for configuration. We will be using it to bootstrap dependencies for linting and testing, such that our environment is as similar to CI/CD as possible and that dependencies are isolated.

## `python-poetry`
[poetry](https://python-poetry.org) is `python packaging and dependency management made easy`.

## GitHub Actions
Let's go through the hassle of setting linting and testing jobs on github once and reuse it. 

## Docker
Minimal docker/podman config with postgres.


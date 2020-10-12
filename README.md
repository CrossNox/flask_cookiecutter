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

## Init repo
```bash
git init
```

## Install pre-commmit hooks
```bash
pre-commit install
pre-commit install -t pre-push
```

## Add some model
In `models.py`:

```python
class TodoSimple(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reminder = db.Column(db.String)
```

## Add initial migration
```bash
poetry run package_name/manage.py db migrate -m "add todo model"
```

## Add some resources!
In `api.py`:

```python

todo_model = api.model('ToDo', {
    "reminder": fields.String
})

@api.route('/todo/<int:todo_id>')
class TodoSimpleResource(Resource):
    @api.marshall_with(todo_model, envelope='resource')
    def get(self, todo_id):
        todo = TodoSimple.query.filter(TodoSimple.id == todo_id).first()
        return todo

    @api.marshall_with(todo_model, envelope='resource')
    def put(self, todo_id):
        parser = reqparse.RequestParser()
        parser.add_argument('reminder', type=str, help='reminder description')
        args = parser.parse_args(strict=True)
        reminder = args.reminder
        new_todo = TodoSimple(id=todo_id, reminder=reminder)
        db.session.add(new_todo)
        db.session.commit()
        return new_todo
```

## Start docker
```bash
cd docker
docker-compose build
docker-compose up
```

# Components

## `flask-restx`
[flask-restx](https://flask-restx.readthedocs.io/en/latest/) defines themselves as:

> an extension for Flask that adds support for quickly building REST APIs

It provides several useful components, such as [resourceful routing](https://flask-restx.readthedocs.io/en/latest/quickstart.html#resourceful-routing), [argument parsing](https://flask-restx.readthedocs.io/en/latest/quickstart.html#argument-parsing), [response marshalling](https://flask-restx.readthedocs.io/en/latest/marshalling.html), [error handling](https://flask-restx.readthedocs.io/en/latest/errors.html), [swagger documentation](https://flask-restx.readthedocs.io/en/latest/swagger.html) and more.

[Here](https://flask-restx.readthedocs.io/en/latest/quickstart.html) is a quickstart guide on `flask-restx`.

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



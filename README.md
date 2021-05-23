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
Read the README on the generated repo!

## Init repo
```bash
git init
```

## Install the package
```bash
poetry install
```

## Install pre-commmit hooks
```bash
poetry run pre-commit install
poetry run pre-commit install -t pre-push
```

## Add some model
In `models.py`:

```python
class TodoSimple(db.Model):  # type:ignore
    id = db.Column(db.Integer, primary_key=True)
    reminder = db.Column(db.String)
```

## Add initial migration
```bash
poetry run python package_name/manage.py db migrate -m "add todo model"
```

## Add some resources!
Create file `namespaces/todo/__init__/.py` with the following content:
```python
from .namespace import ns
```

Create `namespaces/todo/namespace.py` with the following content:

```python
"""ToDo namespace module."""

from flask_restx import Namespace, Resource

from package_name.models import TodoSimple, db

from .models import todo_model

ns = Namespace("ToDo", description="ToDo operations")

ns.models[todo_model.name] = todo_model


@ns.route('/todo')
class TodoListResource(Resource):
    @ns.doc('list_todo')
    @ns.marshal_list_with(todo_model)
    def get(self):
        """Get all ToDos."""
        return TodoSimple.query.all()

    @ns.doc('create_todo')
    @ns.expect(todo_model)
    @ns.marshal_with(todo_model, envelope='resource')
    def post(self):
        """Create a new ToDo."""
        new_todo = TodoSimple(**ns.payload)
        db.session.add(new_todo)
        db.session.commit()
        return new_todo


@ns.route('/todo/<int:todo_id>')
@ns.param('todo_id', 'The ToDo unique identifier')
@ns.response(404, 'ToDo not found')
class TodoSimpleResource(Resource):
    @ns.doc('get_todo')
    @ns.marshal_with(todo_model)
    def get(self, todo_id):
        """Get a ToDo by id."""
        todo = TodoSimple.query.filter(TodoSimple.id == todo_id).first()
        return todo
```

Create `namespaces/todo/models.py` with the following:

```python
"""ToDo namespace models module."""

from flask_restx import Model, fields

todo_model = Model(
    'ToDo',
    {
        "id": fields.String(
            readonly=True, description="The unique identifier of the task"
        ),
        "reminder": fields.String(
            required=True, description="What you want to remember."
        ),
    },
)
```

Add the following line in ```namespaces/__init__.py```:

```python
from .todo import ns as todo_namespace
```

And lastly, in ```api.py```:

```python
from package_name.namespaces import todo_namespace
```

And add the namespace to the api:
```python
api.add_namespace(default_namespace, path='/todo')
```

## Tests
I'll leave this to you :P

## Start docker
```bash
cd docker-compose
docker-compose build
docker-compose up
```

## Try it out!
If you've followed this example, you can test it with

```python
import requests as r
print(r.post('http://localhost:5000/v1/todo', json={'reminder': 'Remember the eggs'}).json())
print(r.get('http://localhost:5000/v1/todo/1').json())
print(r.get('http://localhost:5000/v1/todo').json())
```

## Swagger
You should be able to visit the swagger docs on `http://127.0.0.1:5000`.

## Heroku
Check the heroku section on the generated README.

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

## [Optional] Datadog monitoring on heroku
Heroku dockerfile will use datadog.

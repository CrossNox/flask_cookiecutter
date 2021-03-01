import os
import shutil


def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)


use_datadog = "{{cookiecutter.use_datadog}}" == "yes"

if not use_datadog:
    remove("heroku-Dockerfile")
    remove("heroku")

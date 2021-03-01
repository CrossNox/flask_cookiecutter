#!/bin/bash

datadog-agent run > /dev/null &
/opt/datadog-agent/embedded/bin/trace-agent --config=/etc/datadog-agent/datadog.yaml > /dev/null &
/opt/datadog-agent/embedded/bin/process-agent --config=/etc/datadog-agent/datadog.yaml > /dev/null &
poetry run gunicorn --log-level=debug --bind 0.0.0.0:$PORT "{{cookiecutter.package_name}}.app:create_app()"

import json
from http import HTTPStatus

from api.utils import load_schema
from flask import Flask, Response, request
from jsonschema import validate
from jsonschema.exceptions import SchemaError, ValidationError

app = Flask(__name__)


@app.route("/")
def base():
    """Root server route to ensure proper startup.
    Returns:
        str: Startup message.
    """
    return "<p>Config validation server running.</p>"


@app.post("/validate")
def validate_config():
    """Server route to validate a user-supplied JSON configuration.
    The route accepts a POST request with the configuration in the
    request body. Then, it conducts logic to:
    1. Load the schema (locally or from Azure storage)
    2. Validate the configuration against the schema,
    3. Return the configuration if it's valid, otherwise raise an HTTPError

    Returns:
        flask.Response: response object with valid JSON or error message.
    """

    # Load schema; locally for now. Return early if loading fails
    try:
        schema = load_schema(local=True)
    except (json.decoder.JSONDecodeError, FileNotFoundError) as err:
        return Response(response=str(err), status=HTTPStatus.BAD_REQUEST)

    # Validate configuration in request body against schema
    request_json = request.get_json(silent=False)
    try:
        validate(request_json, schema)
    except (ValidationError, SchemaError) as err:
        return Response(response=str(err), status=HTTPStatus.BAD_REQUEST)

    return request_json, HTTPStatus.OK


if __name__ == "__main__":
    app.run(debug=True)

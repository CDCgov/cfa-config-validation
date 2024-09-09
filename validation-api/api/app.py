import json 
import os
from flask import Flask, Response
from http import HTTPStatus
from api.utils import CONSTANTS

app = Flask(__name__)

@app.route("/")
def base():
    """Root server route to ensure proper startup.
    Returns:
        str: Startup message.
    """
    return "<p>Config validation server running.</p>"

@app.post("/validate")
def validate():
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
        schema_path = os.path.join(CONSTANTS.get("base_dir", ""), CONSTANTS.get("local_schema_path", ""))
        with open(schema_path) as fp:
            schema = json.load(fp)
    except (json.decoder.JSONDecodeError, FileNotFoundError) as err:
        return Response(response=str(err), status=HTTPStatus.BAD_REQUEST)

    
    return schema


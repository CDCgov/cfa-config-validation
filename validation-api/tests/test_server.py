import json
import os
from pathlib import Path

from api.app import app

client = app.test_client()
data_dir = Path(__file__).parent / "data"


def test_base_route():
    """Test base route returns startup message."""
    response = client.get("/")
    assert b"<p>Config validation server running.</p>" in response.data


def test_valid_configuration():
    """Test that a valid config returns a 200 status."""
    config_path = os.path.join(data_dir, "valid_config.json")
    with open(config_path) as fp:
        config = json.load(fp)

    response = client.post("/validate?local=True", json=config)
    assert response.status == "200 OK"
    assert json.loads(response.data) == config


def test_invalid_configuration():
    """Test that an invalid config throws a 400 error."""
    config_path = os.path.join(data_dir, "invalid_config.json")
    with open(config_path) as fp:
        config = json.load(fp)

    response = client.post("/validate?local=True", json=config)
    assert response.status == "400 BAD REQUEST"
    assert (
        "Additional properties are not allowed ('reference_date', 'report_date' were unexpected)"
        in response.data.decode()
    )

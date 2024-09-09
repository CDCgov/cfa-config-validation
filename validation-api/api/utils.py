import os
import json

CONSTANTS = {
     "base_dir": os.path.abspath(os.path.dirname(__file__)),
     "local_schema_path": "local_schema.json"
}

def load_schema(local=True):
    """Load schema to compare configuration against.

    This function loads a schema to compare the user-
    provided configuration object against. Currently,
    it pulls from a local file stored in data/, but
    future implementations will pull from Azure blob
    storage so that it can be more easily maintained.

    Args:
        local (bool): Determines whether to use local
        schema file or pull latest from Azure (currently
        not implemented).

    Returns:
        dict: Loaded schema dictionary.

    Raises:
        json.decoder.JSONDecodeError: If the schema JSON is invalid.
    """ 
    schema_path = os.path.join(CONSTANTS.get("base_dir", ""), CONSTANTS.get("local_schema_path", ""))
    with open(schema_path) as fp:
        schema = json.load(fp)
    return schema
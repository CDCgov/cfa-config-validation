import json
import os

from azure_utils.auth import obtain_sp_credential
from azure_utils.storage import obtain_schema_from_blob_storage

CONSTANTS = {
    "base_dir": os.path.abspath(os.path.dirname(__file__)),
    "local_schema_path": "local_schema.json",
    "azure_storage_account_url": "https://cfaazurebatchprd.blob.core.windows.net/",
    "azure_container_name": "cfa-config-validation",
    "azure_schema_filename": "schema.json",
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

    if local:
        # Use local schema instead of pulling from Azure
        schema_path = os.path.join(
            CONSTANTS.get("base_dir", ""),
            CONSTANTS.get("local_schema_path", ""),
        )
        with open(schema_path) as fp:
            schema = json.load(fp)
        return schema

    sp_credential = obtain_sp_credential()
    schema = obtain_schema_from_blob_storage(
        sp_credential=sp_credential,
        account_url=CONSTANTS.get("azure_storage_account_url", ""),
        container_name=CONSTANTS.get("azure_container_name", ""),
        blob_name=CONSTANTS.get("azure_schema_filename", ""),
    )
    return schema

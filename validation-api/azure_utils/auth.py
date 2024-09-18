import os
import toml
from azure.identity import DefaultAzureCredential


def read_config(config_path):
    """Read local Azure configuration file.
    Args:
        config_path (str): Filepath of configuration file.
    Returns:
        dict: Configuration object.
    """
    config = toml.load(config_path)
    return config


def obtain_sp_credential():
    """Obtains service principal credentials from Azure.
    Returns:
        Instance of DefaultAzureCredential.
    """

    # Since this will be run from a Docker container,
    # we only use the SP Credential to authenticate.

    # Check that env variables are set
    tenant_id = os.environ.get("AZURE_TENANT_ID", "")
    application_id = os.environ.get("AZURE_CLIENT_ID", "")
    client_secret = os.environ.get("AZURE_CLIENT_SECRET", "")
    if "" in [tenant_id, client_secret, application_id]:
        error_message = "Azure secrets not found in environment. Ensure secrets are configured properly."
        raise ValueError(error_message)

    # The DefaultAzureCredential reads from the environment directly
    sp_credential = DefaultAzureCredential()

    return sp_credential

import os

import toml
from azure.identity import ClientSecretCredential


def read_config(config_path):
    """Read local Azure configuration file.
    Args:
        config_path (str): Filepath of configuration file.
    Returns:
        dict: Configuration object.
    """
    config = toml.load(config_path)
    return config


def obtain_credential(config, credential_type="default"):
    """Obtains client credentials from Azure KeyVault.
    Args:
        config (dict): Dictionary of configuration values.
    Returns:
        Instance of ClientSecretCredential.
    """

    # Since this will be run from a Docker container,
    # we only use the SP Credential to Authenticate.

    # Pull values from injected environment variables
    tenant_id = os.environ.get("TENANT_ID", "")
    application_id = os.environ.get("APPLICATION_ID", "")
    client_secret = os.environ.get("SP_SECRET", "")
    if "" in [tenant_id, client_secret, application_id]:
        error_message = "Azure secrets not found in environment. Ensure secrets are configured properly."
        raise ValueError(error_message)

    sp_credential = ClientSecretCredential(
        tenant_id=tenant_id,
        client_id=application_id,
        client_secret=client_secret,
    )

    return sp_credential, client_secret

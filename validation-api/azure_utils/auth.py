import toml
from azure.identity import (
    AzureCliCredential,
    ChainedTokenCredential,
    ClientSecretCredential,
    DefaultAzureCredential,
    EnvironmentCredential
)

from azure.keyvault.secrets import SecretClient

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

    

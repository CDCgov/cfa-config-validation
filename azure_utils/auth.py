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
    Raises:
        LookupError if credential not found.
    """

    # The DefaultAzureCredential reads from the environment directly
    # if running locally. The deployed version uses Managed Identity
    sp_credential = DefaultAzureCredential()

    return sp_credential

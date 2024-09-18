import json
from azure.storage.blob import BlobServiceClient


def obtain_schema_from_blob_storage(
    sp_credential=None, account_url="", container_name="", blob_name=""
):
    """Function to pull the modeling
    pipeline schema from blob storage.
    Args:
        sp_credential (DefaultAzureCredential): Service principal credential object
        for use in authenticating with Storage API.
    Returns:
        dict: Schema dictionary.
    Raises:
        json.decoder.JSONDecodeError: If the schema JSON is invalid.
        ValueError: If sp_credential is invalid or BlobServiceClient
        fails to instantiate.
    """

    if not sp_credential:
        raise ValueError("Service principal credential not provided.")

    # Instantiate BlobStorageClient
    blob_service_client = BlobServiceClient(
        account_url, credential=sp_credential
    )

    # Retrieve blob from client
    blob_client = blob_service_client.get_blob_client(
        container=container_name, blob=blob_name
    )

    # encoding param is necessary for readall() to return str, otherwise it returns bytes
    downloader = blob_client.download_blob(max_concurrency=1, encoding="UTF-8")
    blob_text = downloader.readall()
    schema = json.loads(blob_text)
    return schema

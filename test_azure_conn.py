import os
from dotenv import load_dotenv
from azure.storage.blob import BlobServiceClient

load_dotenv(r"C:\Users\User\.gemini\antigravity\scratch\consultorseosp\.env")
conn_str = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
print("Conn str found:", bool(conn_str))

try:
    client = BlobServiceClient.from_connection_string(conn_str)
    props = client.get_account_information()
    print("Account info:", props)
    container_client = client.get_container_client("$web")
    print("Container exists:", container_client.exists())
    
    # Test uploading a small test string
    test_blob = container_client.get_blob_client("test_ping.txt")
    test_blob.upload_blob(b"ok", overwrite=True)
    print("Upload test_ping.txt succeeded!")
    test_blob.delete_blob()
    print("Delete test_ping.txt succeeded!")
except Exception as e:
    print("Error:", e)

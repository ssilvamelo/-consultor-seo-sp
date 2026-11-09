import os
from dotenv import load_dotenv
from azure.storage.blob import BlobServiceClient

load_dotenv(r"C:\Users\User\.gemini\antigravity\scratch\consultorseosp\.env")
conn_str = os.getenv("AZURE_STORAGE_CONNECTION_STRING")

client = BlobServiceClient.from_connection_string(conn_str)
containers = [c.name for c in client.list_containers()]
print("Containers:", containers)

container = client.get_container_client("$web")
blobs = [b.name for b in container.list_blobs()]
print(f"Total blobs in $web: {len(blobs)}")
print("Sample blobs:", blobs[:10])

import os
from dotenv import load_dotenv
from azure.storage.blob import BlobServiceClient

load_dotenv(r"C:\Users\User\.gemini\antigravity\scratch\consultorseosp\.env")
conn_str = os.getenv("AZURE_STORAGE_CONNECTION_STRING")

client = BlobServiceClient.from_connection_string(conn_str)
props = client.get_service_properties()
print("Static website enabled:", props.get('static_website'))

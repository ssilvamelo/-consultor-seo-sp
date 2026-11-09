import os
import re
from dotenv import load_dotenv
from azure.storage.blob import BlobServiceClient, ContentSettings

load_dotenv(r"C:\Users\User\.gemini\antigravity\scratch\consultorseosp\.env")
conn_str = os.getenv("AZURE_STORAGE_CONNECTION_STRING")

client = BlobServiceClient.from_connection_string(conn_str)
container_client = client.get_container_client("$web")

# 1. Upload the fixed image
img_path = r"C:\Users\User\.gemini\antigravity\scratch\consultorseosp\assets\img\consultor-seo-sao-paulo-especialista-inteligencia-artificial.webp"
img_blob = "assets/img/consultor-seo-sao-paulo-especialista-inteligencia-artificial.webp"
with open(img_path, "rb") as f:
    container_client.get_blob_client(img_blob).upload_blob(
        f,
        overwrite=True,
        content_settings=ContentSettings(content_type="image/webp", cache_control="public, max-age=31536000, immutable")
    )
print("Uploaded image to Azure!")

# 2. Upload index.html
index_path = r"C:\Users\User\.gemini\antigravity\scratch\consultorseosp\index.html"
with open(index_path, "r", encoding="utf-8") as f:
    html_data = f.read()

# Azure canonical
html_data = re.sub(
    r'<link\s+rel=["\']canonical["\']\s+href=["\'][^"\']+["\']\s*/?>',
    '<link rel="canonical" href="https://consultorseohub.z15.web.core.windows.net/">',
    html_data
)
container_client.get_blob_client("index.html").upload_blob(
    html_data.encode("utf-8"),
    overwrite=True,
    content_settings=ContentSettings(content_type="text/html; charset=utf-8", cache_control="public, max-age=3600, must-revalidate")
)
print("Uploaded index.html to Azure!")

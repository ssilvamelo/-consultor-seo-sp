"""
Deploy Automático para Microsoft Azure Blob Storage ($web)
Consultor SEO SP | Brand Hub na Nuvem da Microsoft
"""

import os
import sys
import re
import mimetypes
from dotenv import dotenv_values
from azure.storage.blob import BlobServiceClient, ContentSettings

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ENV_FILE = os.path.join(BASE_DIR, ".env")
CONTAINER_NAME = "$web"

VALID_EXTS = {
    ".html", ".css", ".js", ".webp", ".png", ".jpg", ".jpeg", 
    ".ico", ".txt", ".xml", ".json", ".svg"
}

SKIP_FILES = {
    "build_agent_surface.py", "deploy_s3.py", "generate_cities.py",
    "deploy_hostinger.py", "deploy_azure.py", "inject_gtag.py",
    "generate_graphics.py", "build_blog_and_compliance.py",
    "update_site_seo_master.py", "dossie.md", ".env", ".env.example"
}

INCLUDE_DIRS = {"agent-md", "cidades", "blog", "css", "js", "assets"}
# Arquivos de trabalho NUNCA vao para producao (prefixos)
WORK_PREFIXES = ("webvip_", "relatorio_", "blog_data", "seo_spider", "optimize_", "connect_all",
                 "build_", "normalize_", "dossie", "readme", "audit", "deploy_", "generate_",
                 "inject_", "update_", "fix_", "memoria_", "bios_", "skill", "links do site")



def load_config():
    if not os.path.exists(ENV_FILE):
        print(f"[!] Arquivo .env não encontrado em: {ENV_FILE}")
        sys.exit(1)

    config = dotenv_values(ENV_FILE)
    conn_str = config.get("AZURE_STORAGE_CONNECTION_STRING", "").strip()

    if not conn_str or "DefaultEndpointsProtocol" not in conn_str:
        print("[!] Chave AZURE_STORAGE_CONNECTION_STRING ausente ou inválida no seu arquivo .env.")
        print('    Abra o .env e adicione a linha:')
        print('    AZURE_STORAGE_CONNECTION_STRING="DefaultEndpointsProtocol=https;AccountName=consultorseohub;..."')
        sys.exit(1)

    return conn_str


def get_content_settings(file_name, full_path):
    if file_name.endswith(".html"):
        content_type = "text/html; charset=utf-8"
        cache_control = "public, max-age=3600, must-revalidate"
    elif file_name.endswith(".md"):
        content_type = "text/markdown; charset=utf-8"
        cache_control = "public, max-age=3600, must-revalidate"
    elif file_name.endswith(".txt"):
        content_type = "text/plain; charset=utf-8"
        cache_control = "public, max-age=3600, must-revalidate"
    elif file_name.endswith(".xml"):
        content_type = "application/xml; charset=utf-8"
        cache_control = "public, max-age=3600, must-revalidate"
    elif file_name.endswith(".css"):
        content_type = "text/css; charset=utf-8"
        cache_control = "public, max-age=2592000"
    elif file_name.endswith(".js"):
        content_type = "application/javascript; charset=utf-8"
        cache_control = "public, max-age=2592000"
    elif file_name.endswith(".webp"):
        content_type = "image/webp"
        cache_control = "public, max-age=31536000, immutable"
    else:
        content_type, _ = mimetypes.guess_type(full_path)
        if not content_type:
            content_type = "application/octet-stream"
        cache_control = "public, max-age=31536000, immutable"

    return ContentSettings(content_type=content_type, cache_control=cache_control)


def run_deploy():
    conn_str = load_config()

    print("[*] Conectando ao Microsoft Azure Blob Storage (Consultor SEO SP)...")
    try:
        blob_service_client = BlobServiceClient.from_connection_string(conn_str)
        container_client = blob_service_client.get_container_client(CONTAINER_NAME)
        account_name = blob_service_client.account_name
        print(f"  [+] Conexão autenticada com sucesso na conta: {account_name}")
    except Exception as e:
        print(f"  [!] Erro de autenticação com a Azure: {e}")
        sys.exit(1)

    # Coletar arquivos para upload
    files_to_deploy = {}

    for item in os.listdir(BASE_DIR):
        full_path = os.path.join(BASE_DIR, item)
        if item in SKIP_FILES or item.lower().startswith(WORK_PREFIXES) or item.endswith((".py", ".env", ".log", ".bak", ".zip", ".xlsx", ".pdf", ".md")):
            continue

        if os.path.isfile(full_path):
            ext = os.path.splitext(item)[1].lower()
            if ext == ".txt" and item not in {"robots.txt", "llms.txt", "llms-full.txt", "tiktok-developers-site-verification.txt", "c03b8e216451475d9b6a1a3eb6633038.txt"}:
                continue
            if ext in VALID_EXTS or item == ".htaccess":
                files_to_deploy[item] = full_path

    for inc_dir in INCLUDE_DIRS:
        dir_path = os.path.join(BASE_DIR, inc_dir)
        if os.path.exists(dir_path):
            for root, _, files in os.walk(dir_path):
                for f in files:
                    if f.endswith((".py", ".bak", ".tmp", ".log")):
                        continue
                    full_path = os.path.join(root, f)
                    rel_path = os.path.relpath(full_path, BASE_DIR).replace("\\", "/")
                    files_to_deploy[rel_path] = full_path

    total_files = len(files_to_deploy)
    print(f"[*] Total de {total_files} arquivos elegíveis para upload no container {CONTAINER_NAME}.")

    print("\n" + "=" * 60)
    print(f" SINCRONIZANDO COM MICROSOFT AZURE ({account_name}/$web)")
    print("=" * 60)

    uploaded = 0
    total_bytes = 0

    for i, (blob_name, local_path) in enumerate(files_to_deploy.items(), 1):
        file_size = os.path.getsize(local_path)
        content_settings = get_content_settings(blob_name, local_path)

        blob_client = container_client.get_blob_client(blob_name)

        if blob_name.endswith(".html"):
            with open(local_path, "r", encoding="utf-8") as f:
                html_data = f.read()
            if blob_name == "index.html":
                # Azure Brand Hub self-canonical
                html_data = re.sub(
                    r'<link\s+rel=["\']canonical["\']\s+href=["\'][^"\']+["\']\s*/?>',
                    f'<link rel="canonical" href="https://{account_name}.z15.web.core.windows.net/">',
                    html_data
                )
            else:
                # Forçar Canonical Cross-Domain de volta ao Money Site na Hostinger
                canonical_target = f"https://consultorseosp.com.br/{blob_name}"
                html_data = re.sub(
                    r'<link\s+rel=["\']canonical["\']\s+href=["\'][^"\']+["\']\s*/?>',
                    f'<link rel="canonical" href="{canonical_target}">',
                    html_data
                )
            raw_bytes = html_data.encode("utf-8")
            blob_client.upload_blob(raw_bytes, overwrite=True, content_settings=content_settings)
        else:
            with open(local_path, "rb") as data:
                blob_client.upload_blob(data, overwrite=True, content_settings=content_settings)

        uploaded += 1
        total_bytes += file_size
        pct = (i / total_files) * 100
        print(f"  [+] [{i}/{total_files} | {pct:.1f}%] Sincronizado: {blob_name} ({file_size/1024:.1f} KB)")

    print("\n" + "=" * 60)
    print(" [SUCESSO] DEPLOY CONCLUÍDO NA MICROSOFT AZURE!")
    print(f"  * Arquivos sincronizados: {uploaded}")
    print(f"  * Total transferido: {total_bytes / (1024*1024):.2f} MB")
    print(f"  * URL Pública Azure: https://{account_name}.z15.web.core.windows.net/")
    print("=" * 60)


if __name__ == "__main__":
    run_deploy()

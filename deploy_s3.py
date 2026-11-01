import os
import mimetypes
import boto3
from dotenv import dotenv_values

print("[*] Iniciando Deploy e Sincronizacao de consultorseosp no AWS S3...")

ENV_PATH = r"C:\Users\User\.gemini\config\skills\seo-entity-agency-architect\scripts\.env"
env = dotenv_values(ENV_PATH)

s3 = boto3.client(
    "s3",
    aws_access_key_id=env.get("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=env.get("AWS_SECRET_ACCESS_KEY"),
    region_name="sa-east-1"
)

BUCKET = "consultorseosp-hub"
BASE_DIR = r"C:\Users\User\.gemini\antigravity\scratch\consultorseosp"
# Arquivos de trabalho NUNCA vao para producao (prefixos)
WORK_PREFIXES = ("webvip_", "relatorio_", "blog_data", "seo_spider", "optimize_", "connect_all",
                 "build_", "normalize_", "dossie", "readme", "audit", "deploy_", "generate_",
                 "inject_", "update_", "fix_", "memoria_", "bios_", "skill", "links do site")


# 1. Configurar Website Hosting no S3 com 404.html customizado
try:
    print("[*] Configurando Website Hosting com ErrorDocument='404.html'...")
    s3.put_bucket_website(
        Bucket=BUCKET,
        WebsiteConfiguration={
            "IndexDocument": {"Suffix": "index.html"},
            "ErrorDocument": {"Key": "404.html"}
        }
    )
    print("  [+] Website configuration atualizada com sucesso no S3!")
except Exception as e:
    print(f"  [!] Aviso na configuracao de website: {e}")

# 2. Upload de todos os arquivos com ContentType e CacheControl cirurgicos
uploaded = 0
skipped = 0

for root, dirs, files in os.walk(BASE_DIR):
    # Ignorar diretorios de auditoria, pycache e git
    rel_root = os.path.relpath(root, BASE_DIR)
    if any(x in rel_root for x in ["audit", "__pycache__", ".git"]):
        continue

    for file in files:
        # Seguranca: nunca enviar scripts python locais ou backups
        if (file.endswith((".py", ".pyc", ".env", ".log", ".bak")) or file.lower().startswith(WORK_PREFIXES)
            or (rel_root == "." and (file.endswith(".md") or (file.startswith(".") and file != ".htaccess")))):
            skipped += 1
            continue

        full_path = os.path.join(root, file)
        rel_path = os.path.relpath(full_path, BASE_DIR).replace("\\", "/")

        # Determinar Content-Type
        if file.endswith(".md"):
            content_type = "text/markdown; charset=utf-8"
            cache_control = "public, max-age=3600, must-revalidate"
        elif file.endswith(".txt"):
            content_type = "text/plain; charset=utf-8"
            cache_control = "public, max-age=3600, must-revalidate"
        elif file.endswith(".html"):
            content_type = "text/html; charset=utf-8"
            cache_control = "public, max-age=3600, must-revalidate"
        elif file.endswith(".xml"):
            content_type = "application/xml; charset=utf-8"
            cache_control = "public, max-age=3600, must-revalidate"
        elif file.endswith(".css"):
            content_type = "text/css; charset=utf-8"
            cache_control = "public, max-age=2592000"
        elif file.endswith(".js"):
            content_type = "application/javascript; charset=utf-8"
            cache_control = "public, max-age=2592000"
        elif file.endswith(".webp"):
            content_type = "image/webp"
            cache_control = "public, max-age=31536000, immutable"
        elif file.endswith((".png", ".jpg", ".jpeg", ".svg", ".ico")):
            content_type, _ = mimetypes.guess_type(full_path)
            cache_control = "public, max-age=31536000, immutable"
        else:
            content_type, _ = mimetypes.guess_type(full_path)
            if not content_type:
                content_type = "application/octet-stream"
            cache_control = "public, max-age=86400"

        extra_args = {
            "ContentType": content_type,
            "CacheControl": cache_control
        }

        s3.upload_file(full_path, BUCKET, rel_path, ExtraArgs=extra_args)
        uploaded += 1

print(f"[SUCESSO] Total de {uploaded} arquivos sincronizados com o bucket {BUCKET}!")
print(f"[*] {skipped} arquivos sensiveis/scripts ignorados por seguranca.")
print(f"[*] URL Publica do Brand Hub: http://{BUCKET}.s3-website-sa-east-1.amazonaws.com")

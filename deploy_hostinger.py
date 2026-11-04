"""
Deploy Automático Hostinger (FTP/FTPS Inteligente)
Consultor SEO SP | Sincronização Incremental para public_html com Auto-Reconexão
"""

import os
import sys
import time
import socket
import argparse
from ftplib import FTP, FTP_TLS, error_perm
from dotenv import dotenv_values

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ENV_FILE = os.path.join(BASE_DIR, ".env")

# Extensões e arquivos de produção permitidos
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
    host = config.get("HOSTINGER_FTP_HOST", "").replace("ftp://", "").replace("http://", "").strip("/")
    user = config.get("HOSTINGER_FTP_USER", "").strip()
    pwd = config.get("HOSTINGER_FTP_PASS", "").strip()

    if not host or not user or not pwd or "seu_usuario" in user:
        print("[!] Preencha as credenciais reais no arquivo .env antes de executar o deploy.")
        sys.exit(1)

    return {
        "host": host,
        "user": user,
        "pass": pwd,
        "port": int(config.get("HOSTINGER_FTP_PORT", 21)),
        "remote_dir": config.get("HOSTINGER_REMOTE_DIR", "public_html").strip("/"),
        "use_ftps": config.get("HOSTINGER_USE_FTPS", "true").lower() == "true"
    }


def connect_ftp(cfg):
    ftp = None
    if cfg["use_ftps"]:
        try:
            ftp = FTP_TLS()
            ftp.connect(cfg["host"], cfg["port"], timeout=30)
            ftp.login(cfg["user"], cfg["pass"])
            ftp.prot_p()
            ftp.voidcmd("TYPE I")
            return ftp
        except Exception as e:
            print(f"  [!] Aviso FTPS ({e}). Tentando FTP padrão...")

    ftp = FTP()
    ftp.connect(cfg["host"], cfg["port"], timeout=30)
    ftp.login(cfg["user"], cfg["pass"])
    ftp.voidcmd("TYPE I")
    return ftp


def get_files_to_deploy():
    files_map = {}

    # 1. Arquivos na raiz
    for item in os.listdir(BASE_DIR):
        full_path = os.path.join(BASE_DIR, item)
        if item in SKIP_FILES or item.lower().startswith(WORK_PREFIXES) or item.endswith((".py", ".env", ".log", ".bak", ".zip", ".xlsx", ".pdf")):
            continue
        if item.endswith(".md") and item != "agent.md":
            continue

        if os.path.isfile(full_path):
            ext = os.path.splitext(item)[1].lower()
            if ext == ".txt" and item not in {"robots.txt", "llms.txt", "llms-full.txt", "c03b8e216451475d9b6a1a3eb6633038.txt"} and not item.startswith("tiktok"):
                continue
            if ext in VALID_EXTS or item in {".htaccess", "agent.md"}:
                files_map[item] = full_path

    # 2. Pastas incluídas
    for inc_dir in INCLUDE_DIRS:
        dir_path = os.path.join(BASE_DIR, inc_dir)
        if os.path.exists(dir_path):
            for root, _, files in os.walk(dir_path):
                for f in files:
                    if f.endswith((".py", ".bak", ".tmp", ".log")):
                        continue
                    full_path = os.path.join(root, f)
                    rel_path = os.path.relpath(full_path, BASE_DIR).replace("\\", "/")
                    files_map[rel_path] = full_path

    return files_map


def ensure_remote_dir(ftp, remote_path):
    parts = remote_path.strip("/").split("/")
    current = ""
    for part in parts:
        current = f"{current}/{part}" if current else part
        try:
            ftp.cwd(f"/{current}")
        except Exception:
            try:
                ftp.mkd(f"/{current}")
                ftp.cwd(f"/{current}")
            except Exception:
                pass


def get_remote_file_size(ftp, remote_file_path):
    try:
        return ftp.size(remote_file_path)
    except Exception:
        return None


def run_deploy(force_upload=False, dry_run=False):
    cfg = load_config()
    files_to_deploy = get_files_to_deploy()
    total_files = len(files_to_deploy)

    print(f"[*] Encontrados {total_files} arquivos elegíveis para produção no Consultor SEO SP.")
    print(f"[*] Conectando a {cfg['host']}:{cfg['port']}...")
    ftp = connect_ftp(cfg)
    print("  [+] Conectado com sucesso à Hostinger!")

    initial_pwd = ftp.pwd()
    remote_base = cfg["remote_dir"]
    if initial_pwd.endswith(remote_base):
        base_prefix = initial_pwd
    else:
        base_prefix = f"/{remote_base}"
        ensure_remote_dir(ftp, remote_base)

    ftp.cwd(base_prefix)

    uploaded = 0
    skipped = 0
    bytes_transferred = 0

    print("\n" + "=" * 60)
    print(f" INICIANDO SINCRONIZAÇÃO COM HOSTINGER ({base_prefix}/)")
    if dry_run:
        print(" [MODO DRY-RUN ATIVO - NENHUM ARQUIVO SERÁ GRAVADO]")
    print("=" * 60)

    for i, (rel_path, local_abs) in enumerate(files_to_deploy.items(), 1):
        local_size = os.path.getsize(local_abs)
        remote_file_target = f"{base_prefix}/{rel_path}"

        # Tentativas com auto-reconexão se a Hostinger derrubar a conexão
        max_retries = 3
        for attempt in range(1, max_retries + 1):
            try:
                # Garante diretórios intermediários remotos se houver subpastas
                if "/" in rel_path:
                    parent_rel = os.path.dirname(rel_path)
                    parent_abs = f"{base_prefix}/{parent_rel}"
                    ensure_remote_dir(ftp, parent_abs)
                    ftp.cwd(base_prefix)

                # Sincronização inteligente: pula arquivos já enviados com o mesmo tamanho
                if not force_upload:
                    rem_size = get_remote_file_size(ftp, remote_file_target)
                    if rem_size is not None and rem_size == local_size:
                        skipped += 1
                        pct = (i / total_files) * 100
                        if skipped % 25 == 0 or i == total_files:
                            print(f"  [{i}/{total_files} | {pct:.1f}%] Sincronizados/Pulados: {skipped} arquivos sem alteração...")
                        break

                # Modo Dry-Run
                if dry_run:
                    print(f"  [DRY-RUN] Seria enviado: {rel_path} ({local_size/1024:.1f} KB)")
                    uploaded += 1
                    break

                # Upload real
                with open(local_abs, "rb") as f:
                    ftp.storbinary(f"STOR {remote_file_target}", f)

                uploaded += 1
                bytes_transferred += local_size
                pct = (i / total_files) * 100
                print(f"  [+] [{i}/{total_files} | {pct:.1f}%] Enviado: {rel_path} ({local_size/1024:.1f} KB)")
                break

            except (ConnectionResetError, BrokenPipeError, socket.error, EOFError, TimeoutError, error_perm) as e:
                print(f"  [!] Conexão instável no arquivo {rel_path} (Tentativa {attempt}/{max_retries}): {e}")
                time.sleep(2)
                try:
                    ftp.quit()
                except Exception:
                    pass
                print("  [*] Reconectando ao FTP da Hostinger...")
                ftp = connect_ftp(cfg)
                ftp.cwd(base_prefix)
                if attempt == max_retries:
                    print(f"  [ERRO FINAL] Falha ao enviar {rel_path} após {max_retries} tentativas.")

    try:
        ftp.quit()
    except Exception:
        pass

    print("\n" + "=" * 60)
    print(" [SUCESSO] DEPLOY CONCLUÍDO NA HOSTINGER!")
    print(f"  * Arquivos enviados/atualizados nesta rodada: {uploaded}")
    print(f"  * Arquivos já sincronizados (pulados): {skipped}")
    print(f"  * Total transferido: {bytes_transferred / (1024*1024):.2f} MB")
    print(f"  * URL de Produção: https://consultorseosp.com.br/")
    print("=" * 60)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Deploy Automático Hostinger FTP (Consultor SEO SP)")
    parser.add_argument("--force", action="store_true", help="Força upload de todos os arquivos")
    parser.add_argument("--dry-run", action="store_true", help="Simula o deploy")
    args = parser.parse_args()

    run_deploy(force_upload=args.force, dry_run=args.dry_run)

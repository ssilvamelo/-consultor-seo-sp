with open(r"C:\Users\User\.gemini\antigravity\scratch\consultorseosp\deploy_azure.py", "r", encoding="utf-8") as f:
    code = f.read()

target = '''        if blob_name.endswith(".html"):
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
                blob_client.upload_blob(data, overwrite=True, content_settings=content_settings)'''

replacement = '''        for attempt in range(1, 4):
            try:
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
                    blob_client.upload_blob(raw_bytes, overwrite=True, content_settings=content_settings, timeout=120)
                else:
                    with open(local_path, "rb") as data:
                        blob_client.upload_blob(data, overwrite=True, content_settings=content_settings, timeout=120)
                break
            except Exception as e:
                if attempt == 3:
                    raise e
                print(f"  [!] Timeout/Erro ao enviar {blob_name} (tentativa {attempt}/3): {e}. Tentando novamente em 3s...")
                import time
                time.sleep(3)'''

# Normalize line endings
norm_code = code.replace("\r\n", "\n")
norm_target = target.replace("\r\n", "\n")
norm_rep = replacement.replace("\r\n", "\n")

if norm_target in norm_code:
    norm_code = norm_code.replace(norm_target, norm_rep)
    with open(r"C:\Users\User\.gemini\antigravity\scratch\consultorseosp\deploy_azure.py", "w", encoding="utf-8") as f:
        f.write(norm_code)
    print("deploy_azure.py updated with retries!")
else:
    print("Target not found in deploy_azure.py!")

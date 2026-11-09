with open(r"C:\Users\User\.gemini\antigravity\scratch\consultorseosp\deploy_azure.py", "rb") as f:
    raw = f.read()

# Let's decode with errors ignore or latin1 to safely handle it
text = raw.decode("utf-8", errors="replace")
lines = text.splitlines(keepends=True)

# Find where `if blob_name.endswith(".html"):` is
idx_start = -1
for i, line in enumerate(lines):
    if 'if blob_name.endswith(".html"):' in line:
        idx_start = i
        break

if idx_start != -1:
    # Find the end of this if/else block
    idx_end = -1
    for j in range(idx_start, len(lines)):
        if 'uploaded += 1' in lines[j]:
            idx_end = j
            break

    print(f"Replacing lines {idx_start} to {idx_end}")

    new_block = """        for attempt in range(1, 4):
            try:
                if blob_name.endswith(".html"):
                    with open(local_path, "r", encoding="utf-8") as f:
                        html_data = f.read()
                    if blob_name == "index.html":
                        html_data = re.sub(
                            r'<link\\s+rel=["\\']canonical["\\']\\s+href=["\\'][^"\\']+["\\']\\s*/?>',
                            f'<link rel="canonical" href="https://{account_name}.z15.web.core.windows.net/">',
                            html_data
                        )
                    else:
                        canonical_target = f"https://consultorseosp.com.br/{blob_name}"
                        html_data = re.sub(
                            r'<link\\s+rel=["\\']canonical["\\']\\s+href=["\\'][^"\\']+["\\']\\s*/?>',
                            f'<link rel="canonical" href="{canonical_target}">',
                            html_data
                        )
                    raw_bytes = html_data.encode("utf-8")
                    blob_client.upload_blob(raw_bytes, overwrite=True, content_settings=content_settings, timeout=180)
                else:
                    with open(local_path, "rb") as data:
                        blob_client.upload_blob(data, overwrite=True, content_settings=content_settings, timeout=180)
                break
            except Exception as e:
                if attempt == 3:
                    raise e
                print(f"  [!] Retry {attempt}/3 no blob {blob_name}: {e}. Aguardando 3s...")
                import time
                time.sleep(3)
\n"""
    new_lines = lines[:idx_start] + [new_block] + lines[idx_end:]
    with open(r"C:\Users\User\.gemini\antigravity\scratch\consultorseosp\deploy_azure.py", "w", encoding="utf-8") as f:
        f.writelines(new_lines)
    print("deploy_azure.py patched successfully!")
else:
    print("Could not find start index")

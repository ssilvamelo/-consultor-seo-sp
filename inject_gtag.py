import os

base_dir = r"C:\Users\User\.gemini\antigravity\scratch\consultorseosp"
html_files = []
for root, dirs, files in os.walk(base_dir):
    if any(x in root for x in ["audit", "__pycache__", ".git"]):
        continue
    for f in files:
        if f.endswith(".html"):
            html_files.append(os.path.join(root, f))

gtag_snippet = """  <!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-XL7CQPKLP5"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());

    gtag('config', 'G-XL7CQPKLP5');
  </script>
"""

updated = 0
already_had = 0

for file_path in html_files:
    with open(file_path, "r", encoding="utf-8") as fl:
        content = fl.read()

    if "G-XL7CQPKLP5" in content:
        already_had += 1
        continue

    if "<head>" in content:
        new_content = content.replace("<head>", f"<head>\n{gtag_snippet}", 1)
        with open(file_path, "w", encoding="utf-8") as fl:
            fl.write(new_content)
        updated += 1

print(f"[+] Google tag G-XL7CQPKLP5 injetada em {updated} arquivos HTML do Consultor SEO SP!")
print(f"[*] {already_had} arquivos ja possuiam a tag.")

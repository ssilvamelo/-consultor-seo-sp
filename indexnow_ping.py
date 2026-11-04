import json
import urllib.request
import os

HOST = "consultorseosp.com.br"
KEY = "c03b8e216451475d9b6a1a3eb6633038"
KEY_FILE = f"{KEY}.txt"
BASE_DIR = r"C:\Users\User\.gemini\antigravity\scratch\consultorseosp"

with open(os.path.join(BASE_DIR, KEY_FILE), "w", encoding="utf-8") as f:
    f.write(KEY)

print(f"[+] Arquivo de chave IndexNow criado para Consultor SEO SP: {KEY_FILE}")

URLS = [
    f"https://{HOST}/",
    f"https://{HOST}/cidades/",
    f"https://{HOST}/blog/",
    f"https://{HOST}/sitemap-images.xml",
    f"https://{HOST}/agent-md/index.md"
]

payload = {
    "host": HOST,
    "key": KEY,
    "keyLocation": f"https://{HOST}/{KEY_FILE}",
    "urlList": URLS
}

req_data = json.dumps(payload).encode("utf-8")

req = urllib.request.Request(
    "https://api.indexnow.org/indexnow",
    data=req_data,
    headers={
        "Content-Type": "application/json; charset=utf-8",
        "User-Agent": "Consultor-SEO-SP-IndexNow-Agent/1.0"
    }
)

try:
    with urllib.request.urlopen(req, timeout=10) as resp:
        print(f"[+] IndexNow Ping enviado com sucesso! Status HTTP: {resp.status}")
except Exception as e:
    print(f"[!] Resposta IndexNow: {e}")

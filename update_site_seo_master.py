import os
import re
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import json

BASE_DIR = r"C:\Users\User\.gemini\antigravity\scratch\consultorseosp"
INDEX_PATH = os.path.join(BASE_DIR, "index.html")

print("[*] Iniciando atualizacao mestre de SEO, Metadados e Grafo Semantico...")

# 1. Atualizar index.html
with open(INDEX_PATH, "r", encoding="utf-8") as f:
    html = f.read()

# Injetar Favicon e OG Image no <head> se ainda não existirem
head_meta = """  <!-- Favicon & Social Share Cards -->
  <link rel="icon" href="/favicon.ico" type="image/x-icon">
  <link rel="apple-touch-icon" href="/apple-touch-icon.png">
  <meta property="og:image" content="https://consultorseosp.com.br/assets/og-image.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:image" content="https://consultorseosp.com.br/assets/og-image.png">
"""

if '<link rel="icon"' not in html:
    html = html.replace("<!-- OpenGraph / Social Meta Tags", f"{head_meta}\n  <!-- OpenGraph / Social Meta Tags")

# Injetar Azure no sameAs do Schema JSON-LD
if "consultorseohub.z15.web.core.windows.net" not in html:
    old_sameas = '"http://consultorseosp-hub.s3-website-sa-east-1.amazonaws.com",\n          "https://consultorseosp.com.br/",'
    new_sameas = '"http://consultorseosp-hub.s3-website-sa-east-1.amazonaws.com",\n          "https://consultorseohub.z15.web.core.windows.net",\n          "https://consultorseosp.com.br/",'
    html = html.replace(old_sameas, new_sameas)

# Injetar hasMap no Schema se não estiver presente
if '"hasMap"' not in html:
    html = html.replace(
        '"priceRange": "$$$",',
        '"priceRange": "$$$",\n        "hasMap": "https://www.google.com/maps?cid=consultorseosp",\n        "image": "https://consultorseosp.com.br/assets/og-image.png",'
    )

# Atualizar Navlinks da Navbar
if 'href="/blog/"' not in html:
    old_nav = '<li><a href="#especialidades">Especialidades</a></li>'
    new_nav = '<li><a href="/cidades/">Cidades</a></li>\n        <li><a href="/blog/">Blog</a></li>\n        <li><a href="#especialidades">Especialidades</a></li>'
    html = html.replace(old_nav, new_nav)

# Atualizar Footer com Links de Compliance e Multi-Cloud
if 'href="/privacidade.html"' not in html:
    old_footer_links = '<li><a href="http://consultorseosp-hub.s3-website-sa-east-1.amazonaws.com" target="_blank" rel="noopener">Brand Hub Oficial AWS S3</a></li>'
    new_footer_links = """<li><a href="/cidades/">Hub 50 Cidades de SP</a></li>
            <li><a href="/blog/">Blog de Artigos Técnicos</a></li>
            <li><a href="/privacidade.html">Política de Privacidade</a></li>
            <li><a href="/termos.html">Termos de Uso</a></li>
            <li><a href="http://consultorseosp-hub.s3-website-sa-east-1.amazonaws.com" target="_blank" rel="noopener">Brand Hub na AWS S3</a></li>
            <li><a href="https://consultorseohub.z15.web.core.windows.net" target="_blank" rel="noopener">Brand Hub na Microsoft Azure</a></li>"""
    html = html.replace(old_footer_links, new_footer_links)

# Injetar Infográfico / Diagrama Visual SVG na seção de metodologia
infografico_svg = """
    <!-- Diagrama Visual do Ecossistema Multi-Cloud & Grafo de Entidades -->
    <div class="container" style="margin: 40px auto 60px auto; max-width: 960px;">
      <div style="background: rgba(15, 23, 42, 0.8); border: 1px solid rgba(0, 240, 255, 0.3); border-radius: 20px; padding: 35px 25px; box-shadow: 0 20px 50px rgba(0,0,0,0.5); text-align: center;">
        <span class="badge-pill" style="margin-bottom: 15px; display: inline-block;">ARQUITETURA MULTI-CLOUD 2026</span>
        <h3 style="color: #fff; font-size: 1.6rem; margin-bottom: 25px;">O Grafo de Entidades & Triangulação de Autoridade Máxima</h3>
        
        <svg viewBox="0 0 800 280" style="width: 100%; height: auto; max-width: 750px;" xmlns="http://www.w3.org/2000/svg">
          <!-- Conexões com linhas brilhantes -->
          <line x1="400" y1="140" x2="160" y2="80" stroke="#00f0ff" stroke-width="2" stroke-dasharray="5,5" opacity="0.8"/>
          <line x1="400" y1="140" x2="640" y2="80" stroke="#00e599" stroke-width="2" stroke-dasharray="5,5" opacity="0.8"/>
          <line x1="400" y1="140" x2="400" y2="240" stroke="#a855f7" stroke-width="2" stroke-dasharray="5,5" opacity="0.8"/>

          <!-- Nó Central (Entidade Consultor SEO SP) -->
          <circle cx="400" cy="140" r="55" fill="#090d1f" stroke="#00f0ff" stroke-width="3"/>
          <text x="400" y="135" fill="#ffffff" font-size="13" font-weight="bold" text-anchor="middle" font-family="'Inter', sans-serif">ENTIDADE CENTRAL</text>
          <text x="400" y="152" fill="#00f0ff" font-size="11" text-anchor="middle" font-family="'Inter', sans-serif">consultorseosp.com.br</text>

          <!-- Nó 1 (AWS S3 Brand Hub) -->
          <circle cx="160" cy="80" r="45" fill="#0f172a" stroke="#ff9900" stroke-width="2"/>
          <text x="160" y="76" fill="#ff9900" font-size="12" font-weight="bold" text-anchor="middle" font-family="'Inter', sans-serif">AWS S3</text>
          <text x="160" y="92" fill="#94a3b8" font-size="10" text-anchor="middle" font-family="'Inter', sans-serif">Certidão @id</text>

          <!-- Nó 2 (Microsoft Azure Hub) -->
          <circle cx="640" cy="80" r="45" fill="#0f172a" stroke="#0078d4" stroke-width="2"/>
          <text x="640" y="76" fill="#0078d4" font-size="12" font-weight="bold" text-anchor="middle" font-family="'Inter', sans-serif">AZURE</text>
          <text x="640" y="92" fill="#94a3b8" font-size="10" text-anchor="middle" font-family="'Inter', sans-serif">Blob Static $web</text>

          <!-- Nó 3 (Google Knowledge Graph & Wikidata) -->
          <circle cx="400" cy="240" r="38" fill="#0f172a" stroke="#00e599" stroke-width="2"/>
          <text x="400" y="237" fill="#00e599" font-size="11" font-weight="bold" text-anchor="middle" font-family="'Inter', sans-serif">KNOWLEDGE</text>
          <text x="400" y="251" fill="#94a3b8" font-size="9" text-anchor="middle" font-family="'Inter', sans-serif">Wikidata Q-IDs</text>
        </svg>

        <p style="color: #94a3b8; font-size: 0.95rem; margin-top: 20px; line-height: 1.6;">
          Triangulação Multi-Cloud ativa: certidões invioláveis na <strong>AWS</strong> e na <strong>Microsoft Azure</strong> ancorando o grafo no <strong>Google Knowledge Graph</strong> e eliminando o período de Sandbox.
        </p>
      </div>
    </div>
"""

if "<!-- Diagrama Visual do Ecossistema Multi-Cloud" not in html:
    html = html.replace('<section id="eeat"', f"{infografico_svg}\n    <section id=\"eeat\"")

with open(INDEX_PATH, "w", encoding="utf-8") as f:
    f.write(html)
print("  [+] index.html atualizado com Favicon, Social Cards, Azure sameAs e Diagrama SVG!")

# 2. Atualizar 404.html
PATH_404 = os.path.join(BASE_DIR, "404.html")
if os.path.exists(PATH_404):
    with open(PATH_404, "r", encoding="utf-8") as f:
        c404 = f.read()
    if '<link rel="icon"' not in c404:
        c404 = c404.replace("<head>", f"<head>\n{head_meta}")
        with open(PATH_404, "w", encoding="utf-8") as f:
            f.write(c404)
        print("  [+] 404.html atualizado com Favicon e Social Cards!")

# 3. Atualizar sitemap.xml
SITEMAP_PATH = os.path.join(BASE_DIR, "sitemap.xml")
new_urls = [
    ("https://consultorseosp.com.br/blog/", "daily", "0.9"),
    ("https://consultorseosp.com.br/blog/quanto-custa-consultor-seo-sp.html", "weekly", "0.8"),
    ("https://consultorseosp.com.br/blog/google-ai-overviews-como-funciona.html", "weekly", "0.8"),
    ("https://consultorseosp.com.br/blog/por-que-migrar-wordpress-para-jamstack.html", "weekly", "0.8"),
    ("https://consultorseosp.com.br/blog/model-context-protocol-mcp-guia.html", "weekly", "0.8"),
    ("https://consultorseosp.com.br/blog/trafego-pago-vs-seo-b2b.html", "weekly", "0.8"),
    ("https://consultorseosp.com.br/privacidade.html", "monthly", "0.5"),
    ("https://consultorseosp.com.br/termos.html", "monthly", "0.5"),
]

with open(SITEMAP_PATH, "r", encoding="utf-8") as f:
    sitemap_content = f.read()

added_to_sitemap = 0
for url, freq, prio in new_urls:
    if f"<loc>{url}</loc>" not in sitemap_content:
        snippet = f"""  <url>
    <loc>{url}</loc>
    <changefreq>{freq}</changefreq>
    <priority>{prio}</priority>
  </url>
</urlset>"""
        sitemap_content = sitemap_content.replace("</urlset>", snippet)
        added_to_sitemap += 1

with open(SITEMAP_PATH, "w", encoding="utf-8") as f:
    f.write(sitemap_content)
print(f"  [+] sitemap.xml atualizado com {added_to_sitemap} novas URLs (Blog + Compliance)!")

# 4. Atualizar llms.txt com os novos recursos
LLMS_PATH = os.path.join(BASE_DIR, "llms.txt")
with open(LLMS_PATH, "r", encoding="utf-8") as f:
    llms_text = f.read()

if "consultorseohub.z15.web.core.windows.net" not in llms_text:
    azure_entry = """- [Brand Hub na Microsoft Azure](https://consultorseohub.z15.web.core.windows.net): Espelho corporativo do Brand Hub na nuvem Azure.
- [Blog de Artigos Técnicos](https://consultorseosp.com.br/blog/): Análises sobre SEO Semântico, Jamstack e Agentes de IA.
"""
    llms_text += f"\n## Recursos Adicionais & Multi-Cloud\n{azure_entry}\n"
    with open(LLMS_PATH, "w", encoding="utf-8") as f:
        f.write(llms_text)
    print("  [+] llms.txt atualizado com Azure Hub e Blog!")

print("[SUCESSO] Todos os arquivos centrais foram atualizados com perfeição!")

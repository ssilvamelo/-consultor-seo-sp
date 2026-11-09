import urllib.request

headers = {'User-Agent': 'Mozilla/5.0'}

print("=== CHECKING HOSTINGER PRODUCTION ===")
req = urllib.request.Request('https://consultorseosp.com.br/?nocache=2', headers=headers)
with urllib.request.urlopen(req, timeout=15) as r:
    html = r.read().decode('utf-8')
    print("Hostinger Status:", r.status)
    has_cert = 'id="certificacao-entidade"' in html
    print("Seção no rodapé (#certificacao-entidade) presente:", has_cert)
    
    # Check if hero contains the figure
    hero_part = html[html.find('class="stats-ribbon"'):html.find('class="eas-banner"')]
    has_figure_in_hero = 'consultorseo-media' in hero_part
    print("Figura ainda está no topo/hero?:", has_figure_in_hero)

# Check the image directly
img_url = "https://consultorseosp.com.br/assets/img/consultor-seo-sao-paulo-especialista-inteligencia-artificial.webp"
req_img = urllib.request.Request(img_url, headers=headers)
with urllib.request.urlopen(req_img, timeout=15) as r_img:
    img_bytes = r_img.read()
    print(f"Imagem WebP baixada com sucesso ({len(img_bytes)} bytes)!")

print("\n=== CHECKING AWS S3 BRAND HUB ===")
req_s3 = urllib.request.Request('http://consultorseosp-hub.s3-website-sa-east-1.amazonaws.com/?nocache=2', headers=headers)
with urllib.request.urlopen(req_s3, timeout=15) as r2:
    html2 = r2.read().decode('utf-8')
    print("AWS S3 Status:", r2.status)
    print("AWS S3 #certificacao-entidade presente:", 'id="certificacao-entidade"' in html2)

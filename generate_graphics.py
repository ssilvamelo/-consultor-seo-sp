import os
from PIL import Image, ImageDraw, ImageFont

BASE_DIR = r"C:\Users\User\.gemini\antigravity\scratch\consultorseosp"
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
os.makedirs(ASSETS_DIR, exist_ok=True)

# 1. Gerar Favicon e Ícones
def generate_favicons():
    size = 512
    img = Image.new("RGBA", (size, size), (8, 11, 24, 255))
    draw = ImageDraw.Draw(img)

    # Círculo externo com brilho cyan
    margin = 40
    draw.ellipse(
        [margin, margin, size - margin, size - margin],
        outline=(0, 240, 255, 255),
        width=24
    )

    # Nó interno com brilho esmeralda
    center_margin = 140
    draw.ellipse(
        [center_margin, center_margin, size - center_margin, size - center_margin],
        fill=(0, 229, 153, 230)
    )

    # Letra estilizada "S" ou grafo
    draw.arc([160, 160, 350, 260], start=180, end=0, fill=(8, 11, 24, 255), width=28)
    draw.arc([160, 250, 350, 350], start=0, end=180, fill=(8, 11, 24, 255), width=28)

    # Salvar formatos
    png_path = os.path.join(BASE_DIR, "favicon.png")
    apple_path = os.path.join(BASE_DIR, "apple-touch-icon.png")
    ico_path = os.path.join(BASE_DIR, "favicon.ico")

    img.save(png_path, "PNG")
    img.resize((180, 180), Image.Resampling.LANCZOS).save(apple_path, "PNG")
    img.resize((64, 64), Image.Resampling.LANCZOS).save(ico_path, format="ICO", sizes=[(64, 64), (32, 32), (16, 16)])
    print("[+] Favicons gerados com sucesso (ICO, PNG, Apple Touch Icon)!")

# 2. Gerar OpenGraph Image (1200x630)
def generate_og_image():
    w, h = 1200, 630
    img = Image.new("RGB", (w, h), (9, 13, 31))
    draw = ImageDraw.Draw(img)

    # Gradiente de fundo sutil
    for y in range(h):
        r = int(9 + (y / h) * 12)
        g = int(13 + (y / h) * 16)
        b = int(31 + (y / h) * 35)
        draw.line([(0, y), (w, y)], fill=(r, g, b))

    # Borda tecnológica
    draw.rectangle([20, 20, w - 20, h - 20], outline=(0, 240, 255, 120), width=3)
    draw.rectangle([28, 28, w - 28, h - 28], outline=(0, 229, 153, 60), width=1)

    # Badge de Categoria
    draw.rounded_rectangle([70, 70, 480, 120], radius=12, fill=(15, 23, 42), outline=(0, 240, 255), width=2)
    draw.text((90, 83), "CONSULTOR SEO SP  •  ENTITY-FIRST", fill=(0, 240, 255))

    # Título Principal
    draw.text((70, 160), "SEO Semantico &\nAgentes de IA em Sao Paulo", fill=(255, 255, 255), spacing=20)

    # Subtítulo com diferenciais
    draw.text((70, 350), "• Arquitetura Jamstack Ultrarrapida (< 50ms) - Zero WordPress", fill=(148, 163, 184))
    draw.text((70, 395), "• Brand Hub Multi-Cloud: AWS S3 + Microsoft Azure", fill=(148, 163, 184))
    draw.text((70, 440), "• Qualificacao para Google AI Overviews & Knowledge Graph", fill=(148, 163, 184))
    draw.text((70, 485), "• Cobertura Estrategica nos 50 Polos Industriais de SP", fill=(148, 163, 184))

    # Barra de Rodapé
    draw.line([(70, 545), (w - 70, 545)], fill=(30, 41, 59), width=2)
    draw.text((70, 565), "https://consultorseosp.com.br", fill=(0, 240, 255))
    draw.text((850, 565), "Atendimento: (11) 91873-8164", fill=(0, 229, 153))

    og_path = os.path.join(ASSETS_DIR, "og-image.png")
    img.save(og_path, "PNG", optimize=True)
    print(f"[+] Imagem OpenGraph 1200x630 gerada em: {og_path}")

if __name__ == "__main__":
    generate_favicons()
    generate_og_image()

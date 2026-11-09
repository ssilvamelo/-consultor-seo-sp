import os
from PIL import Image, ImageDraw, ImageFont

def create_banner():
    width = 1200
    height = 675
    
    # Base image with deep tech background
    img = Image.new("RGBA", (width, height), (6, 9, 19, 255))
    draw = ImageDraw.Draw(img)
    
    # 1. Subtle background gradient
    for y in range(height):
        ratio = y / height
        r = int(6 + ratio * 8)
        g = int(9 + ratio * 16)
        b = int(19 + ratio * 28)
        draw.line([(0, y), (width, y)], fill=(r, g, b, 255))
        
    # 2. Draw subtle tech grid
    grid_color = (30, 58, 95, 70)
    for x in range(0, width, 40):
        draw.line([(x, 0), (x, height)], fill=grid_color, width=1)
    for y in range(0, height, 40):
        draw.line([(0, y), (width, y)], fill=grid_color, width=1)
        
    # 3. Glowing borders
    # Outer margin
    m = 24
    draw.rounded_rectangle([m, m, width - m, height - m], radius=16, outline=(56, 189, 248, 120), width=2)
    draw.rounded_rectangle([m + 6, m + 6, width - m - 6, height - m - 6], radius=12, outline=(16, 185, 129, 60), width=1)
    
    # Fonts
    # Choose available Windows TrueType fonts
    font_badge = ImageFont.truetype(r"C:\Windows\Fonts\segoeuib.ttf", 16)
    font_title = ImageFont.truetype(r"C:\Windows\Fonts\segoeuib.ttf", 52)
    font_subtitle = ImageFont.truetype(r"C:\Windows\Fonts\segoeui.ttf", 26)
    font_card_title = ImageFont.truetype(r"C:\Windows\Fonts\segoeuib.ttf", 18)
    font_card_sub = ImageFont.truetype(r"C:\Windows\Fonts\segoeui.ttf", 14)
    font_meta = ImageFont.truetype(r"C:\Windows\Fonts\consola.ttf", 15)
    
    # Center X
    cx = width // 2
    
    # 4. Badge Pill at top
    badge_text = "AUTORIDADE DE ENTIDADE  •  SÃO PAULO - SP"
    bbox = font_badge.getbbox(badge_text)
    bw = bbox[2] - bbox[0]
    bh = bbox[3] - bbox[1]
    
    pill_x1 = cx - bw // 2 - 20
    pill_y1 = 65
    pill_x2 = cx + bw // 2 + 20
    pill_y2 = pill_y1 + bh + 16
    
    draw.rounded_rectangle([pill_x1, pill_y1, pill_x2, pill_y2], radius=12, fill=(15, 23, 42, 230), outline=(56, 189, 248, 200), width=1)
    draw.text((cx - bw // 2, pill_y1 + 8), badge_text, font=font_badge, fill=(56, 189, 248, 255))
    
    # 5. Main Title
    title_text = "CONSULTOR SEO SÃO PAULO"
    t_bbox = font_title.getbbox(title_text)
    tw = t_bbox[2] - t_bbox[0]
    draw.text((cx - tw // 2, 140), title_text, font=font_title, fill=(56, 189, 248, 255))
    
    # 6. Subtitle
    sub_text = "Especialista em SEO Semântico & Agentes de IA"
    s_bbox = font_subtitle.getbbox(sub_text)
    sw = s_bbox[2] - s_bbox[0]
    draw.text((cx - sw // 2, 215), sub_text, font=font_subtitle, fill=(241, 245, 249, 255))
    
    # Decorative line under subtitle
    line_w = 400
    draw.line([(cx - line_w // 2, 265), (cx + line_w // 2, 265)], fill=(16, 185, 129, 200), width=2)
    
    # 7. 3 Architecture Pillar Cards
    cards = [
        ("SEO SEMÂNTICO", "Entity-First & Knowledge Graph\nTriangulação S3 + Azure"),
        ("ALTA VELOCIDADE", "Jamstack Própria (< 50ms)\nZero Dependência WordPress"),
        ("AGENTES AUTÔNOMOS", "Protocolo MCP & Automações\nOperações Ativas 24/7")
    ]
    
    card_w = 340
    card_h = 130
    gap = 30
    total_cards_w = 3 * card_w + 2 * gap
    start_x = (width - total_cards_w) // 2
    cards_y = 305
    
    for i, (ctitle, csub) in enumerate(cards):
        x1 = start_x + i * (card_w + gap)
        y1 = cards_y
        x2 = x1 + card_w
        y2 = y1 + card_h
        
        # Draw card background
        draw.rounded_rectangle([x1, y1, x2, y2], radius=12, fill=(15, 23, 42, 210), outline=(30, 58, 95, 200), width=1)
        
        # Mini accent bar on left of card
        draw.rounded_rectangle([x1, y1 + 16, x1 + 4, y2 - 16], radius=2, fill=(56, 189, 248, 255))
        
        # Card title
        draw.text((x1 + 22, y1 + 20), ctitle, font=font_card_title, fill=(56, 189, 248, 255))
        
        # Card subtitle (multiline)
        lines = csub.split("\n")
        draw.text((x1 + 22, y1 + 54), lines[0], font=font_card_sub, fill=(203, 213, 225, 255))
        draw.text((x1 + 22, y1 + 78), lines[1], font=font_card_sub, fill=(148, 163, 184, 255))

    # 8. Technical Geo & Metadata Footer inside image
    footer_y = 485
    draw.line([(m + 30, footer_y), (width - m - 30, footer_y)], fill=(30, 58, 95, 180), width=1)
    
    meta1 = "CONSULTORSEOSP.COM.BR  |  GEO: SÃO PAULO - SP  |  TEL: (11) 91873-8164"
    m1_bbox = font_meta.getbbox(meta1)
    m1_w = m1_bbox[2] - m1_bbox[0]
    draw.text((cx - m1_w // 2, footer_y + 25), meta1, font=font_meta, fill=(16, 185, 129, 255))
    
    meta2 = "LAT: -23.5615  |  LONG: -46.6560  |  BRAND HUB MULTI-CLOUD: AWS S3 + AZURE $WEB"
    m2_bbox = font_meta.getbbox(meta2)
    m2_w = m2_bbox[2] - m2_bbox[0]
    draw.text((cx - m2_w // 2, footer_y + 55), meta2, font=font_meta, fill=(148, 163, 184, 255))
    
    meta3 = "CERTIFICAÇÃO OFICIAL DE ENTIDADE DIGITAL & DIRETRIZES DE QUALIDADE GOOGLE SEARCH"
    m3_bbox = font_meta.getbbox(meta3)
    m3_w = m3_bbox[2] - m3_bbox[0]
    draw.text((cx - m3_w // 2, footer_y + 85), meta3, font=font_meta, fill=(100, 116, 139, 220))
    
    # Output path
    out_path = r"C:\Users\User\.gemini\antigravity\scratch\consultorseosp\assets\img\consultor-seo-sao-paulo-especialista-inteligencia-artificial.webp"
    
    # Save as WebP
    # Convert RGBA to RGB for webp compression or save RGBA directly
    img.convert("RGB").save(out_path, "WEBP", quality=95, method=6)
    print(f"Generated clean WebP at: {out_path}")

if __name__ == "__main__":
    create_banner()

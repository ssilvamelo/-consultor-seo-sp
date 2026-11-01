"""
Script de Otimização Estratégica de Linkagem Interna & Textos-Âncora
Implementa as diretrizes do Screaming Frog SEO Spider:
1. Elimina âncoras genéricas ('Ler Artigo Completo') no Hub do Blog.
2. Cria clusterização cruzada entre Blog e Cidades de alto PIB.
3. Cria linkagem bidirecional entre Cidades e o Guia de Preços.
"""

import os
import re

BASE_DIR = r"C:\Users\User\.gemini\antigravity\scratch\consultorseosp"

def update_blog_index():
    path = os.path.join(BASE_DIR, "blog", "index.html")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Substituir âncoras genéricas por âncoras semânticas ricas
    replacements = [
        (
            r'<a href="quanto-custa-consultor-seo-sp\.html"[^>]*>Ler Artigo Completo →</a>',
            '<a href="quanto-custa-consultor-seo-sp.html" style="color: var(--cyan); font-weight: 600; text-decoration: none;">Ver Tabela Completa de Preços de SEO em SP →</a>'
        ),
        (
            r'<a href="google-ai-overviews-como-funciona\.html"[^>]*>Ler Artigo Completo →</a>',
            '<a href="google-ai-overviews-como-funciona.html" style="color: var(--cyan); font-weight: 600; text-decoration: none;">Ver Guia de Otimização para AI Overviews →</a>'
        ),
        (
            r'<a href="por-que-migrar-wordpress-para-jamstack\.html"[^>]*>Ler Artigo Completo →</a>',
            '<a href="por-que-migrar-wordpress-para-jamstack.html" style="color: var(--cyan); font-weight: 600; text-decoration: none;">Descobrir Por Que Migrar do WordPress para Jamstack →</a>'
        ),
        (
            r'<a href="model-context-protocol-mcp-guia\.html"[^>]*>Ler Artigo Completo →</a>',
            '<a href="model-context-protocol-mcp-guia.html" style="color: var(--cyan); font-weight: 600; text-decoration: none;">Aprender a Implementar Servidores MCP com IA →</a>'
        ),
        (
            r'<a href="trafego-pago-vs-seo-b2b\.html"[^>]*>Ler Artigo Completo →</a>',
            '<a href="trafego-pago-vs-seo-b2b.html" style="color: var(--cyan); font-weight: 600; text-decoration: none;">Comparar ROI de SEO vs Tráfego Pago no B2B →</a>'
        )
    ]

    for pattern, repl in replacements:
        content = re.sub(pattern, repl, content)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("[+] blog/index.html atualizado com âncoras semânticas ricas!")

def update_pricing_article():
    path = os.path.join(BASE_DIR, "blog", "quanto-custa-consultor-seo-sp.html")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    regional_section = """
    <h2 style="color: #fff; margin: 35px 0 15px 0;">4. Variação de Demanda por Polo Econômico no Estado de SP</h2>
    <p>A intensidade competitiva e os segmentos corporativos mudam conforme a região do estado. Nossa consultoria possui mapeamento de dados específico para os maiores centros de negócios de São Paulo:</p>
    <ul style="margin-bottom: 25px; line-height: 1.8;">
      <li><strong>Capital e Região Metropolitana:</strong> Estratégias de autoridade para o maior centro financeiro da América Latina via nossa página de <a href="../cidades/sao-paulo/" style="color: var(--cyan); text-decoration: underline; font-weight: 600;">Consultor SEO em São Paulo</a>.</li>
      <li><strong>Polo de Inovação e Tecnologia:</strong> Foco em empresas de software, biotecnologia e indústria em <a href="../cidades/campinas/" style="color: var(--cyan); text-decoration: underline; font-weight: 600;">Consultor SEO em Campinas</a>.</li>
      <li><strong>Centros Corporativos e Sedes B2B:</strong> Otimização de marcas em <a href="../cidades/barueri-alphaville/" style="color: var(--cyan); text-decoration: underline; font-weight: 600;">Consultor SEO em Barueri e Alphaville</a>.</li>
      <li><strong>Comércio Exterior e Logística Portuária:</strong> Captação internacional e serviços aduaneiros em <a href="../cidades/santos/" style="color: var(--cyan); text-decoration: underline; font-weight: 600;">Consultor SEO em Santos</a>.</li>
      <li><strong>Complexo Industrial e Distribuição:</strong> Estratégias para grandes malhas logísticas em <a href="../cidades/guarulhos/" style="color: var(--cyan); text-decoration: underline; font-weight: 600;">Consultor SEO em Guarulhos</a>.</li>
    </ul>
    <p>Para ver todas as regiões atendidas, consulte nosso índice completo de <a href="../cidades/" style="color: var(--cyan); text-decoration: underline;">todas as 50 cidades atendidas no Estado de São Paulo</a>.</p>
"""

    if "4. Variação de Demanda por Polo Econômico" not in content:
        content = content.replace("</div>\n\n    <!-- CTA de Conversão no Final do Artigo -->", f"{regional_section}\n    </div>\n\n    <!-- CTA de Conversão no Final do Artigo -->")
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print("[+] blog/quanto-custa-consultor-seo-sp.html atualizado com clusterização para Cidades!")

def update_ai_overviews_article():
    path = os.path.join(BASE_DIR, "blog", "google-ai-overviews-como-funciona.html")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    links_box = """
    <div style="background: rgba(15, 23, 42, 0.6); border-left: 4px solid var(--cyan); padding: 20px; margin: 30px 0; border-radius: 0 12px 12px 0;">
      <h4 style="color: #fff; margin-bottom: 8px;">Recursos Estratégicos Complementares:</h4>
      <p style="margin-bottom: 0; font-size: 0.95rem;">
        Entenda também quanto investir em uma <a href="quanto-custa-consultor-seo-sp.html" style="color: var(--cyan); text-decoration: underline; font-weight: 600;">consultoria especializada em SEO em São Paulo</a> e como integrar seus bancos de dados a LLMs utilizando nosso <a href="model-context-protocol-mcp-guia.html" style="color: var(--cyan); text-decoration: underline; font-weight: 600;">guia definitivo do Model Context Protocol (MCP)</a>.
      </p>
    </div>
"""
    if "Recursos Estratégicos Complementares" not in content:
        content = content.replace("</div>\n\n    <!-- CTA de Conversão no Final do Artigo -->", f"{links_box}\n    </div>\n\n    <!-- CTA de Conversão no Final do Artigo -->")
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print("[+] blog/google-ai-overviews-como-funciona.html atualizado com links contextuais cruzados!")

def update_jamstack_article():
    path = os.path.join(BASE_DIR, "blog", "por-que-migrar-wordpress-para-jamstack.html")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    jamstack_links = """
    <div style="background: rgba(15, 23, 42, 0.6); border-left: 4px solid var(--cyan); padding: 20px; margin: 30px 0; border-radius: 0 12px 12px 0;">
      <h4 style="color: #fff; margin-bottom: 8px;">Planejamento de Migração e Custos:</h4>
      <p style="margin-bottom: 0; font-size: 0.95rem;">
        Veja a <a href="quanto-custa-consultor-seo-sp.html" style="color: var(--cyan); text-decoration: underline; font-weight: 600;">tabela real de custos de consultoria de SEO</a> e compare o impacto financeiro de tráfego orgânico versus anúncios pagos em nosso artigo sobre <a href="trafego-pago-vs-seo-b2b.html" style="color: var(--cyan); text-decoration: underline; font-weight: 600;">Tráfego Pago vs SEO no B2B</a>.
      </p>
    </div>
"""
    if "Planejamento de Migração e Custos" not in content:
        content = content.replace("</div>\n\n    <!-- CTA de Conversão no Final do Artigo -->", f"{jamstack_links}\n    </div>\n\n    <!-- CTA de Conversão no Final do Artigo -->")
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print("[+] blog/por-que-migrar-wordpress-para-jamstack.html atualizado!")

def update_top_cities():
    top_cities = [
        "cidades/sao-paulo/index.html",
        "cidades/campinas/index.html",
        "cidades/barueri-alphaville/index.html",
        "cidades/santos/index.html",
        "cidades/guarulhos/index.html"
    ]

    for city_rel in top_cities:
        path = os.path.join(BASE_DIR, city_rel)
        if not os.path.exists(path):
            continue
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()

        guide_callout = """
      <!-- Guia de Custos & Linkagem Interna Estratégica -->
      <div style="background: rgba(0, 240, 255, 0.05); border: 1px solid rgba(0, 240, 255, 0.2); border-radius: 12px; padding: 20px; margin: 30px 0;">
        <p style="margin: 0; color: #cbd5e1; font-size: 0.95rem;">
          💼 <strong>Planejando a contratação?</strong> Consulte nossa análise transparente sobre <a href="../../blog/quanto-custa-consultor-seo-sp.html" style="color: var(--cyan); text-decoration: underline; font-weight: 600;">quanto custa um consultor de SEO em São Paulo em 2026</a>, incluindo modelos de fee mensal e auditorias para empresas.
        </p>
      </div>
"""
        if "Planejando a contratação?" not in content:
            # Inserir antes da seção de FAQ ou do formulário
            if '<section class="section faq"' in content:
                content = content.replace('<section class="section faq"', f"{guide_callout}\n  <section class=\"section faq\"")
            elif '<section class="section cta"' in content:
                content = content.replace('<section class="section cta"', f"{guide_callout}\n  <section class=\"section cta\"")
            else:
                content = content.replace('</main>', f"{guide_callout}\n</main>")

            with open(path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"[+] {city_rel} atualizada com link reverso para o Guia de Custos!")

if __name__ == "__main__":
    print("[*] Iniciando otimização estratégica de linkagem interna...")
    update_blog_index()
    update_pricing_article()
    update_ai_overviews_article()
    update_jamstack_article()
    update_top_cities()
    print("\n[SUCESSO] Todas as otimizações de linkagem semântica foram aplicadas!")

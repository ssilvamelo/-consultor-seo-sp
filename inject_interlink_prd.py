import bs4
import json

HTML_FILE = r"C:\Users\User\.gemini\antigravity\scratch\consultorseosp\index.html"

with open(HTML_FILE, "r", encoding="utf-8") as f:
    html = f.read()

soup = bs4.BeautifulSoup(html, "lxml")

# 1. ATUALIZAR SCHEMA JSON-LD: sameAs (YouTube, Telegram, WhatsApp, GitHub)
sc = soup.find("script", type="application/ld+json")
if sc:
    data = json.loads(sc.string)
    if "@graph" in data:
        for node in data["@graph"]:
            types = node.get("@type", [])
            if isinstance(types, str): types = [types]
            if any(t in types for t in ("ProfessionalService", "LocalBusiness", "Organization")):
                same_as = node.get("sameAs", [])
                links_to_add = [
                    "https://youtube.com/@prd_monitoramento_caixa_dgua",
                    "https://t.me/servicosprd",
                    "https://whatsapp.com/channel/0029VbE4mL8EFeXcHIR5cs1l",
                    "https://servicosprd.com.br/"
                ]
                for l in links_to_add:
                    if l not in same_as:
                        same_as.append(l)
                node["sameAs"] = same_as

                # Conectar knowsAbout a estudos de caso de telemetria predial
                ka = node.get("knowsAbout", [])
                if "Engenharia de Telemetria e Monitoramento de Caixa d'Água IoT" not in ka:
                    ka.append("Engenharia de Telemetria e Monitoramento de Caixa d'Água IoT")
                node["knowsAbout"] = ka

    sc.string = json.dumps(data, indent=2, ensure_ascii=False)

html_str = str(soup)

# 2. INJETAR SEÇÃO DE CASE REAL DE ENGENHARIA DE SEO COM LINK ESTRATÉGICO PARA A PRD
case_prd_section = """
    <!-- SEÇÃO DE PROVA DE CONCEITO & ENGENHARIA EM PRODUÇÃO (CASE PRD) -->
    <section id="case-engenharia-prd" style="padding: 70px 0; background: rgba(9, 13, 31, 0.7); border-top: 1px solid var(--border); border-bottom: 1px solid var(--border);">
      <div class="container">
        <div class="section-header" style="text-align: center; margin-bottom: 35px;">
          <span class="section-tag" style="background: rgba(16, 185, 129, 0.12); color: #10b981; border-color: rgba(16, 185, 129, 0.3);">Estudo de Caso em Produção</span>
          <h2 class="section-title">Engenharia SEO Semântico Aplicada na Prática: Caso PRD</h2>
          <p class="section-desc">
            Veja como a nossa arquitetura <strong>Entity-First</strong>, aliada a dados estruturados profundos e nuvem híbrida, colocou em operação um dos sistemas de telemetria mais rápidos do Brasil.
          </p>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 2rem; align-items: center; background: rgba(15, 23, 42, 0.85); padding: 35px; border-radius: 20px; border: 1px solid rgba(56, 189, 248, 0.25);">
          <div>
            <span class="badge-pill" style="margin-bottom: 15px; display: inline-block;">INFRAESTRUTURA IOT & SEO</span>
            <h3 style="color: #fff; font-size: 1.45rem; margin-bottom: 15px; line-height: 1.35;">
              Monitoramento de Alta Frequência e Telemetria Hídrica Predial
            </h3>
            <p style="color: #cbd5e1; font-size: 0.95rem; line-height: 1.65; margin-bottom: 15px;">
              Desenvolvido sob nossa metodologia proprietária, o ecossistema da <strong>PRD Consultoria</strong> integra sensores industriais de pressão hidrostática 4–20mA e automação predial a uma plataforma Jamstack com TTFB inferior a 50ms e dados estruturados certificados perante o Google.
            </p>
            <p style="color: #94a3b8; font-size: 0.9rem; line-height: 1.6; margin-bottom: 20px;">
              A solução é referência no segmento de <a href="https://servicosprd.com.br/servico-caixa-dagua.html" target="_blank" rel="noopener" style="color: #38bdf8; font-weight: 700; text-decoration: underline;">monitoramento de caixa d'água</a> e reservatórios para condomínios, eliminando transbordamentos e queima de bombas elétricas em São Paulo e cidades do interior.
            </p>
            <div style="display: flex; gap: 1rem; flex-wrap: wrap;">
              <a href="https://servicosprd.com.br/servico-caixa-dagua.html" target="_blank" rel="noopener" class="btn-primary" style="display: inline-flex; align-items: center; gap: 8px; padding: 10px 18px; font-size: 0.9rem; background: #0284c7; color: #fff; text-decoration: none; border-radius: 8px; font-weight: 700;">
                <span>Visitar Estudo Técnico na PRD</span>
                <span>↗</span>
              </a>
              <a href="https://youtube.com/@prd_monitoramento_caixa_dgua" target="_blank" rel="noopener" style="display: inline-flex; align-items: center; gap: 8px; padding: 10px 18px; font-size: 0.9rem; background: rgba(239, 68, 68, 0.15); color: #f87171; border: 1px solid rgba(239, 68, 68, 0.3); text-decoration: none; border-radius: 8px; font-weight: 700;">
                <span>Canal YouTube</span>
                <span>▶</span>
              </a>
            </div>
          </div>

          <div style="text-align: center; background: rgba(9, 13, 31, 0.9); padding: 25px; border-radius: 16px; border: 1px solid rgba(255,255,255,0.08);">
            <div style="font-size: 2.8rem; font-weight: 900; color: #10b981; font-family: monospace;">10.0 / 10</div>
            <div style="color: #38bdf8; font-weight: 700; font-size: 1.05rem; margin-top: 5px;">Nota Máxima em IA & Search Console</div>
            <p style="color: #94a3b8; font-size: 0.85rem; margin-top: 10px; line-height: 1.5;">
              Indexação de dados estruturados Google Imagens 2.0 com selo Licenciável, Brand Hub AWS S3 e suporte a agentes WebMCP.
            </p>
          </div>
        </div>
      </div>
    </section>
"""

# Inserir antes da seção de certificação
if '<section id="certificacao-entidade"' in html_str:
    html_str = html_str.replace('<section id="certificacao-entidade"', case_prd_section + '\n    <section id="certificacao-entidade"')
else:
    html_str = html_str.replace('</main>', case_prd_section + '\n  </main>')

# 3. ATUALIZAR O FOOTER (INTERLINK E PROPRIEDADES SOCIAIS)
footer_interlink = """
            <li><a href="https://servicosprd.com.br/servico-caixa-dagua.html" target="_blank" rel="noopener">Case Telemetria PRD (Caixa d'Água)</a></li>
            <li><a href="https://youtube.com/@prd_monitoramento_caixa_dgua" target="_blank" rel="noopener">Canal Oficial YouTube</a></li>
            <li><a href="https://t.me/servicosprd" target="_blank" rel="noopener">Comunidade Telegram</a></li>
            <li><a href="https://whatsapp.com/channel/0029VbE4mL8EFeXcHIR5cs1l" target="_blank" rel="noopener">Canal WhatsApp</a></li>
"""
html_str = html_str.replace('<li><a href="http://consultorseosp-hub.s3-website-sa-east-1.amazonaws.com"', footer_interlink + '            <li><a href="http://consultorseosp-hub.s3-website-sa-east-1.amazonaws.com"')

with open(HTML_FILE, "w", encoding="utf-8") as f:
    f.write(html_str)

print("[+] consultorseosp/index.html atualizado com sucesso com Interlink de Engenharia!")

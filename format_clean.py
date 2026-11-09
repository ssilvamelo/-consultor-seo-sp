import re

index_path = r"C:\Users\User\.gemini\antigravity\scratch\consultorseosp\index.html"

with open(index_path, "r", encoding="utf-8") as f:
    text = f.read()

clean_sec = '''    <!-- Seção de Credenciamento Técnico de Entidade Digital -->
    <section id="certificacao-entidade" style="padding: 50px 0 60px; background: rgba(15, 23, 42, 0.4); border-top: 1px solid var(--border);">
      <div class="container" style="text-align: center; max-width: 960px;">
        <span class="badge-pill" style="margin-bottom: 12px; display: inline-block;">INFRAESTRUTURA TÉCNICA 2026</span>
        <h3 style="color: #fff; font-size: 1.5rem; margin-bottom: 24px;">Credenciamento Técnico &amp; Infraestrutura Multi-Cloud</h3>
        <figure class="consultorseo-media" itemscope itemtype="https://schema.org/ImageObject" style="margin: 0 auto;">
          <link itemprop="license" href="https://consultorseosp.com.br/termos-de-uso.html" />
          <link itemprop="acquireLicensePage" href="https://consultorseosp.com.br/contato.html" />
          <span itemprop="creator" itemscope itemtype="https://schema.org/Organization" style="display:none;"><span itemprop="name">Consultor SEO SP</span></span>
          <img 
            src="/assets/img/consultor-seo-sao-paulo-especialista-inteligencia-artificial.webp" 
            alt="Consultor SEO em São Paulo especialista em SEO Semântico e Agentes de IA - Consultor SEO SP" 
            title="Consultoria de SEO e Automação com Inteligência Artificial em São Paulo - Consultor SEO SP"
            width="1200" 
            height="675" 
            loading="lazy" 
            decoding="async"
            itemprop="contentUrl"
            style="width: 100%; height: auto; border-radius: 16px; border: 1px solid rgba(56, 189, 248, 0.35); box-shadow: 0 15px 35px rgba(0,0,0,0.5);"
          />
          <figcaption itemprop="caption" style="font-size: 0.85rem; color: #94a3b8; margin-top: 0.75rem; text-align: center;">
            <strong>Consultor SEO em São Paulo:</strong> Engenharia de SEO Semântico (Entity-First), Brand Hub Multi-Cloud e automação com agentes autônomos de IA para empresas B2B.
          </figcaption>
        </figure>
      </div>
    </section>'''

pattern = re.compile(r'    <!-- Seção de Credenciamento Técnico de Entidade Digital -->.*?    </section>', re.DOTALL)
new_text = pattern.sub(clean_sec, text, count=1)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(new_text)

print("Cleaned up successfully!")

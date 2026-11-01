import os
import json

BASE_DIR = r"C:\Users\User\.gemini\antigravity\scratch\consultorseosp"
BLOG_DIR = os.path.join(BASE_DIR, "blog")
os.makedirs(BLOG_DIR, exist_ok=True)

# Template base de estilo e navegação idêntico à Home
HEADER_NAV = """
  <nav class="nav">
    <div class="nav-content">
      <a href="/" class="logo">
        <span class="logo-icon">▲</span>
        <span class="logo-text">Consultor SEO SP</span>
      </a>
      <div class="nav-links">
        <a href="/">Home</a>
        <a href="/cidades/">Cidades</a>
        <a href="/blog/">Blog</a>
        <a href="/#simulador">Simulador</a>
        <a href="/#contato" class="btn btn-primary">Falar com Especialista</a>
      </div>
    </div>
  </nav>
"""

FOOTER = """
  <footer class="footer">
    <div class="container footer-content">
      <div class="footer-col">
        <a href="/" class="logo">
          <span class="logo-icon">▲</span>
          <span class="logo-text">Consultor SEO SP</span>
        </a>
        <p class="footer-desc">Especialista em SEO Semântico de alta conversão e automação corporativa com agentes autônomos de Inteligência Artificial em São Paulo - SP.</p>
        <p class="footer-nap">📍 Av. Paulista, 1000 - Bela Vista, São Paulo - SP<br>📞 WhatsApp: +55 (11) 91873-8164<br>✉️ contato@consultorseosp.com.br</p>
      </div>
      <div class="footer-col">
        <h4>Ecossistema</h4>
        <ul>
          <li><a href="/">Página Inicial</a></li>
          <li><a href="/cidades/">Cidades Atendidas em SP</a></li>
          <li><a href="/blog/">Blog & Artigos Técnicos</a></li>
          <li><a href="/llms.txt">Superfície para Agentes (llms.txt)</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Compliance & Multi-Cloud</h4>
        <ul>
          <li><a href="/privacidade.html">Política de Privacidade</a></li>
          <li><a href="/termos.html">Termos de Uso</a></li>
          <li><a href="http://consultorseosp-hub.s3-website-sa-east-1.amazonaws.com" target="_blank" rel="noopener">Brand Hub na AWS S3</a></li>
          <li><a href="https://consultorseohub.z15.web.core.windows.net" target="_blank" rel="noopener">Brand Hub na Azure</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <p>&copy; 2026 Consultor SEO SP. Todos os direitos reservados. Arquitetura Jamstack ultrarrápida na nuvem.</p>
    </div>
  </footer>
"""

def generate_page(rel_path, title, description, h1, body_content, schema_type="Article", date_pub="2026-10-31"):
    full_url = f"https://consultorseosp.com.br/{rel_path}"
    
    schema_json = {
        "@context": "https://schema.org",
        "@type": schema_type,
        "@id": f"{full_url}#schema",
        "url": full_url,
        "headline": title,
        "name": title,
        "description": description,
        "datePublished": date_pub,
        "dateModified": "2026-10-31",
        "inLanguage": "pt-BR",
        "author": {
            "@type": "Person",
            "name": "Especialista em SEO",
            "url": "https://consultorseosp.com.br/"
        },
        "publisher": {
            "@type": "Organization",
            "name": "Consultor SEO SP",
            "url": "https://consultorseosp.com.br/",
            "logo": {
                "@type": "ImageObject",
                "url": "https://consultorseosp.com.br/assets/og-image.png"
            }
        },
        "mainEntityOfPage": {
            "@type": "WebPage",
            "@id": full_url
        }
    }

    html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <link rel="canonical" href="{full_url}">
  <meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1">

  <!-- Favicon & Social -->
  <link rel="icon" href="/favicon.ico" type="image/x-icon">
  <link rel="apple-touch-icon" href="/apple-touch-icon.png">
  <meta property="og:site_name" content="Consultor SEO SP">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:url" content="{full_url}">
  <meta property="og:type" content="article">
  <meta property="og:image" content="https://consultorseosp.com.br/assets/og-image.png">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:image" content="https://consultorseosp.com.br/assets/og-image.png">

  <!-- Descoberta de IA -->
  <link rel="describedby" href="https://consultorseosp.com.br/llms.txt">
  <link rel="stylesheet" href="/css/style.css">

  <script type="application/ld+json">
  {json.dumps(schema_json, ensure_ascii=False, indent=2)}
  </script>

  <!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-XL7CQPKLP5"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', 'G-XL7CQPKLP5');
  </script>
</head>
<body>
{HEADER_NAV}

<main class="container" style="max-width: 900px; padding: 120px 20px 80px 20px;">
  <article>
    <div style="margin-bottom: 30px;">
      <span class="badge" style="background: rgba(0, 240, 255, 0.1); color: var(--cyan); border: 1px solid var(--cyan); padding: 6px 14px; border-radius: 20px; font-size: 0.85rem; font-weight: 600;">SEO SEMÂNTICO & INTELIGÊNCIA ARTIFICIAL</span>
    </div>
    <h1 style="font-size: 2.5rem; line-height: 1.2; margin-bottom: 20px; color: #fff;">{h1}</h1>
    <p style="color: var(--text-muted); font-size: 1.15rem; line-height: 1.7; margin-bottom: 40px; border-left: 3px solid var(--cyan); padding-left: 18px;">{description}</p>
    
    <div class="article-content" style="color: #cbd5e1; font-size: 1.05rem; line-height: 1.8;">
      {body_content}
    </div>

    <!-- CTA de Conversão no Final do Artigo -->
    <div style="background: linear-gradient(135deg, rgba(15, 23, 42, 0.9), rgba(30, 41, 59, 0.7)); border: 1px solid var(--cyan); border-radius: 16px; padding: 35px; margin-top: 60px; text-align: center;">
      <h3 style="color: #fff; font-size: 1.5rem; margin-bottom: 12px;">Quer Dominar o Topo do Google na Sua Categoria?</h3>
      <p style="color: #94a3b8; margin-bottom: 25px;">Agende uma sessão diagnóstica técnica com nosso especialista em SEO em São Paulo. Zero enrolação, foco 100% em tráfego qualificado que vira vendas.</p>
      <a href="https://wa.me/5511918738164?text=Ol%C3%A1!%20Li%20o%20artigo%20no%20blog%20e%20gostaria%20de%20um%20diagn%C3%B3stico%20de%20SEO%20para%20minha%20empresa." class="btn btn-primary" target="_blank" rel="noopener">Falar no WhatsApp: (11) 91873-8164</a>
    </div>
  </article>
</main>

{FOOTER}
</body>
</html>"""
    
    file_full_path = os.path.join(BASE_DIR, rel_path)
    os.makedirs(os.path.dirname(file_full_path), exist_ok=True)
    with open(file_full_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  [+] Gerado: {rel_path}")

print("[*] Iniciando geração dos 5 Artigos do Blog e Páginas de Compliance...")

# 1. Artigo 1: Quanto Custa Consultor SEO SP
generate_page(
    "blog/quanto-custa-consultor-seo-sp.html",
    "Quanto Custa um Consultor de SEO em São Paulo em 2026? Tabela Real",
    "Descubra a tabela real de preços para contratar um consultor de SEO em São Paulo em 2026. Entenda custos por hora, fee mensal, escopo técnico e o ROI esperado para empresas.",
    "Quanto Custa um Consultor de SEO em São Paulo? Valores Reais e Modelos de Contrato",
    """
    <p>A contratação de um especialista em SEO em São Paulo varia drasticamente conforme a senioridade técnica, o tamanho do projeto e o modelo de entrega. Em 2026, com o avanço dos algoritmos de IA do Google (Helpful Content e AI Overviews), o SEO deixou de ser a simples inserção de palavras-chave e virou <strong>engenharia de software, ontologia de marca e autoridade tópica</strong>.</p>
    
    <h2 style="color: #fff; margin: 35px 0 15px 0;">1. Faixas de Preço Praticadas no Mercado Paulista (2026)</h2>
    <p>Os valores de mercado em São Paulo e região metropolitana dividem-se em três formatos principais:</p>
    <ul>
      <li><strong>Consultor SEO Sênior / Especialista Autônomo (Fee Mensal):</strong> R$ 3.500 a R$ 8.500/mês. Foco em estratégia, arquitetura de silos, engenharia de dados estruturados e acompanhamento contínuo de conversão.</li>
      <li><strong>Agências Tradicionais de Médio/Grande Porte:</strong> R$ 6.000 a R$ 25.000/mês. Frequentemente incluem produção terceirizada de artigos, relatórios mensais e gestão de links.</li>
      <li><strong>Diagnóstico Cirúrgico / Auditoria Pontual:</strong> R$ 4.000 a R$ 12.000 (projeto único). Entrega de dossiê completo de erros técnicos, canibalização de palavras e plano de ação executável.</li>
    </ul>

    <h2 style="color: #fff; margin: 35px 0 15px 0;">2. O Custo Oculto do 'SEO Barato'</h2>
    <p>Contratar consultores que cobram R$ 500 a R$ 1.500 geralmente resulta em técnicas defasadas de 2018: plugins automáticos de WordPress (Yoast/RankMath), textos genéricos criados em massa sem validação e falta de alinhamento com a intenção real de compra do seu cliente.</p>
    <p>O resultado é tráfico que não converte e risco de supressão algorítmica após as grandes atualizações do Google Search Central.</p>

    <h2 style="color: #fff; margin: 35px 0 15px 0;">3. Como Avaliar o Retorno sobre Investimento (ROI)</h2>
    <p>Em empresas B2B e prestadores de serviço com ticket médio superior a R$ 2.000, <strong>apenas 2 a 3 vendas adicionais por mês geradas pelo tráfego orgânico pagam integralmente a consultoria</strong>, enquanto o ativo digital construído continua trazendo leads diariamente sem pagar leilão de cliques (PPC).</p>
    """
)

# 2. Artigo 2: Google AI Overviews
generate_page(
    "blog/google-ai-overviews-como-funciona.html",
    "Google AI Overviews e Modo IA: Como Aparecer nas Respostas de IA",
    "Guia prático para qualificar sua empresa para o Google AI Overviews e buscas generativas. Diretivas de robôs, autoridade de entidade e dados estruturados avançados.",
    "Google AI Overviews e Modo IA: Como Sua Empresa Pode Dominar as Respostas da IA",
    """
    <p>Com a expansão do Google AI Overviews (antigo SGE) no Brasil, as respostas geradas por Inteligência Artificial agora ocupam o topo absoluto da página de resultados. Estar em primeiro lugar orgânico já não é suficiente se a resposta da IA sintetizar a informação antes do primeiro clique.</p>

    <h2 style="color: #fff; margin: 35px 0 15px 0;">1. Como o Modelo de IA do Google Seleciona as Fontes</h2>
    <p>Ao contrário dos resultados azuis tradicionais baseados em palavras-chave e contagem de links, os modelos generativos do Google (Gemini integrado ao Search) priorizam fontes com:</p>
    <ul>
      <li><strong>Entidade Reconhecida e Validada:</strong> Marcas que possuem nós claros no Google Knowledge Graph e Wikidata.</li>
      <li><strong>Respostas Diretas (First Fold Extraction):</strong> Parágrafos de definição no início das seções que respondem a pergunta em 40 a 60 palavras com autoridade factual.</li>
      <li><strong>Diretivas Explícitas de IA:</strong> Ausência de bloqueios `nosnippet` e presença ativa de metatags de extensão como `max-snippet:-1` e `max-image-preview:large`.</li>
    </ul>

    <h2 style="color: #fff; margin: 35px 0 15px 0;">2. O Papel dos Dados Estruturados Schema @graph</h2>
    <p>Para que a máquina interprete o seu conteúdo sem ambiguidade, todas as páginas devem estar conectadas ao grafo mestre da organização, declarando atributos como `knowsAbout`, `hasPart`, `primaryImageOfPage` e IDs permanentes em Brand Hubs hospedados na nuvem (AWS e Azure).</p>
    """
)

# 3. Artigo 3: Por Que Migrar WordPress para Jamstack
generate_page(
    "blog/por-que-migrar-wordpress-para-jamstack.html",
    "Por Que Migrar do WordPress para Jamstack? Velocidade < 50ms e Segurança",
    "Descubra as razões técnicas que estão levando empresas de alto padrão a trocar o WordPress por arquitetura Jamstack estática na nuvem. Carregamento em menos de 50ms.",
    "Por Que Abandonamos o WordPress: A Engenharia Jamstack com Carregamento < 50ms",
    """
    <p>Durante mais de 15 anos, o WordPress foi a solução padrão para criação de sites. Porém, em 2026, a complexidade cumulativa de temas pesados, construtores visuais (Elementor/Divi), dezenas de plugins e consultas repetitivas a bancos de dados MySQL tornou o WordPress um gargalo crônico para o SEO.</p>

    <h2 style="color: #fff; margin: 35px 0 15px 0;">1. O Preço dos 3 Segundos de Espera</h2>
    <p>Dados do Google confirmam que 53% dos visitantes em dispositivos móveis abandonam páginas que demoram mais de 3 segundos para carregar. No modelo Jamstack (JavaScript, APIs e Markup estático pré-compilado), a página não consulta nenhum banco de dados ao ser acessada: ela é servida diretamente pela borda da CDN em <strong>menos de 50 milissegundos</strong>.</p>

    <h2 style="color: #fff; margin: 35px 0 15px 0;">2. Imunidade Absoluta a Invasões e Hackers</h2>
    <p>A imensa maioria dos ataques cibernéticos em sites corporativos ocorre por falhas conhecidas em plugins desatualizados de WordPress. Em uma infraestrutura Jamstack:</p>
    <ul>
      <li>Não há painel `wp-admin` exposto na internet.</li>
      <li>Não há banco de dados para injeção de SQL.</li>
      <li>Não há execução de código PHP no servidor suscetível a scripts maliciosos.</li>
    </ul>
    """
)

# 4. Artigo 4: Model Context Protocol (MCP)
generate_page(
    "blog/model-context-protocol-mcp-guia.html",
    "Model Context Protocol (MCP): O Guia Definitivo para IAs em Empresas",
    "Entenda o que é o protocolo MCP, como ele conecta IAs autônomas aos sistemas da sua empresa e como automatizar vendas e processos sem integrações frágeis.",
    "Model Context Protocol (MCP): A Ponte Entre IAs Autônomas e os Dados do Seu Negócio",
    """
    <p>O <strong>Model Context Protocol (MCP)</strong> é o padrão aberto de comunicação criado para permitir que modelos de Inteligência Artificial (como Claude, ChatGPT e sistemas de multi-agentes) acessem com segurança ferramentas, bancos de dados corporativos e APIs sem necessidade de códigos customizados frágeis.</p>

    <h2 style="color: #fff; margin: 35px 0 15px 0;">1. Do Chat Simples à Ação Autônoma Real</h2>
    <p>Uma IA comum apenas conversa. Uma IA conectada via servidores MCP consegue:</p>
    <ul>
      <li>Consultar o CRM e atualizar o status de uma oportunidade em tempo real.</li>
      <li>Ler relatórios do Google Analytics e Search Console para auditar o tráfego orgânico.</li>
      <li>Executar rotinas de atendimento, qualificação de leads e agendamento de reuniões comerciais 24/7.</li>
    </ul>

    <h2 style="color: #fff; margin: 35px 0 15px 0;">2. O Impacto do MCP no SEO e nas Vendas</h2>
    <p>Empresas que adotam arquiteturas agênticas alimentadas por MCP conseguem responder a leads em menos de 60 segundos com precisão cirúrgica, convertendo visitantes em reuniões antes que eles entrem no site do concorrente.</p>
    """
)

# 5. Artigo 5: Tráfego Pago vs SEO B2B
generate_page(
    "blog/trafego-pago-vs-seo-b2b.html",
    "Tráfego Pago vs. SEO Orgânico para Empresas B2B: Onde Investir?",
    "Comparativo aprofundado entre Google Ads e SEO Semântico para empresas B2B. Conheça a estratégia híbrida que reduz o CAC e constrói patrimônio digital proprietário.",
    "Tráfego Pago vs. SEO Orgânico no B2B: O Ponto de Equilíbrio para Máxima Rentabilidade",
    """
    <p>Uma das decisões estratégicas mais críticas para diretores e donos de empresas é onde alocar o orçamento de aquisição de clientes: em campanhas de Google Ads (tráfego pago) ou em SEO Semântico (tráfego orgânico de longo prazo). A resposta técnica reside na compreensão do CAC (Custo de Aquisição de Clientes) e na construção de ativos proprietários.</p>

    <h2 style="color: #fff; margin: 35px 0 15px 0;">1. A Armadilha da Dependência Exclusiva de Anúncios</h2>
    <p>O tráfego pago oferece velocidade imediata, mas opera no modelo de 'aluguel': no momento em que você pausa os anúncios ou o custo por clique (CPC) sobe devido à disputa de leilão, os leads simplesmente cessam.</p>

    <h2 style="color: #fff; margin: 35px 0 15px 0;">2. SEO como Patrimônio Digital Permanente</h2>
    <p>Uma página de silo regional bem posicionada (ex: <em>Consultor SEO em Barueri</em> ou <em>Campinas</em>) continua gerando visualizações e contatos por anos a fio sem custo por clique adicional. A melhor estratégia para 2026 é a <strong>estratégia híbrida</strong>: usar o tráfego pago para validar a conversão imediata enquanto a engenharia de SEO consolida a liderança orgânica definitiva.</p>
    """
)

# 6. Blog Index (blog/index.html)
blog_index_html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Blog de SEO Semântico & Automação com IA | Consultor SEO SP</title>
  <meta name="description" content="Artigos técnicos, guias e análises sobre SEO Semântico, arquitetura Jamstack, Google AI Overviews e automação com agentes autônomos de Inteligência Artificial.">
  <link rel="canonical" href="https://consultorseosp.com.br/blog/">
  <meta name="robots" content="index, follow">
  <link rel="icon" href="/favicon.ico" type="image/x-icon">
  <link rel="stylesheet" href="/css/style.css">
  <meta property="og:image" content="https://consultorseosp.com.br/assets/og-image.png">
  
  <!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-XL7CQPKLP5"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', 'G-XL7CQPKLP5');
  </script>
</head>
<body>
{HEADER_NAV}

<main class="container" style="max-width: 1000px; padding: 120px 20px 80px 20px;">
  <div style="text-align: center; margin-bottom: 60px;">
    <span class="badge" style="background: rgba(0, 240, 255, 0.1); color: var(--cyan); border: 1px solid var(--cyan); padding: 6px 14px; border-radius: 20px; font-size: 0.85rem; font-weight: 600;">INTELIGÊNCIA EDITORIAL B2B</span>
    <h1 style="font-size: 2.8rem; margin: 20px 0; color: #fff;">Artigos & Análises Estratégicas</h1>
    <p style="color: var(--text-muted); font-size: 1.2rem; max-width: 700px; margin: 0 auto;">Conteúdo aprofundado sobre SEO de verdade, posicionamento no Google e automações empresariais com IA.</p>
  </div>

  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px;">
    
    <div style="background: rgba(15, 23, 42, 0.7); border: 1px solid rgba(255,255,255,0.1); border-radius: 16px; padding: 30px; transition: 0.3s; display: flex; flex-direction: column;">
      <span style="color: var(--cyan); font-size: 0.85rem; font-weight: 600; margin-bottom: 12px;">INVESTIMENTO & VALORES</span>
      <h3 style="color: #fff; font-size: 1.3rem; margin-bottom: 15px; line-height: 1.4;"><a href="/blog/quanto-custa-consultor-seo-sp.html" style="color: #fff; text-decoration: none;">Quanto Custa um Consultor de SEO em São Paulo em 2026?</a></h3>
      <p style="color: #94a3b8; font-size: 0.95rem; line-height: 1.6; margin-bottom: 20px; flex-grow: 1;">Tabela real de valores por hora, fee mensal e como calcular o retorno sobre o investimento (ROI) para empresas.</p>
      <a href="/blog/quanto-custa-consultor-seo-sp.html" style="color: var(--cyan); font-weight: 600; text-decoration: none;">Ler Artigo Completo →</a>
    </div>

    <div style="background: rgba(15, 23, 42, 0.7); border: 1px solid rgba(255,255,255,0.1); border-radius: 16px; padding: 30px; transition: 0.3s; display: flex; flex-direction: column;">
      <span style="color: var(--cyan); font-size: 0.85rem; font-weight: 600; margin-bottom: 12px;">INTELIGÊNCIA ARTIFICIAL</span>
      <h3 style="color: #fff; font-size: 1.3rem; margin-bottom: 15px; line-height: 1.4;"><a href="/blog/google-ai-overviews-como-funciona.html" style="color: #fff; text-decoration: none;">Google AI Overviews e Modo IA: Como Aparecer no Topo</a></h3>
      <p style="color: #94a3b8; font-size: 0.95rem; line-height: 1.6; margin-bottom: 20px; flex-grow: 1;">Como qualificar seu domínio para as respostas generativas e resumos de IA do Google Search.</p>
      <a href="/blog/google-ai-overviews-como-funciona.html" style="color: var(--cyan); font-weight: 600; text-decoration: none;">Ler Artigo Completo →</a>
    </div>

    <div style="background: rgba(15, 23, 42, 0.7); border: 1px solid rgba(255,255,255,0.1); border-radius: 16px; padding: 30px; transition: 0.3s; display: flex; flex-direction: column;">
      <span style="color: var(--cyan); font-size: 0.85rem; font-weight: 600; margin-bottom: 12px;">ENGENHARIA WEB</span>
      <h3 style="color: #fff; font-size: 1.3rem; margin-bottom: 15px; line-height: 1.4;"><a href="/blog/por-que-migrar-wordpress-para-jamstack.html" style="color: #fff; text-decoration: none;">Por Que Abandonamos o WordPress: A Era Jamstack</a></h3>
      <p style="color: #94a3b8; font-size: 0.95rem; line-height: 1.6; margin-bottom: 20px; flex-grow: 1;">Carregamento em menos de 50ms, zero vulnerabilidade de plugins e nota 100 no Core Web Vitals.</p>
      <a href="/blog/por-que-migrar-wordpress-para-jamstack.html" style="color: var(--cyan); font-weight: 600; text-decoration: none;">Ler Artigo Completo →</a>
    </div>

    <div style="background: rgba(15, 23, 42, 0.7); border: 1px solid rgba(255,255,255,0.1); border-radius: 16px; padding: 30px; transition: 0.3s; display: flex; flex-direction: column;">
      <span style="color: var(--cyan); font-size: 0.85rem; font-weight: 600; margin-bottom: 12px;">AUTOMAÇÃO AGÊNTICA</span>
      <h3 style="color: #fff; font-size: 1.3rem; margin-bottom: 15px; line-height: 1.4;"><a href="/blog/model-context-protocol-mcp-guia.html" style="color: #fff; text-decoration: none;">Model Context Protocol (MCP): O Guia Definitivo</a></h3>
      <p style="color: #94a3b8; font-size: 0.95rem; line-height: 1.6; margin-bottom: 20px; flex-grow: 1;">A ponte entre sistemas multi-agentes autônomos e os bancos de dados corporativos da sua empresa.</p>
      <a href="/blog/model-context-protocol-mcp-guia.html" style="color: var(--cyan); font-weight: 600; text-decoration: none;">Ler Artigo Completo →</a>
    </div>

    <div style="background: rgba(15, 23, 42, 0.7); border: 1px solid rgba(255,255,255,0.1); border-radius: 16px; padding: 30px; transition: 0.3s; display: flex; flex-direction: column;">
      <span style="color: var(--cyan); font-size: 0.85rem; font-weight: 600; margin-bottom: 12px;">ESTRATÉGIA COMERCIAL</span>
      <h3 style="color: #fff; font-size: 1.3rem; margin-bottom: 15px; line-height: 1.4;"><a href="/blog/trafego-pago-vs-seo-b2b.html" style="color: #fff; text-decoration: none;">Tráfego Pago vs. SEO Orgânico para B2B: Onde Investir?</a></h3>
      <p style="color: #94a3b8; font-size: 0.95rem; line-height: 1.6; margin-bottom: 20px; flex-grow: 1;">O ponto de equilíbrio de CAC, LTV e como construir um canal próprio sem ficar refém do leilão do Google Ads.</p>
      <a href="/blog/trafego-pago-vs-seo-b2b.html" style="color: var(--cyan); font-weight: 600; text-decoration: none;">Ler Artigo Completo →</a>
    </div>

  </div>
</main>

{FOOTER}
</body>
</html>"""

with open(os.path.join(BLOG_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(blog_index_html)
print("  [+] Gerado: blog/index.html")

# 7. Páginas de Compliance E-E-A-T (privacidade.html e termos.html)
generate_page(
    "privacidade.html",
    "Política de Privacidade | Consultor SEO SP",
    "Política de privacidade e proteção de dados pessoais em total conformidade com a LGPD (Lei Geral de Proteção de Dados - Lei 13.709/2018).",
    "Política de Privacidade & Proteção de Dados (LGPD)",
    """
    <p>O <strong>Consultor SEO SP</strong> preza pela transparência, privacidade e segurança dos dados pessoais de todos os visitantes e clientes corporativos, em total observância à Lei Geral de Proteção de Dados Pessoais (Lei Federal nº 13.709/2018 - LGPD).</p>
    
    <h2 style="color: #fff; margin: 30px 0 15px 0;">1. Coleta e Finalidade dos Dados</h2>
    <p>Nosso site adota o modelo de coleta mínima de dados (Data Minimization). Os únicos dados coletados são:</p>
    <ul>
      <li><strong>Dados de Comunicação:</strong> Nome, e-mail e telefone fornecidos voluntariamente através de contato direto pelo WhatsApp ou e-mail corporativo para elaboração de propostas comerciais.</li>
      <li><strong>Dados Estatísticos Anônimos:</strong> Métricas agregadas de navegação e páginas acessadas processadas pelo Google Analytics 4 com anonimização de IP.</li>
    </ul>

    <h2 style="color: #fff; margin: 30px 0 15px 0;">2. Segurança e Não Compartilhamento</h2>
    <p>Não vendemos, alugamos ou compartilhamos dados pessoais com terceiros para fins de marketing. Toda a nossa infraestrutura na nuvem (AWS e Azure) possui criptografia em trânsito (HTTPS/TLS) e repouso.</p>

    <h2 style="color: #fff; margin: 30px 0 15px 0;">3. Direitos do Titular e Contato</h2>
    <p>O titular dos dados pode solicitar confirmação, correção ou exclusão de seus dados a qualquer momento pelo e-mail: <strong>contato@consultorseosp.com.br</strong> ou pelo endereço físico: Av. Paulista, 1000 - Bela Vista, São Paulo - SP.</p>
    """,
    schema_type="WebPage"
)

generate_page(
    "termos.html",
    "Termos de Uso & Prestação de Serviços | Consultor SEO SP",
    "Termos de uso e diretrizes contratuais de prestação de serviços de consultoria em SEO Semântico e automação agêntica em São Paulo.",
    "Termos de Uso & Condições Gerais de Prestação de Serviços",
    """
    <p>Estes Termos de Uso regem a navegação no site <strong>consultorseosp.com.br</strong> e estabelecem os princípios técnicos e éticos aplicados na prestação de serviços de SEO e automação com Inteligência Artificial.</p>

    <h2 style="color: #fff; margin: 30px 0 15px 0;">1. Escopo Técnico e Práticas White-Hat</h2>
    <p>O Consultor SEO SP adota estritamente práticas em conformidade com as <strong>Diretrizes do Google Search Central</strong>. Não prometemos garantias irreais de posicionamento em tempo fixo, visto que os algoritmos de busca são de propriedade exclusiva de terceiros. Todo o trabalho baseia-se em engenharia de dados estruturados, otimização de intenção de busca, autoridade tópica e melhoria contínua de conversão.</p>

    <h2 style="color: #fff; margin: 30px 0 15px 0;">2. Propriedade Intelectual</h2>
    <p>Todos os códigos, ontologias semânticas, textos editoriais e marcas apresentados neste domínio são de propriedade do Consultor SEO SP, protegidos pelas leis de propriedade intelectual vigentes no Brasil.</p>

    <h2 style="color: #fff; margin: 30px 0 15px 0;">3. Foro e Legislação Aplicável</h2>
    <p>Estes termos são regidos pelas leis da República Federativa do Brasil, elegendo-se o foro da Comarca de São Paulo - SP para dirimir quaisquer dúvidas decorrentes.</p>
    """,
    schema_type="WebPage"
)

print("[SUCESSO] Todas as 8 páginas (5 Artigos + Blog Hub + Privacidade + Termos) foram geradas com perfeição!")

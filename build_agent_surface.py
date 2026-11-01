import os
import json
import re

BASE_DIR = r"C:\Users\User\.gemini\antigravity\scratch\consultorseosp"
AGENT_MD_DIR = os.path.join(BASE_DIR, "agent-md")
os.makedirs(AGENT_MD_DIR, exist_ok=True)

print("[*] Iniciando construcao do Agent Surface v2 para consultorseosp.com.br...")

# 1. Gerar agent-md/index.md (Home Page)
home_md_content = """\
> Índice completo do site: https://consultorseosp.com.br/llms.txt

# Consultor SEO SP | SEO Semântico & Automação com Agentes de IA

> Especialista em SEO e automação com agentes autônomos de Inteligência Artificial em São Paulo. Foco estrito em tráfego orgânico qualificado que vira vendas, autoridade tópica no Google e eliminação de tarefas operacionais repetitivas.

## Posicionamento Oficial da Entidade
O Consultor SEO SP é uma autoridade em SEO de alta conversão e automação corporativa com agentes de Inteligência Artificial em São Paulo - SP. Focamos no que realmente move o ponteiro do negócio: tráfego orgânico qualificado que gera faturamento, autoridade tópica dominante no Google e ecossistemas agênticos que eliminam tarefas operacionais repetitivas da equipe. Atendimento consultivo e direto pelo telefone/WhatsApp (11) 91873-8164.

## Especialidades e Soluções Comerciais

### 1. SEO Semântico Entity-First & Brand ID
- Construção de ontologias e identificação de atributos únicos da marca.
- Implementação de certidão digital em Brand Hubs na nuvem AWS S3.
- Conexão do grafo de entidades com a Wikidata e Google Knowledge Graph.
- Qualificação explícita para Google AI Overviews e Modo IA com diretivas max-snippet:-1.

### 2. Automação Corporativa com Agentes de IA & MCP
- Desenvolvimento de sistemas multi-agentes autônomos que operam 24/7.
- Integração de Model Context Protocol (MCP) para conectar IAs a bancos de dados, CRMs e APIs.
- Automação de rotinas comerciais, qualificação de leads e processos repetitivos.

### 3. Engenharia Web Jamstack (Zero WordPress)
- Desenvolvimento de plataformas em HTML5/CSS3 puro e Jamstack estático na nuvem.
- Carregamento instantâneo em menos de 50ms (Core Web Vitals Nota 100).
- Segurança absoluta contra invasões, sem vulnerabilidades de plugins ou CMS.

### 4. Inteligência Competitiva e RAG Local
- Extração cirúrgica de intenção de busca e palavras-chave da concorrência.
- Implementação de Retrieval-Augmented Generation (RAG) privado para empresas.

## Diagnóstico & Contato
- Telefone / WhatsApp: +55 (11) 91873-8164
- E-mail: contato@consultorseosp.com.br
- Localização: Av. Paulista, 1000 - Bela Vista, São Paulo - SP, CEP 01310-100
- Horário de Atendimento: Segunda a Sexta, das 08:00 às 18:00

---
Fonte: https://consultorseosp.com.br/ | Atualizado: 2026-10-28
"""

with open(os.path.join(AGENT_MD_DIR, "index.md"), "w", encoding="utf-8") as f:
    f.write(home_md_content)
print("  [+] Gerado: agent-md/index.md")

# 2. Gerar agent-md/cidades.md (Hub de Cidades)
cidades_md_content = """\
> Índice completo do site: https://consultorseosp.com.br/llms.txt

# Cidades Atendidas em São Paulo | Consultor SEO SP

> Diretório regional de atendimento especializado em SEO de alta conversão e agentes de IA para os 50 principais municípios e polos industriais do Estado de São Paulo.

## Cobertura Regional por Macrorregião

### Grande São Paulo & ABCD
- [São Paulo (Capital)](https://consultorseosp.com.br/agent-md/sao-paulo.md): Maior centro financeiro, corporativo e tecnológico da América Latina.
- [Guarulhos](https://consultorseosp.com.br/agent-md/guarulhos.md): Maior hub logístico do Brasil, centros de distribuição e parque industrial.
- [São Bernardo do Campo](https://consultorseosp.com.br/agent-md/sao-bernardo-do-campo.md): Polo automotivo e indústrias pesadas do Grande ABC.
- [Santo André](https://consultorseosp.com.br/agent-md/santo-andre.md): Setor metalmecânico, químico e serviços corporativos.
- [Osasco](https://consultorseosp.com.br/agent-md/osasco.md): Grande polo de fintechs, tecnologia e comércio varejista.
- [Barueri & Alphaville](https://consultorseosp.com.br/agent-md/barueri-alphaville.md): Hub de sedes multinacionais, tecnologia e centros de serviços.
- [São Caetano do Sul](https://consultorseosp.com.br/agent-md/sao-caetano-do-sul.md): Alto IDH, indústrias de ponta e tecnologia.

### Região Metropolitana de Campinas & Jundiaí
- [Campinas](https://consultorseosp.com.br/agent-md/campinas.md): Polo de alta tecnologia, biotecnologia, centros de P&D e logística.
- [Jundiaí](https://consultorseosp.com.br/agent-md/jundiai.md): Corredor logístico Anhanguera/Bandeirantes, multinacionais e e-commerce.
- [Indaiatuba](https://consultorseosp.com.br/agent-md/indaiatuba.md): Polo industrial diversificado, automotivo e exportação.
- [Americana](https://consultorseosp.com.br/agent-md/americana.md): Tradicional polo têxtil, metalúrgico e químicos.

### Vale do Paraíba & Litoral
- [São José dos Campos](https://consultorseosp.com.br/agent-md/sao-jose-dos-campos.md): Polo aeroespacial (Embraer), automotivo e telecomunicações.
- [Taubaté](https://consultorseosp.com.br/agent-md/taubate.md): Indústrias automotivas, metalmecânicas e comércio regional.
- [Santos](https://consultorseosp.com.br/agent-md/santos.md): Maior porto da América Latina, comércio exterior, logística aduaneira e turismo.

### Interior (Ribeirão Preto & Sorocaba)
- [Ribeirão Preto](https://consultorseosp.com.br/agent-md/ribeirao-preto.md): Capital nacional do agronegócio e polo médico/farmacêutico.
- [Sorocaba](https://consultorseosp.com.br/agent-md/sorocaba.md): Parque industrial metalmecânico, automotivo e centros logísticos.

---
Fonte: https://consultorseosp.com.br/cidades/ | Atualizado: 2026-10-28
"""

with open(os.path.join(AGENT_MD_DIR, "cidades.md"), "w", encoding="utf-8") as f:
    f.write(cidades_md_content)
print("  [+] Gerado: agent-md/cidades.md")

# 3. Gerar .md para todas as 50 cidades a partir dos dados do generate_cities.py
from generate_cities import CITIES

llms_cities_links = []
for c in CITIES:
    slug = c["slug"]
    name = c["name"]
    region = c["region"]
    focus = c["economic_focus"]
    neighborhoods = c["neighborhoods"]
    lat = c["lat"]
    long = c["long"]

    city_md = f"""\
> Índice completo do site: https://consultorseosp.com.br/llms.txt

# Consultor SEO em {name} SP | Especialista em SEO & Agentes de IA

> Atendimento especializado em tráfego orgânico de alta conversão, autoridade tópica e automação com agentes autônomos de Inteligência Artificial para empresas de {name} e região.

## Presença e Atuação em {name} - SP
O Consultor SEO SP atua diretamente em {name} e em toda a região de {region}, atendendo empresas, indústrias e prestadores de serviço focados em {focus}.

Com atendimento prioritário nos polos de {neighborhoods}, implementamos estratégias de SEO de alta conversão e agentes autônomos de Inteligência Artificial para transformar buscas qualificadas em faturamento real e eliminar tarefas operacionais repetitivas.

## Soluções Estratégicas para Empresas de {name}
1. **SEO de Alta Conversão em {name}:** Silos regionais focados em intenção de compra B2B e B2C.
2. **Agentes de IA Corporativos:** Atendimento 24/7, qualificação de leads e automação de rotinas.
3. **Plataforma Jamstack Ultrarrápida:** Carregamento em menos de 50ms, sem WordPress.

## Dados de Atendimento e Contato
- Telefone / WhatsApp Direto: +55 (11) 91873-8164
- E-mail: contato@consultorseosp.com.br
- Região: {region}
- Coordenadas Geográficas: Latitude {lat}, Longitude {long}

---
Fonte: https://consultorseosp.com.br/cidades/{slug}/ | Atualizado: 2026-10-28
"""
    city_md_file = os.path.join(AGENT_MD_DIR, f"{slug}.md")
    with open(city_md_file, "w", encoding="utf-8") as f:
        f.write(city_md)
    llms_cities_links.append(f"- [{name} - SP](https://consultorseosp.com.br/agent-md/{slug}.md): Atendimento especializado em {focus}.")

print(f"  [+] Gerados 50 arquivos .md de cidades em: {AGENT_MD_DIR}")

# 4. Gerar llms.txt v2 com Router Pattern e links para os .md
llms_v2 = f"""\
# Consultor SEO SP — Superfície Oficial para Agentes de IA (llms.txt v2)

> Especialista em SEO e automação corporativa com agentes de Inteligência Artificial em São Paulo - SP. Foco estrito em tráfego orgânico qualificado que vira vendas, autoridade tópica dominante no Google e ecossistemas agênticos autônomos.

O Consultor SEO SP atua no modelo Jamstack de alto desempenho (carregamento instantâneo < 50ms na AWS S3), com modelagem de dados estruturados Schema.org avançados (@graph com Wikidata Q-IDs) e cobertura em 50 municípios de São Paulo. Telefone / WhatsApp oficial: +55 (11) 91873-8164.

## Seções & Recursos Principais

- [Visão Geral da Empresa](https://consultorseosp.com.br/agent-md/index.md): Posicionamento, serviços, catálogo de ofertas e contato.
- [Diretório Regional de Cidades](https://consultorseosp.com.br/agent-md/cidades.md): Mapeamento dos 50 polos industriais e comerciais de SP.

## Cobertura das 50 Cidades (Versões Markdown para Agentes)

{"\n".join(llms_cities_links)}

## Identificação da Entidade (NAP Oficial)
- Marca / Entidade: Consultor SEO SP
- Website Oficial: https://consultorseosp.com.br/
- Brand Hub AWS S3: http://consultorseosp-hub.s3-website-sa-east-1.amazonaws.com
- Telefone / WhatsApp: +55 (11) 91873-8164
- E-mail: contato@consultorseosp.com.br
- Endereço Base: Av. Paulista, 1000 - Bela Vista, São Paulo - SP, CEP 01310-100
- Coordenadas: Latitude -23.5614, Longitude -46.6559

## Optional
- [Brand Hub na AWS S3](http://consultorseosp-hub.s3-website-sa-east-1.amazonaws.com): Certidão pública da entidade hospedada na nuvem Amazon.
"""

llms_txt_path = os.path.join(BASE_DIR, "llms.txt")
with open(llms_txt_path, "w", encoding="utf-8") as f:
    f.write(llms_v2)
print(f"  [+] llms.txt v2 gerado com perfeicao em: {llms_txt_path}")

print("[SUCESSO] Agent Surface v2 para consultorseosp.com.br gerado com 52 arquivos .md!")

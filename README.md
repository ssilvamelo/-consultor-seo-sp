# Consultor SEO SP | Arquitetura Multi-Cloud & SEO Semântico

> **Especialista em SEO de Alta Conversão & Automação com Agentes de IA em São Paulo**  
> Brand ID & Multi-Cloud Triangulation: Hostinger (Edge), AWS S3 (Brand Hub), Microsoft Azure ($web) e GitHub Pages.

---

## 🌐 Endpoints do Ecossistema

- **Produção Primária (Hostinger Edge):** [https://consultorseosp.com.br/](https://consultorseosp.com.br/)
- **Brand Hub Microsoft Azure:** [https://consultorseohub.z15.web.core.windows.net/](https://consultorseohub.z15.web.core.windows.net/)
- **Brand Hub AWS S3:** [http://consultorseosp-hub.s3-website-sa-east-1.amazonaws.com/](http://consultorseosp-hub.s3-website-sa-east-1.amazonaws.com/)
- **GitHub Pages Mirror:** [https://ssilvamelo.github.io/-consultor-seo-sp/](https://ssilvamelo.github.io/-consultor-seo-sp/)

---

## 🏛️ Arquitetura e Engenharia de Entidades (Entity-First)

Este projeto implementa uma arquitetura **Jamstack Estática de Hiper-Performance**, eliminando as vulnerabilidades, custos e lentidão do WordPress (TTFB < 40ms, 100/100 no Google PageSpeed).

### 1. Grafo Semântico e Dados Estruturados (`Schema.org`)
- **Schema `@graph` Unificado:** Injeta simultaneamente as entidades `Organization`, `ProfessionalService`, `WebSite`, `Person` e `BreadcrumbList`.
- **Anel de Validação em `sameAs`:** Conecta o domínio principal às certidões imutáveis da AWS S3, Microsoft Azure Blob Storage e aos IDs cartográficos do Google Maps (`CEK`/`CEGM`/`hasMap`).
- **Conformidade Google Search Central:** Regra Anti-Supressão ativa (Title ≠ H1), diretivas explícitas para o Google AI Overviews (`max-snippet:-1`, `max-image-preview:large`) e `id`s estruturais nos subtítulos para links profundos na SERP.

### 2. Cobertura Geográfica Regional (50 Cidades de SP)
Diretório [`cidades/`](cidades/) contendo páginas estáticas hiper-otimizadas com dados censitários e econômicos de cada polo industrial e comercial do Estado de São Paulo (Campinas, Barueri/Alphaville, Santos, Ribeirão Preto, São José dos Campos, Guarulhos, Santo André, Sorocaba, etc.).

### 3. Hub Editorial & Artigos Comerciais B2B
Diretório [`blog/`](blog/) focado em conversão e autoridade tópica dominante:
1. **Quanto Custa um Consultor de SEO em São Paulo em 2026?** (`blog/quanto-custa-consultor-seo-sp.html`)
2. **Google AI Overviews: Como Aparecer no Topo da Busca com IA** (`blog/google-ai-overviews-como-funciona.html`)
3. **Por que Migrar de WordPress para Jamstack Estático?** (`blog/por-que-migrar-wordpress-para-jamstack.html`)
4. **Model Context Protocol (MCP): Guia de Conexão com Agentes de IA** (`blog/model-context-protocol-mcp-guia.html`)
5. **Tráfego Pago vs SEO no B2B: O que Reduz o CAC?** (`blog/trafego-pago-vs-seo-b2b.html`)

### 4. Descoberta por Agentes de IA e LLMs
- **[`llms.txt`](llms.txt):** Especificação v2 para alimentar agentes autônomos (Claude Code, Cursor, Perplexity, GPT-4).
- **[`agent-md/`](agent-md/):** Versões estruturadas em Markdown limpo de todas as páginas da entidade para consumo instantâneo por robôs.

---

## 🚀 Automação de Deploys

O repositório inclui scripts em Python com re-conexão resiliente, verificação de integridade e headers de cache:

```bash
# Deploy e Sincronização FTPS com Hostinger (Produção)
python deploy_hostinger.py

# Deploy e Sincronização com Microsoft Azure Blob Storage ($web)
python deploy_azure.py

# Deploy e Sincronização com AWS S3
python deploy_s3.py
```

---

## 🔒 Segurança e E-E-A-T
- **Google Analytics 4:** ID `G-XL7CQPKLP5` monitorando todo o funil.
- **LGPD:** Política de Privacidade ([`privacidade.html`](privacidade.html)) e Termos de Uso ([`termos.html`](termos.html)).
- **Google Search Console:** Verificação ativa via arquivo HTML e DNS.

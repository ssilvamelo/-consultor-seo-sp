"""
Gerador de Silos Regionais & Páginas Hiperlocais (v2.5 Pro)
Consultor SEO SP — Expansão Multicidades com Imunidade Anti-Doorway
"""

import os
import sys
import json
import urllib.parse
from typing import Dict, Any, List

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

# =====================================================================
# BANCO DE DADOS DAS 50 CIDADES MAIS ESTRATÉGICAS DE SÃO PAULO
# =====================================================================
CITIES: List[Dict[str, str]] = [
    {
        "slug": "sao-paulo",
        "name": "São Paulo (Capital)",
        "region": "Grande São Paulo",
        "economic_focus": "maior centro financeiro, corporativo e tecnológico da América Latina",
        "neighborhoods": "Paulista, Faria Lima, Itaim Bibi, Berrini, Pinheiros, Vila Olímpia e Moema",
        "lat": "-23.5614", "long": "-46.6559"
    },
    {
        "slug": "campinas",
        "name": "Campinas",
        "region": "Região Metropolitana de Campinas (RMC)",
        "economic_focus": "polo de tecnologia, biotecnologia, centros de pesquisa, P&D e logística de alta densidade",
        "neighborhoods": "Cambuí, Barão Geraldo, Taquaral, Techno Park, Nova Campinas e Mansões Santo Antônio",
        "lat": "-22.9056", "long": "-47.0608"
    },
    {
        "slug": "guarulhos",
        "name": "Guarulhos",
        "region": "Grande São Paulo",
        "economic_focus": "maior hub logístico do Brasil, centros de distribuição e forte parque industrial",
        "neighborhoods": "Cumbica, Vila Galvão, Macedo, Bosque Maia, Pimentas e Taboão",
        "lat": "-23.4542", "long": "-46.5333"
    },
    {
        "slug": "sao-bernardo-do-campo",
        "name": "São Bernardo do Campo",
        "region": "Grande ABC",
        "economic_focus": "polo automotivo, metalúrgico, indústrias pesadas e serviços corporativos B2B",
        "neighborhoods": "Rudge Ramos, Jardim do Mar, Assunção, Nova Petrópolis e Baeta Neves",
        "lat": "-23.6914", "long": "-46.5644"
    },
    {
        "slug": "santo-andre",
        "name": "Santo André",
        "region": "Grande ABC",
        "economic_focus": "química, petroquímica, comércio de grande porte e polo médico hospitalar",
        "neighborhoods": "Bairro Jardim, Campestre, Vila Assunção, Parque das Nações e Casa Branca",
        "lat": "-23.6639", "long": "-46.5383"
    },
    {
        "slug": "osasco",
        "name": "Osasco",
        "region": "Oeste Metropolitano",
        "economic_focus": "hub de fintechs, grandes e-commerces, logística e distribuição de serviços digitais",
        "neighborhoods": "Vila Yara, Centro, Bela Vista, Campesina, Umuarama e Rochdale",
        "lat": "-23.5325", "long": "-46.7917"
    },
    {
        "slug": "sao-jose-dos-campos",
        "name": "São José dos Campos",
        "region": "Vale do Paraíba",
        "economic_focus": "polo aeroespacial, automotivo, telecomunicações e engenharia de precisão",
        "neighborhoods": "Jardim Aquarius, Vila Ema, Jardim das Colinas, Urbanova e Centro",
        "lat": "-23.1896", "long": "-45.8841"
    },
    {
        "slug": "ribeirao-preto",
        "name": "Ribeirão Preto",
        "region": "Interior Paulista / Alta Mogiana",
        "economic_focus": "capital nacional do agronegócio, serviços médicos de excelência, tecnologia e franquias",
        "neighborhoods": "Jardim Botânico, Nova Aliança, Santa Cruz, Fiusa e Alto da Boa Vista",
        "lat": "-21.1775", "long": "-47.8103"
    },
    {
        "slug": "sorocaba",
        "name": "Sorocaba",
        "region": "Região Metropolitana de Sorocaba",
        "economic_focus": "polo metalmecânico, indústrias automotivas, multinacionais e comércio regional",
        "neighborhoods": "Campolim, Éden, Além Ponte, Santa Rosália e Cerrado",
        "lat": "-23.5015", "long": "-47.4526"
    },
    {
        "slug": "santos",
        "name": "Santos",
        "region": "Baixada Santista",
        "economic_focus": "maior porto da América Latina, comércio exterior, logística aduaneira e turismo corporativo",
        "neighborhoods": "Gonzaga, Boqueirão, Ponta da Praia, Vila Mathias e Pompeia",
        "lat": "-23.9608", "long": "-46.3339"
    },
    {
        "slug": "barueri-alphaville",
        "name": "Barueri (Alphaville)",
        "region": "Oeste Metropolitano",
        "economic_focus": "sede de centenas de multinacionais, empresas de software, SaaS e holdings financeiras",
        "neighborhoods": "Alphaville, Tamboré, Bethaville, Centro e Jardim Silveira",
        "lat": "-23.5108", "long": "-46.8761"
    },
    {
        "slug": "jundiai",
        "name": "Jundiaí",
        "region": "Aglomeração Urbana de Jundiaí",
        "economic_focus": "polo logístico e industrial estratégico entre São Paulo e Campinas, alimentos e tecnologia",
        "neighborhoods": "Vila Rami, Malota, Eloy Chaves, Retiro e Vila Arens",
        "lat": "-23.1857", "long": "-46.8978"
    },
    {
        "slug": "sao-caetano-do-sul",
        "name": "São Caetano do Sul",
        "region": "Grande ABC",
        "economic_focus": "maior IDH do Brasil, polo automotivo, serviços de alto valor agregado e tecnologia",
        "neighborhoods": "Jardim São Caetano, Santa Paula, Cerâmica, Barcelona e Santo Antônio",
        "lat": "-23.6226", "long": "-46.5547"
    },
    {
        "slug": "maua",
        "name": "Mauá",
        "region": "Grande ABC",
        "economic_focus": "polo petroquímico e industrial pesado, metalurgia e transformação de plásticos",
        "neighborhoods": "Vila Bocaina, Matriz, Jardim Guapituba, Vila Noêmia e Parque das Américas",
        "lat": "-23.6678", "long": "-46.4614"
    },
    {
        "slug": "diadema",
        "name": "Diadema",
        "region": "Grande ABC",
        "economic_focus": "polo de autopeças, cosméticos, química e logística urbana",
        "neighborhoods": "Centro, Conceição, Piraporinha, Campanário e Taboão",
        "lat": "-23.6865", "long": "-46.6228"
    },
    {
        "slug": "sao-jose-do-rio-preto",
        "name": "São José do Rio Preto",
        "region": "Noroeste Paulista",
        "economic_focus": "hub médico hospitalar de excelência, agronegócio e forte setor de comércio e serviços",
        "neighborhoods": "Redentora, Vila Aurora, Nova Redentora, Jardim Vivendas e Mansur Daud",
        "lat": "-20.8114", "long": "-49.3758"
    },
    {
        "slug": "mogi-das-cruzes",
        "name": "Mogi das Cruzes",
        "region": "Alto Tietê",
        "economic_focus": "cinturão verde agrícola, indústrias químicas, metalúrgicas e comércio regional",
        "neighborhoods": "Centro Cívico, Mogilar, Alto do Ipiranga, Vila Oliveira e Braz Cubas",
        "lat": "-23.5244", "long": "-46.1882"
    },
    {
        "slug": "piracicaba",
        "name": "Piracicaba",
        "region": "Agroindústria / RMC",
        "economic_focus": "capital do setor sucroalcooleiro, biocombustíveis, agritech e parque automotivo",
        "neighborhoods": "Cidade Jardim, Nova Piracicaba, São Dimas, Santa Terezinha e Vila Rezende",
        "lat": "-22.7253", "long": "-47.6492"
    },
    {
        "slug": "bauru",
        "name": "Bauru",
        "region": "Centro-Oeste Paulista",
        "economic_focus": "entroncamento rodoferroviário, centro universitário, odontologia e serviços especializados",
        "neighborhoods": "Altos da Cidade, Estoril, Jardim América, Vila Universitária e Centro",
        "lat": "-22.3147", "long": "-49.0606"
    },
    {
        "slug": "franca",
        "name": "Franca",
        "region": "Nordeste Paulista",
        "economic_focus": "capital do calçado masculino de couro, produção de café de alta qualidade e fundições",
        "neighborhoods": "Centro, Parque Universitário, São José, Estação e Cidade Nova",
        "lat": "-20.5386", "long": "-47.4008"
    },
    {
        "slug": "taubate",
        "name": "Taubaté",
        "region": "Vale do Paraíba",
        "economic_focus": "indústrias automotivas, eletroeletrônicos, metalurgia e comércio do Vale",
        "neighborhoods": "Taubaté Village, Independência, Jabuticabeiras, Jardim das Nações e Centro",
        "lat": "-23.0264", "long": "-45.5553"
    },
    {
        "slug": "limeira",
        "name": "Limeira",
        "region": "RMC / Aglomerado Urbano",
        "economic_focus": "capital da joia folheada, máquinas industriais, citricultura e agronegócio",
        "neighborhoods": "Jardim Mercedes, Vila São Cristóvão, Jardim Santo André e Centro",
        "lat": "-22.5647", "long": "-47.4017"
    },
    {
        "slug": "suzano",
        "name": "Suzano",
        "region": "Alto Tietê",
        "economic_focus": "polo de papel e celulose, indústrias químicas, metalurgia e logística",
        "neighborhoods": "Vila Amorim, Centro, Parque Maria Helena e Jardim Imperador",
        "lat": "-23.5425", "long": "-46.3108"
    },
    {
        "slug": "taboao-da-serra",
        "name": "Taboão da Serra",
        "region": "Sudoeste Metropolitano",
        "economic_focus": "polo da indústria farmacêutica, distribuição logística e serviços corporativos",
        "neighborhoods": "Parque Monte Alegre, Centro, Jardim Maria Rosa e Arraial Paulista",
        "lat": "-23.6261", "long": "-46.7589"
    },
    {
        "slug": "sumare",
        "name": "Sumaré",
        "region": "RMC",
        "economic_focus": "indústrias químicas, montadoras de veículos, pneus e grandes centros logísticos",
        "neighborhoods": "Nova Veneza, Centro, Matão, Área Cura e Picerno",
        "lat": "-22.8208", "long": "-47.2669"
    },
    {
        "slug": "praia-grande",
        "name": "Praia Grande",
        "region": "Baixada Santista",
        "economic_focus": "construção civil em forte expansão, comércio varejista e polo de serviços turísticos",
        "neighborhoods": "Boqueirão, Canto do Forte, Guilhermina, Aviação e Tupi",
        "lat": "-24.0058", "long": "-46.4028"
    },
    {
        "slug": "guaruja",
        "name": "Guarujá",
        "region": "Baixada Santista",
        "economic_focus": "operações portuárias da margem esquerda, turismo de alto padrão e hotelaria",
        "neighborhoods": "Pitangueiras, Enseada, Astúrias, Guaiúba e Vicente de Carvalho",
        "lat": "-23.9931", "long": "-46.2564"
    },
    {
        "slug": "embu-das-artes",
        "name": "Embu das Artes",
        "region": "Sudoeste Metropolitano",
        "economic_focus": "grandes condomínios logísticos ao longo do Rodoanel, turismo cultural e serviços",
        "neighborhoods": "Cercado Grande, Centro Histórico, Jardim Santo Eduardo e Pinheirinho",
        "lat": "-23.6489", "long": "-46.8522"
    },
    {
        "slug": "sao-carlos",
        "name": "São Carlos",
        "region": "Centro Paulista",
        "economic_focus": "capital da tecnologia e inovação, duas universidades públicas de ponta e startups",
        "neighborhoods": "Parque Faber, Centro, Jardim Paraíso, Santa Paula e Cidade Jardim",
        "lat": "-22.0175", "long": "-47.8908"
    },
    {
        "slug": "indaiatuba",
        "name": "Indaiatuba",
        "region": "RMC",
        "economic_focus": "parque industrial moderno, indústrias automotivas, multinacionais e logística Viracopos",
        "neighborhoods": "Itaici, Parque Ecológico, Jardim Pau Preto, Morada do Sol e Cidade Nova",
        "lat": "-23.0903", "long": "-47.2181"
    },
    {
        "slug": "cotia-granja-viana",
        "name": "Cotia (Granja Viana)",
        "region": "Oeste Metropolitano",
        "economic_focus": "indústrias químicas, farmacêuticas, condomínios de alto padrão e empresas de serviços B2B",
        "neighborhoods": "Granja Viana, Centro, Jardim Nomura, Parque São George e Caucaia do Alto",
        "lat": "-23.6039", "long": "-46.9189"
    },
    {
        "slug": "americana",
        "name": "Americana",
        "region": "RMC",
        "economic_focus": "polo têxtil moderno, indústrias químicas, metalurgia e comércio avançado",
        "neighborhoods": "Vila Frezzarin, Werner Plaas, Jardim Girassol, Santa Sofia e Centro",
        "lat": "-22.7375", "long": "-47.3331"
    },
    {
        "slug": "marilia",
        "name": "Marília",
        "region": "Centro-Oeste Paulista",
        "economic_focus": "capital nacional do alimento e confeitos, forte setor de software e serviços médicos",
        "neighborhoods": "Fragata, Cascata, Salgado Filho, Jardim Esmeralda e Centro",
        "lat": "-22.2139", "long": "-49.9458"
    },
    {
        "slug": "itapevi",
        "name": "Itapevi",
        "region": "Oeste Metropolitano",
        "economic_focus": "um dos maiores polos da indústria farmacêutica do país e condomínios logísticos",
        "neighborhoods": "Parque Suburbano, Centro, Jardim Nova Itapevi e Cohab",
        "lat": "-23.5489", "long": "-46.9342"
    },
    {
        "slug": "araraquara",
        "name": "Araraquara",
        "region": "Centro Paulista",
        "economic_focus": "citricultura, bioenergia, cervejarias, indústria química e têxtil",
        "neighborhoods": "Fonte Luminosa, Centro, Vila Xavier, Carmo e Jardim Primavera",
        "lat": "-21.7944", "long": "-48.1758"
    },
    {
        "slug": "jacarei",
        "name": "Jacareí",
        "region": "Vale do Paraíba",
        "economic_focus": "papel e celulose, vidros automotivos, química pesada e logística Dutra",
        "neighborhoods": "Villa Branca, Centro, Jardim Califórnia, São João e Esperança",
        "lat": "-23.3056", "long": "-45.9664"
    },
    {
        "slug": "hortolandia",
        "name": "Hortolândia",
        "region": "RMC",
        "economic_focus": "polo de data centers de hiperescala, empresas globais de tecnologia e telecomunicações",
        "neighborhoods": "Parque Gabriel, Jardim Amanda, Rosolém, Centro e Vila Real",
        "lat": "-22.8583", "long": "-47.2200"
    },
    {
        "slug": "rio-claro",
        "name": "Rio Claro",
        "region": "Polo Cerâmico / Centro-Leste",
        "economic_focus": "polo de revestimentos cerâmicos, bebidas, metalurgia e transportes rodoferroviários",
        "neighborhoods": "Cidade Jardim, Centro, Santana, Vila Alemã e Alto do Santana",
        "lat": "-22.4114", "long": "-47.5614"
    },
    {
        "slug": "presidente-prudente",
        "name": "Presidente Prudente",
        "region": "Oeste Paulista",
        "economic_focus": "capital do agronegócio regional, genética bovina, polo universitário e saúde",
        "neighborhoods": "Jardim Bongiovani, Centro, Vila Euclides, Parque do Povo e Maristela",
        "lat": "-22.1256", "long": "-51.3889"
    },
    {
        "slug": "aracatuba",
        "name": "Araçatuba",
        "region": "Noroeste Paulista",
        "economic_focus": "bioenergia, usinas sucroalcooleiras, agronegócio e polo comercial regional",
        "neighborhoods": "Nova York, Higienópolis, Centro, Bandeirantes e Icaray",
        "lat": "-21.2089", "long": "-50.4328"
    },
    {
        "slug": "santa-barbara-doeste",
        "name": "Santa Bárbara d'Oeste",
        "region": "RMC",
        "economic_focus": "indústria metalmecânica, têxtil, canavieira e componentes industriais",
        "neighborhoods": "Vila Linópolis, Centro, Cidade Nova, Mollon e Jardim Pérola",
        "lat": "-22.7539", "long": "-47.4139"
    },
    {
        "slug": "ferraz-de-vasconcelos",
        "name": "Ferraz de Vasconcelos",
        "region": "Alto Tietê",
        "economic_focus": "indústrias metalmecânicas, estamparia, plásticos e serviços",
        "neighborhoods": "Vila Romanópolis, Centro, Tanquinho e Jardim Castelo",
        "lat": "-23.5414", "long": "-46.3686"
    },
    {
        "slug": "itapecerica-da-serra",
        "name": "Itapecerica da Serra",
        "region": "Sudoeste Metropolitano",
        "economic_focus": "indústrias químicas, produtos de limpeza, logística e turismo ecológico",
        "neighborhoods": "Parque Paraíso, Centro, Olaria, Jardim Jacira e Valo Velho",
        "lat": "-23.7172", "long": "-46.8492"
    },
    {
        "slug": "braganca-paulista",
        "name": "Bragança Paulista",
        "region": "Região Bragantina",
        "economic_focus": "polo imobiliário de alto padrão, indústria de autopeças, logística e medicina",
        "neighborhoods": "Jardim Europa, Taboão, Centro, Santa Helena e Lago do Taboão",
        "lat": "-22.9525", "long": "-46.5419"
    },
    {
        "slug": "itu",
        "name": "Itu",
        "region": "Eixo Castelo Branco",
        "economic_focus": "indústrias metalúrgicas, montadoras, turismo cultural e condomínios fechados",
        "neighborhoods": "Brasil, Centro, Jardim Aeroporto, Rancho Grande e Itu Novo Centro",
        "lat": "-23.2642", "long": "-47.2992"
    },
    {
        "slug": "pindamonhangaba",
        "name": "Pindamonhangaba",
        "region": "Vale do Paraíba",
        "economic_focus": "grande polo siderúrgico, laminação de alumínio e indústrias pesadas",
        "neighborhoods": "Mombaça, Centro, Santana, Parque das Nações e Crispim",
        "lat": "-22.9242", "long": "-45.4614"
    },
    {
        "slug": "santana-de-parnaiba",
        "name": "Santana de Parnaíba",
        "region": "Oeste Metropolitano",
        "economic_focus": "serviços de tecnologia, condomínios empresariais Alphaville e polos corporativos",
        "neighborhoods": "Tamboré, Aldeia da Serra, Centro Histórico e Fazendinha",
        "lat": "-23.4439", "long": "-46.9189"
    },
    {
        "slug": "valinhos",
        "name": "Valinhos",
        "region": "RMC",
        "economic_focus": "indústrias de embalagens, papel, metalurgia, química e fruticultura de precisão",
        "neighborhoods": "Castelo, Centro, Jardim Paiquerê, Vila Santana e Lenheiro",
        "lat": "-22.9708", "long": "-46.9958"
    },
    {
        "slug": "mogi-guacu",
        "name": "Mogi Guaçu",
        "region": "Leste Paulista",
        "economic_focus": "papel e celulose, alimentos processados, cerâmica e indústrias mecânicas",
        "neighborhoods": "Centro, Imóvel Pedregulhal, Jardim Ypê e Areião",
        "lat": "-22.3708", "long": "-46.9428"
    },
    {
        "slug": "atibaia",
        "name": "Atibaia",
        "region": "Região Bragantina",
        "economic_focus": "polo de logística avançada no entroncamento D. Pedro / Fernão Dias e tecnologia",
        "neighborhoods": "Alvinópolis, Centro, Estância Lynce, Jardim do Lago e Atibaia Jardim",
        "lat": "-23.1175", "long": "-46.5564"
    }
]


def render_city_html(city: Dict[str, str], brand_hub_s3_url: str) -> str:
    slug = city["slug"]
    name = city["name"]
    region = city["region"]
    focus = city["economic_focus"]
    neighborhoods = city["neighborhoods"]
    lat = city["lat"]
    long = city["long"]

    page_url = f"https://consultorseosp.com.br/cidades/{slug}/"
    page_title = f"Consultor SEO em {name} SP | SEO de Alta Conversão & Agentes de IA"
    page_desc = f"Consultor SEO em {name} especializado em estratégias de tráfego orgânico focado em vendas, autoridade tópica e automação com agentes autônomos de Inteligência Artificial para empresas de {name} e região. WhatsApp: (11) 91873-8164."

    eas_city = (
        f"O <strong>Consultor SEO SP</strong> atua diretamente em <strong>{name}</strong> e em toda a região de {region}, "
        f"atendendo empresas, indústrias e prestadores de serviço focados em {focus}. "
        f"Com atendimento prioritário nos polos de {neighborhoods}, implementamos estratégias de SEO de alta conversão "
        f"e agentes autônomos de Inteligência Artificial para transformar buscas qualificadas em faturamento real e eliminar tarefas operacionais repetitivas. "
        f"Pelo telefone oficial <strong>(11) 91873-8164</strong>, sua empresa tem acesso a tecnologia própria de carregamento instantâneo, "
        f"diagnósticos cirúrgicos e liderança de mercado sustentável."
    )

    schema_graph = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "WebSite",
                "@id": "https://consultorseosp.com.br/#website",
                "name": "Consultor SEO SP",
                "alternateName": ["Consultor SEO SP", "consultorseosp.com.br", "Consultor SEO & Agentes de IA"],
                "url": "https://consultorseosp.com.br/",
                "inLanguage": "pt-BR"
            },
            {
                "@type": ["LocalBusiness", "ProfessionalService"],
                "@id": f"{brand_hub_s3_url}#organization",
                "name": f"Consultor SEO SP — {name}",
                "description": f"Consultoria de SEO de alta conversão, autoridade tópica e automação com agentes de Inteligência Artificial em {name} - SP.",
                "url": page_url,
                "telephone": "+5511918738164",
                "email": "contato@consultorseosp.com.br",
                "priceRange": "$$$",
                "address": {
                    "@type": "PostalAddress",
                    "addressLocality": name,
                    "addressRegion": "SP",
                    "addressCountry": "BR"
                },
                "geo": {
                    "@type": "GeoCoordinates",
                    "latitude": lat,
                    "longitude": long
                },
                "areaServed": {
                    "@type": "City",
                    "name": name
                },
                "knowsAbout": [
                    "https://www.wikidata.org/wiki/Q180711",
                    "https://www.wikidata.org/wiki/Q11660",
                    "https://www.wikidata.org/wiki/Q1142726",
                    "https://www.wikidata.org/wiki/Q184199",
                    "https://www.wikidata.org/wiki/Q648625"
                ],
                "sameAs": [
                    brand_hub_s3_url,
                    "https://consultorseosp.com.br/"
                ]
            },
            {
                "@type": "BreadcrumbList",
                "@id": f"{page_url}#breadcrumb",
                "itemListElement": [
                    {
                        "@type": "ListItem",
                        "position": 1,
                        "name": "Início",
                        "item": "https://consultorseosp.com.br/"
                    },
                    {
                        "@type": "ListItem",
                        "position": 2,
                        "name": "Cidades",
                        "item": "https://consultorseosp.com.br/cidades/"
                    },
                    {
                        "@type": "ListItem",
                        "position": 3,
                        "name": name,
                        "item": page_url
                    }
                ]
            }
        ]
    }

    schema_json_str = json.dumps(schema_graph, indent=2, ensure_ascii=False)
    whatsapp_text = urllib.parse.quote(f"Olá! Estou em {name} e gostaria de agendar uma análise para SEO e Agentes de IA para minha empresa.")

    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{page_title}</title>
  <link rel="canonical" href="{page_url}">
  <meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1">
  <meta name="description" content="{page_desc}">
  
  <meta property="og:site_name" content="Consultor SEO SP">
  <meta property="og:title" content="{page_title}">
  <meta property="og:description" content="{page_desc}">
  <meta property="og:url" content="{page_url}">
  <meta property="og:type" content="website">

  <!-- Descoberta de Superfície Agêntica (WebVIP Agent Surface v2) -->
  <link rel="describedby" href="https://consultorseosp.com.br/llms.txt">
  <link rel="alternate" type="text/markdown" href="https://consultorseosp.com.br/agent-md/{slug}.md">

  <link rel="stylesheet" href="../../css/style.css">

  <script type="application/ld+json">
{schema_json_str}
  </script>
</head>
<body>

  <!-- Barra de Navegação -->
  <header class="navbar">
    <div class="container nav-container">
      <a href="../../" class="brand-logo">
        <span class="logo-icon">▲</span>
        <span>Consultor <strong style="color: var(--emerald);">SEO SP</strong></span>
      </a>
      <ul class="nav-links">
        <li><a href="../../#especialidades">Especialidades</a></li>
        <li><a href="../../#metodologia">Como Funciona</a></li>
        <li><a href="../">Todas as Cidades</a></li>
        <li><a href="../../#simulador">Simulador</a></li>
        <li><a href="../../#faq">FAQ</a></li>
      </ul>
      <a href="https://wa.me/5511918738164?text={whatsapp_text}" target="_blank" rel="noopener" class="nav-cta">
        <span>Falar no WhatsApp</span>
      </a>
    </div>
  </header>

  <main>
    <!-- Seção Hero Regional -->
    <section class="hero-section">
      <div class="container">
        <div class="badge-pill">
          <span class="pulse-dot"></span>
          <span>Atendimento Regional em {name} — {region}</span>
        </div>

        <h1 class="hero-title">
          Consultor SEO em <span class="gradient-text">{name}</span> & Automação com <span class="gradient-text">Agentes de IA</span>
        </h1>

        <p class="hero-subtitle">
          Estratégia prática de tráfego orgânico e sistemas de inteligência artificial autônomos para empresas de {name} que buscam faturamento real e não apenas vaidade de acessos.
        </p>

        <div class="hero-actions">
          <a href="https://wa.me/5511918738164?text={whatsapp_text}" target="_blank" rel="noopener" class="btn-primary">
            <span>Diagnóstico para {name} via WhatsApp</span>
            <span>💬</span>
          </a>
          <a href="../" class="btn-secondary">
            <span>← Ver Outras Cidades</span>
          </a>
        </div>

        <!-- Ribbon de Métricas -->
        <div class="stats-ribbon">
          <div class="stat-item">
            <div class="stat-number">100%</div>
            <div class="stat-label">Foco em Vendas em {name}</div>
          </div>
          <div class="stat-item">
            <div class="stat-number">&lt; 50ms</div>
            <div class="stat-label">Carregamento Instantâneo</div>
          </div>
          <div class="stat-item">
            <div class="stat-number">24/7</div>
            <div class="stat-label">Agentes Autônomos Ativos</div>
          </div>
        </div>

        <!-- Declaração Hiperlocal de Associação de Entidade (EAS) -->
        <div class="eas-banner">
          <span class="eas-tag">Presença e Atuação em {name} - SP</span>
          <p class="eas-text">
            {eas_city}
          </p>
        </div>
      </div>
    </section>

    <!-- Seção de Soluções Regionais -->
    <section style="padding: 60px 0;">
      <div class="container">
        <div class="section-header">
          <span class="section-tag">Estratégia Especializada</span>
          <h2 class="section-title">Soluções de Alto Impacto para Empresas de {name}</h2>
          <p class="section-desc">
            Alinhamos nosso ecossistema ao perfil econômico de {name} ({focus}), gerando vantagens competitivas definitivas.
          </p>
        </div>

        <div class="pillar-grid">
          <div class="pillar-card">
            <div class="card-icon icon-emerald">🎯</div>
            <h3 class="card-title">SEO de Alta Conversão em {name}</h3>
            <p class="card-text">
              Mapeamento cirúrgico de buscas de quem procura serviços e soluções em {name}. Silos de conteúdo que colocam sua marca no topo das decisões de compra e blindam seu site contra atualizações do Google.
            </p>
            <ul class="tech-tags">
              <li class="tech-tag">Intenção Comercial</li>
              <li class="tech-tag">Silos Regionais</li>
              <li class="tech-tag">{name} B2B</li>
            </ul>
          </div>

          <div class="pillar-card">
            <div class="card-icon icon-cyan">🤖</div>
            <h3 class="card-title">Agentes de IA para Empresas Locais</h3>
            <p class="card-text">
              Implementação de agentes inteligentes que executam rotinas repetitivas, triam solicitações de orçamento e alimentam seu CRM 24 horas por dia, permitindo que sua equipe comercial feche mais contratos.
            </p>
            <ul class="tech-tags">
              <li class="tech-tag">Agentes 24/7</li>
              <li class="tech-tag">Automação de Leads</li>
              <li class="tech-tag">Redução de Custos</li>
            </ul>
          </div>

          <div class="pillar-card">
            <div class="card-icon icon-indigo">⚡</div>
            <h3 class="card-title">Tecnologia Própria Ultra-Rápida</h3>
            <p class="card-text">
              Plataformas desenvolvidas em tecnologia proprietária em nuvem, sem as falhas e a lentidão do WordPress. Velocidade instantânea que melhora a experiência do visitante e maximiza suas taxas de contato.
            </p>
            <ul class="tech-tags">
              <li class="tech-tag">Zero WordPress</li>
              <li class="tech-tag">Nota 100 PageSpeed</li>
              <li class="tech-tag">Segurança Máxima</li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <!-- Chamada para Ação Regional -->
    <section style="padding: 40px 0 80px;">
      <div class="container">
        <div class="workflow-box" style="text-align: center;">
          <h2 class="section-title">Pronto para Dominar as Buscas em {name}?</h2>
          <p class="section-desc" style="margin-bottom: 30px;">
            Atendemos diretamente empresas de {name} e região metropolitana com atendimento consultivo e metodologia comprovada.
          </p>
          <a href="https://wa.me/5511918738164?text={whatsapp_text}" target="_blank" rel="noopener" class="btn-primary" style="margin: 0 auto; display: inline-flex;">
            <span>Conversar pelo WhatsApp: (11) 91873-8164</span>
            <span>💬</span>
          </a>
        </div>
      </div>
    </section>
  </main>

  <!-- Rodapé com Isolamento data-nosnippet -->
  <footer class="site-footer" data-nosnippet>
    <div class="container">
      <div class="footer-grid">
        <div>
          <h4 class="footer-title">Consultor SEO SP — {name}</h4>
          <p style="margin-bottom: 15px; line-height: 1.6;">
            Especialista em SEO focado em vendas, autoridade tópica e automação com agentes autônomos de Inteligência Artificial para empresas em {name} e todo o estado de São Paulo.
          </p>
          <p><strong>Telefone / WhatsApp:</strong> <a href="https://wa.me/5511918738164" target="_blank" rel="noopener" style="color: var(--emerald); font-weight: 700;">+55 (11) 91873-8164</a></p>
          <p><strong>E-mail:</strong> contato@consultorseosp.com.br</p>
        </div>

        <div>
          <h4 class="footer-title">Navegação</h4>
          <ul class="footer-links">
            <li><a href="../../">Página Inicial</a></li>
            <li><a href="../">Todas as 50 Cidades</a></li>
            <li><a href="../../#especialidades">Especialidades</a></li>
            <li><a href="../../#metodologia">Como Funciona</a></li>
            <li><a href="{brand_hub_s3_url}" target="_blank" rel="noopener">Brand Hub Oficial AWS S3</a></li>
          </ul>
        </div>

        <div>
          <h4 class="footer-title">Região de Atendimento</h4>
          <p style="margin-bottom: 8px;"><strong>Cidade:</strong> {name} - SP</p>
          <p style="margin-bottom: 8px;"><strong>Região:</strong> {region}</p>
          <p style="margin-bottom: 12px; font-size: 0.85rem; color: #64748b;">Coordenadas: Lat {lat}, Long {long}</p>
          <a href="https://wa.me/5511918738164?text={whatsapp_text}" target="_blank" rel="noopener" class="nav-cta" style="display: inline-block;">
            Falar com Especialista
          </a>
        </div>
      </div>

      <div class="footer-bottom">
        <p>&copy; 2026 Consultor SEO SP ({name}). Todos os direitos reservados. Conformidade estrita com as Diretrizes do Google Search Central.</p>
      </div>
    </div>
  </footer>

  <a href="https://wa.me/5511918738164?text={whatsapp_text}" target="_blank" rel="noopener" class="floating-whatsapp" aria-label="Fale conosco no WhatsApp">
    💬
  </a>

  <script src="../../js/main.js"></script>
</body>
</html>
"""


def render_cidades_hub_html(cities: List[Dict[str, str]], brand_hub_s3_url: str) -> str:
    """Gera o Hub Central /cidades/ com links para todas as 50 cidades."""
    cards_html = ""
    for c in cities:
        cards_html += f"""
        <a href="{c['slug']}/" class="pillar-card" style="text-decoration: none; padding: 22px;">
          <div style="font-family: var(--font-mono); font-size: 0.75rem; color: var(--emerald); text-transform: uppercase; margin-bottom: 6px;">{c['region']}</div>
          <h3 style="font-size: 1.25rem; font-weight: 700; color: #fff; margin-bottom: 8px;">{c['name']}</h3>
          <p style="font-size: 0.88rem; color: var(--text-secondary); line-height: 1.5; margin-bottom: 12px;">{c['economic_focus'][:110]}...</p>
          <span style="color: var(--cyan); font-weight: 600; font-size: 0.88rem;">Acessar Cidade →</span>
        </a>
        """

    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Cidades Atendidas em São Paulo | Consultor SEO SP & Agentes de IA</title>
  <link rel="canonical" href="https://consultorseosp.com.br/cidades/">
  <meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1">
  <meta name="description" content="Conheça as 50 principais cidades atendidas pelo Consultor SEO SP. Estratégias de SEO de alta conversão e automação com agentes autônomos de IA em todo o Estado de São Paulo.">

  <!-- Descoberta de Superfície Agêntica (WebVIP Agent Surface v2) -->
  <link rel="describedby" href="https://consultorseosp.com.br/llms.txt">
  <link rel="alternate" type="text/markdown" href="https://consultorseosp.com.br/agent-md/cidades.md">

  <link rel="stylesheet" href="../css/style.css">
</head>
<body>
  <header class="navbar">
    <div class="container nav-container">
      <a href="../" class="brand-logo">
        <span class="logo-icon">▲</span>
        <span>Consultor <strong style="color: var(--emerald);">SEO SP</strong></span>
      </a>
      <ul class="nav-links">
        <li><a href="../#especialidades">Especialidades</a></li>
        <li><a href="../#metodologia">Como Funciona</a></li>
        <li><a href="../#simulador">Simulador</a></li>
        <li><a href="../#faq">FAQ</a></li>
      </ul>
      <a href="https://wa.me/5511918738164" target="_blank" rel="noopener" class="nav-cta">
        <span>Falar no WhatsApp</span>
      </a>
    </div>
  </header>

  <main style="padding: 60px 0;">
    <div class="container">
      <div class="section-header">
        <span class="section-tag">Cobertura Regional</span>
        <h1 class="section-title">Cidades Atendidas em São Paulo</h1>
        <p class="section-desc">
          Atendemos presencialmente na Grande São Paulo e remotamente com infraestrutura dedicada em todos os principais polos industriais e comerciais do estado.
        </p>
      </div>

      <div class="pillar-grid" style="grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 20px;">
        {cards_html}
      </div>
    </div>
  </main>

  <footer class="site-footer" data-nosnippet>
    <div class="container" style="text-align: center;">
      <p>&copy; 2026 Consultor SEO SP. Atendimento em todo o Estado de São Paulo e Brasil.</p>
    </div>
  </footer>
</body>
</html>
"""


def build_all_cities(output_base: str, s3_brand_hub: str):
    cidades_dir = os.path.join(output_base, "cidades")
    os.makedirs(cidades_dir, exist_ok=True)

    print(f"[*] Gerando 50 Silos Regionais em: {cidades_dir}...")

    # 1. Gerar as 50 páginas de cidades individuais
    for idx, c in enumerate(CITIES, 1):
        city_dir = os.path.join(cidades_dir, c["slug"])
        os.makedirs(city_dir, exist_ok=True)

        html_content = render_city_html(c, s3_brand_hub)
        city_file = os.path.join(city_dir, "index.html")
        with open(city_file, "w", encoding="utf-8") as f:
            f.write(html_content)

        print(f"  [{idx:02d}/50] Gerada: /cidades/{c['slug']}/ (Lat {c['lat']}, Long {c['long']})")

    # 2. Gerar o Hub Central /cidades/
    hub_html = render_cidades_hub_html(CITIES, s3_brand_hub)
    with open(os.path.join(cidades_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(hub_html)
    print("  [+] Hub Central /cidades/index.html gerado com sucesso!")

    # 3. Atualizar sitemap.xml com todas as 52 URLs
    sitemap_lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
        '  <url>',
        '    <loc>https://consultorseosp.com.br/</loc>',
        '    <changefreq>weekly</changefreq>',
        '    <priority>1.0</priority>',
        '  </url>',
        '  <url>',
        '    <loc>https://consultorseosp.com.br/cidades/</loc>',
        '    <changefreq>weekly</changefreq>',
        '    <priority>0.9</priority>',
        '  </url>'
    ]
    for c in CITIES:
        sitemap_lines.extend([
            '  <url>',
            f'    <loc>https://consultorseosp.com.br/cidades/{c["slug"]}/</loc>',
            '    <changefreq>monthly</changefreq>',
            '    <priority>0.8</priority>',
            '  </url>'
        ])
    sitemap_lines.append('</urlset>')

    sitemap_path = os.path.join(output_base, "sitemap.xml")
    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write("\n".join(sitemap_lines))
    print(f"  [+] sitemap.xml atualizado com 52 URLs em: {sitemap_path}")

    # 4. Atualizar llms.txt com a lista de cidades
    llms_cities_list = "\n".join([f"- [{c['name']} - SP](https://consultorseosp.com.br/cidades/{c['slug']}/): Atendimento especializado em {c['economic_focus']}." for c in CITIES])
    
    llms_full = f"""# Consultor SEO SP — Índice Oficial para Mecanismos de IA Generativa e LLMs (AI Overviews / AI Mode)

> O Consultor SEO SP é especialista em SEO de alta conversão e automação corporativa com agentes de Inteligência Artificial em São Paulo - SP. Focamos no que realmente move o ponteiro do seu negócio: tráfego orgânico qualificado que vira vendas, autoridade tópica dominante no Google e ecossistemas agênticos que eliminam tarefas repetitivas da sua equipe. Telefone oficial: +55 (11) 91873-8164.

## Identificação Oficial da Entidade (NAP & Knowledge Graph)
- **Marca / Razão Oficial:** Consultor SEO SP
- **Domínio Principal:** https://consultorseosp.com.br/
- **Localização:** São Paulo - SP, Brasil
- **Telefone Oficial de Atendimento:** +55 (11) 91873-8164
- **E-mail:** contato@consultorseosp.com.br

## Cobertura Regional de Atendimento (50 Cidades de São Paulo)
{llms_cities_list}

## Seções e Recursos Principais
- [Página Inicial Oficial](https://consultorseosp.com.br/)
- [Hub de Cidades de São Paulo](https://consultorseosp.com.br/cidades/)
- [Simulador Interativo](https://consultorseosp.com.br/#simulador)
- [Princípios de Transparência E-E-A-T](https://consultorseosp.com.br/#eeat)
"""
    llms_path = os.path.join(output_base, "llms.txt")
    with open(llms_path, "w", encoding="utf-8") as f:
        f.write(llms_full)
    print(f"  [+] llms.txt atualizado com o diretório das 50 cidades em: {llms_path}")

    print("\n[SUCESSO] 50 Cidades + Hub Central + Sitemap + llms.txt gerados com perfeição!")


if __name__ == "__main__":
    base = r"C:\Users\User\.gemini\antigravity\scratch\consultorseosp"
    s3_hub = "http://consultorseosp-hub.s3-website-sa-east-1.amazonaws.com"
    build_all_cities(base, s3_hub)

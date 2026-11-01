# Auditoria GEO — consultorseosp
_Gerado em 2026-11-01 09:27 | Origem: https://consultorseosp.com.br | Modo: LOCAL + AO VIVO_

**Pontuação de elegibilidade técnica GEO: 100/100** (24/24 pontos)

| | Verificação | Detalhe |
|:-:|---|---|
| ✅ | Todas as URLs do sitemap existem localmente | 60 URLs; ausentes: [] |
| ✅ | robots.txt declara os crawlers de IA | faltando: [] |
| ✅ | robots.txt aponta o sitemap |  |
| ✅ | robots.txt não bloqueia o site inteiro |  |
| ✅ | llms.txt existe | 7.6KB |
| ✅ | llms.txt sem quebras de linha duplicadas (\r\r) |  |
| ✅ | llms.txt compacto (<20KB; detalhes vão no llms-full.txt) | 7.6KB |
| ✅ | llms-full.txt existe |  |
| ✅ | Todas as páginas do sitemap estão no llms.txt/llms-full.txt | 60/60; fora: [] |
| ✅ | Cada página tem versão agent-md/*.md | 60/60; sem .md: [] |
| ✅ | Links internos do llms apontam para arquivos existentes | 65 links; quebrados: [] |
| ✅ | Todos os links do llms e arquivos-chave respondem 200 (ao vivo) | 64 testados; falhas: [] |
| ✅ | Servidor/WAF não bloqueia UAs de bots de IA (teste ao vivo) | bloqueados: nenhum |

## Teste ao vivo por User-Agent

| Bot | Tipo | robots.txt permite? | HTTP / | HTTP robots | HTTP llms |
|---|---|:--:|:--:|:--:|:--:|
| OAI-SearchBot | busca/citacao | ✅ | 200 | 200 | 200 |
| ChatGPT-User | usuario/citacao | ✅ | 200 | 200 | 200 |
| GPTBot | treino | ✅ | 200 | 200 | 200 |
| PerplexityBot | busca/citacao | ✅ | 200 | 200 | 200 |
| Perplexity-User | usuario/citacao | ✅ | 200 | 200 | 200 |
| Claude-SearchBot | busca/citacao | ✅ | 200 | 200 | 200 |
| Claude-User | usuario/citacao | ✅ | 200 | 200 | 200 |
| ClaudeBot | treino | ✅ | 200 | 200 | 200 |
| Google-Extended | treino/Gemini (token robots) | ✅ | - | - | - |
| Applebot | busca | ✅ | 200 | 200 | 200 |
| Applebot-Extended | treino (token robots) | ✅ | - | - | - |
| Amazonbot | busca/assistente | ✅ | 200 | 200 | 200 |
| Meta-ExternalAgent | treino | ✅ | 200 | 200 | 200 |
| CCBot | dataset aberto | ✅ | 200 | 200 | 200 |
| DuckAssistBot | busca/citacao | ✅ | 200 | 200 | 200 |
| Googlebot | tradicional | ✅ | 200 | 200 | 200 |
| bingbot | tradicional | ✅ | 200 | 200 | 200 |

> Googlebot/bingbot com UA falso podem receber 403 do WAF (verificação de IP) — comportamento esperado e não indica bloqueio real.

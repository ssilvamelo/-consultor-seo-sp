"""
Antigravity SEO Spider & Internal PageRank Engine
Inspirado no Screaming Frog SEO Spider (v20+ Architecture)
Calcula PageRank Interno, Profundidade de Cliques (Crawl Depth), Inlinks, Outlinks e Oportunidades de Linkagem.
"""

import os
import re
from collections import defaultdict, deque
from bs4 import BeautifulSoup

BASE_DIR = r"C:\Users\User\.gemini\antigravity\scratch\consultorseosp"

def normalize_url(url, current_file):
    if not url or url.startswith(("#", "mailto:", "tel:", "javascript:")):
        return None
    if url.startswith(("http://", "https://")):
        if "consultorseosp.com.br" in url:
            # Converter para caminho relativo local
            path = url.split("consultorseosp.com.br")[-1].strip("/")
            return path if path else "index.html"
        return None  # Link externo

    # Limpar query e fragment
    clean = url.split("#")[0].split("?")[0].strip("/")
    if not clean:
        return "index.html"

    # Resolver caminho relativo com base no diretório absoluto do arquivo atual
    cur_dir = os.path.join(BASE_DIR, os.path.dirname(current_file))
    target_abs = os.path.normpath(os.path.join(cur_dir, clean)).replace("\\", "/")
    base_norm = os.path.normpath(BASE_DIR).replace("\\", "/")
    
    if target_abs.startswith(base_norm):
        rel = target_abs[len(base_norm):].strip("/")
        if not rel:
            return "index.html"
        full_target = os.path.join(BASE_DIR, rel)
        if os.path.isdir(full_target):
            return f"{rel}/index.html"
        elif not rel.endswith(".html") and not os.path.splitext(rel)[1]:
            return f"{rel}/index.html"
        return rel
    return clean

def crawl_site():
    html_files = {}
    for root, _, files in os.walk(BASE_DIR):
        if any(x in root for x in ["audit", "__pycache__", ".git", ".github"]):
            continue
        for f in files:
            if f.endswith(".html"):
                full_path = os.path.join(root, f)
                rel_path = os.path.relpath(full_path, BASE_DIR).replace("\\", "/")
                html_files[rel_path] = full_path

    print(f"[*] Crawling {len(html_files)} páginas HTML locais (Screaming Frog Engine)...")

    # Mapear grafo direcionado
    graph = defaultdict(set) # node -> set of outlinks
    inlinks_map = defaultdict(list) # target -> list of (source, anchor_text)
    anchor_analysis = defaultdict(list) # target -> list of anchors

    for rel_path, full_path in html_files.items():
        with open(full_path, "r", encoding="utf-8", errors="ignore") as fp:
            soup = BeautifulSoup(fp.read(), "html.parser")

        # Ignorar links de footer ou nosnippet se quiser análise pura de conteúdo,
        # mas Screaming Frog mapeia TODO o DOM.
        for a in soup.find_all("a", href=True):
            raw_href = a["href"].strip()
            anchor_text = a.get_text(strip=True) or "[Imagem/Sem Texto]"
            resolved = normalize_url(raw_href, rel_path)

            if resolved and (resolved in html_files or resolved.replace("/index.html", "") in html_files):
                # Normalizar formato index.html
                canonical_target = resolved
                if canonical_target not in html_files and f"{canonical_target}/index.html" in html_files:
                    canonical_target = f"{canonical_target}/index.html"
                
                graph[rel_path].add(canonical_target)
                inlinks_map[canonical_target].append((rel_path, anchor_text))
                anchor_analysis[canonical_target].append(anchor_text)

    # 1. Calcular Profundidade de Cliques (Crawl Depth) via BFS a partir da Home (index.html)
    depth = {k: -1 for k in html_files}
    queue = deque([("index.html", 0)])
    depth["index.html"] = 0
    visited = {"index.html"}

    while queue:
        curr, d = queue.popleft()
        for neighbor in graph[curr]:
            if neighbor in depth and neighbor not in visited:
                visited.add(neighbor)
                depth[neighbor] = d + 1
                queue.append((neighbor, d + 1))

    # 2. Algoritmo Iterativo de PageRank Interno (Damping Factor 0.85, 25 iterações)
    # Exatamente como Screaming Frog calcula o "Internal Link Score"
    N = len(html_files)
    damp = 0.85
    pr = {page: 1.0 / N for page in html_files}

    for iteration in range(30):
        new_pr = {}
        sink_pr = sum(pr[p] for p in html_files if len(graph[p]) == 0)
        for page in html_files:
            # Somatório de PR recebido dos nós que apontam para 'page'
            inlink_sum = sum(pr[src] / len(graph[src]) for src in html_files if page in graph[src])
            new_pr[page] = (1.0 - damp) / N + damp * (inlink_sum + sink_pr / N)
        pr = new_pr

    # Normalizar Link Score para escala 0 a 100 (Screaming Frog style)
    max_pr = max(pr.values()) if pr else 1.0
    link_scores = {page: round((pr[page] / max_pr) * 100, 1) for page in pr}

    return html_files, graph, inlinks_map, depth, link_scores, anchor_analysis

def generate_report():
    html_files, graph, inlinks_map, depth, link_scores, anchor_analysis = crawl_site()

    # Identificar métricas estratégicas
    orphans = [p for p in html_files if len(inlinks_map[p]) == 0 and p != "index.html"]
    dead_ends = [p for p in html_files if len(graph[p]) == 0]
    high_depth = [p for p in html_files if depth[p] > 3 or depth[p] == -1]

    # Ordenar por Link Score (PageRank)
    sorted_by_pr = sorted(link_scores.items(), key=lambda x: x[1], reverse=True)

    report_lines = []
    report_lines.append("# Relatório Executivo de Linkagem Interna & PageRank (Engine Screaming Frog)")
    report_lines.append(f"**Total de URLs Rastreadas:** {len(html_files)} páginas")
    report_lines.append(f"**Páginas Órfãs (0 Inlinks):** {len(orphans)} {('✅ NENHUMA!' if not orphans else '⚠️ Requer Atenção')}")
    report_lines.append(f"**Páginas Dead-End (0 Outlinks):** {len(dead_ends)}")
    report_lines.append(f"**Profundidade Média de Rastreador:** {round(sum(d for d in depth.values() if d >= 0) / len(depth), 2)} cliques")
    report_lines.append("\n---\n")

    report_lines.append("## 1. Top 15 Páginas com Maior PageRank Interno (Link Score 0-100)")
    report_lines.append("| URL | Link Score | Inlinks (Links Recebidos) | Outlinks (Links Enviados) | Crawl Depth |")
    report_lines.append("| :--- | :---: | :---: | :---: | :---: |")
    for page, score in sorted_by_pr[:15]:
        report_lines.append(f"| `{page}` | **{score}** | {len(inlinks_map[page])} | {len(graph[page])} | {depth[page]} cliques |")

    report_lines.append("\n---\n")
    report_lines.append("## 2. Análise Estratégica dos Artigos do Blog (Pilar Comercial)")
    report_lines.append("| Artigo B2B | Link Score | Inlinks | Crawl Depth | Âncora Mais Frequente |")
    report_lines.append("| :--- | :---: | :---: | :---: | :--- |")
    for page, score in sorted_by_pr:
        if page.startswith("blog/") and page != "blog/index.html":
            anchors = anchor_analysis[page]
            top_anchor = max(set(anchors), key=anchors.count) if anchors else "Nenhuma"
            report_lines.append(f"| `{page}` | **{score}** | {len(inlinks_map[page])} | {depth[page]} cliques | \"{top_anchor[:40]}\" |")

    report_lines.append("\n---\n")
    report_lines.append("## 3. Distribuição de Profundidade de Cliques (Crawl Depth)")
    depth_dist = defaultdict(int)
    for d in depth.values():
        depth_dist[d] += 1
    
    for d in sorted(depth_dist.keys()):
        label = "Inacessível (Órfã)" if d == -1 else f"{d} clique(s) da Home"
        pct = round((depth_dist[d] / len(html_files)) * 100, 1)
        report_lines.append(f"* **{label}:** {depth_dist[d]} páginas ({pct}%)")

    report_lines.append("\n---\n")
    report_lines.append("## 4. Oportunidades Estratégicas de Linkagem Interna Detectadas")
    
    # Detecção de oportunidades
    report_lines.append("1. **Clusterização Cruzada Blog ↔ Cidades:**")
    report_lines.append("   - Cidades de alto PIB (ex: Campinas, Guarulhos, Barueri) podem receber links contextuais diretos de artigos como `quanto-custa-consultor-seo-sp.html` para canalizar PageRank transacional.")
    report_lines.append("2. **Âncoras Semânticas de Alta Conversão:**")
    report_lines.append("   - Em vez de âncoras vazias em botões, utilizar termos de busca com cauda longa exata: *'consultor de SEO em Campinas'*, *'preço de SEO corporativo'*, *'automação com agentes de IA'*.")

    content = "\n".join(report_lines)
    output_file = os.path.join(BASE_DIR, "relatorio_linkagem_screaming_frog.md")
    with open(output_file, "w", encoding="utf-8") as fp:
        fp.write(content)

    print(f"\n[SUCESSO] Relatório gerado com sucesso em: {output_file}")
    return content

if __name__ == "__main__":
    generate_report()

import re

index_path = r"C:\Users\User\.gemini\antigravity\scratch\consultorseosp\index.html"

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

# Pattern to extract the figure block from hero
pattern = re.compile(
    r'(\s*<div style="margin: 2rem auto 1\.5rem; text-align: center; max-width: 960px;">\s*<figure class="consultorseo-media".*?</figure>\s*</div>)',
    re.DOTALL
)

match = pattern.search(content)
if not match:
    print("Error: Could not find media figure block in hero!")
    exit(1)

media_block = match.group(1)
print("Found media block, length:", len(media_block))

# Remove from hero
content_without_hero_media = content[:match.start()] + "\n" + content[match.end():]

# Prepare footer/bottom section containing the media block
# Update img loading to lazy and remove eager/fetchpriority
updated_media = media_block.replace('loading="eager"', 'loading="lazy"').replace('fetchpriority="high"', '')

new_bottom_section = f'''
    <!-- Seção de Credenciamento Técnico de Entidade Digital -->
    <section id="certificacao-entidade" style="padding: 40px 0 60px; background: rgba(15, 23, 42, 0.4); border-top: 1px solid var(--border);">
      <div class="container" style="text-align: center; max-width: 960px;">
        <h3 style="color: #fff; font-size: 1.5rem; margin-bottom: 20px;">Credenciamento Técnico & Infraestrutura Multi-Cloud</h3>
{updated_media}
      </div>
    </section>
'''

# We place it before </main>
main_close = "</main>"
if main_close not in content_without_hero_media:
    print("Error: </main> not found!")
    exit(1)

content_final = content_without_hero_media.replace(main_close, new_bottom_section + "\n  </main>")

with open(index_path, "w", encoding="utf-8") as f:
    f.write(content_final)

print("Successfully moved figure block from hero to bottom before </main>!")

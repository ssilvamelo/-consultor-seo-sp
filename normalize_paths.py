import os
import re

files_modified = 0

# 1. Root HTML files
root_files = ['index.html', '404.html', 'privacidade.html', 'termos.html']
for rf in root_files:
    if os.path.exists(rf):
        with open(rf, 'r', encoding='utf-8') as f:
            content = f.read()
        new_content = content
        new_content = re.sub(r'href=[\'"]/favicon\.ico[\'"]', 'href="favicon.ico"', new_content)
        new_content = re.sub(r'href=[\'"]/favicon\.png[\'"]', 'href="favicon.png"', new_content)
        new_content = re.sub(r'href=[\'"]/apple-touch-icon\.png[\'"]', 'href="apple-touch-icon.png"', new_content)
        new_content = re.sub(r'href=[\'"]/css/style\.css[\'"]', 'href="css/style.css"', new_content)
        new_content = re.sub(r'href=[\'"]/cidades/?[\'"]', 'href="cidades/"', new_content)
        new_content = re.sub(r'href=[\'"]/blog/?[\'"]', 'href="blog/"', new_content)
        new_content = re.sub(r'href=[\'"]/privacidade\.html[\'"]', 'href="privacidade.html"', new_content)
        new_content = re.sub(r'href=[\'"]/termos\.html[\'"]', 'href="termos.html"', new_content)
        new_content = re.sub(r'href=[\'"]/index\.html[\'"]', 'href="index.html"', new_content)
        if new_content != content:
            with open(rf, 'w', encoding='utf-8') as f:
                f.write(new_content)
            files_modified += 1
            print(f"Updated root file: {rf}")

# 2. Blog HTML files
blog_dir = 'blog'
if os.path.exists(blog_dir):
    for f in os.listdir(blog_dir):
        if f.endswith('.html'):
            p = os.path.join(blog_dir, f)
            with open(p, 'r', encoding='utf-8') as fp:
                content = fp.read()
            new_content = content
            new_content = re.sub(r'href=[\'"]/favicon\.ico[\'"]', 'href="../favicon.ico"', new_content)
            new_content = re.sub(r'href=[\'"]/favicon\.png[\'"]', 'href="../favicon.png"', new_content)
            new_content = re.sub(r'href=[\'"]/apple-touch-icon\.png[\'"]', 'href="../apple-touch-icon.png"', new_content)
            new_content = re.sub(r'href=[\'"]/css/style\.css[\'"]', 'href="../css/style.css"', new_content)
            new_content = re.sub(r'href=[\'"]/cidades/?[\'"]', 'href="../cidades/"', new_content)
            if f == 'index.html':
                new_content = re.sub(r'href=[\'"]/blog/?[\'"]', 'href="./"', new_content)
                new_content = re.sub(r'href=[\'"]/blog/([a-zA-Z0-9_\-\.]+)\.html[\'"]', r'href="\1.html"', new_content)
            else:
                new_content = re.sub(r'href=[\'"]/blog/?[\'"]', 'href="./"', new_content)
                new_content = re.sub(r'href=[\'"]/blog/([a-zA-Z0-9_\-\.]+)\.html[\'"]', r'href="\1.html"', new_content)
            new_content = re.sub(r'href=[\'"]/privacidade\.html[\'"]', 'href="../privacidade.html"', new_content)
            new_content = re.sub(r'href=[\'"]/termos\.html[\'"]', 'href="../termos.html"', new_content)
            new_content = re.sub(r'href=[\'"]/[\'"]', 'href="../index.html"', new_content)
            new_content = re.sub(r'href=[\'"]/index\.html[\'"]', 'href="../index.html"', new_content)
            if new_content != content:
                with open(p, 'w', encoding='utf-8') as fp:
                    fp.write(new_content)
                files_modified += 1
                print(f"Updated blog file: {p}")

print(f"Total files updated: {files_modified}")

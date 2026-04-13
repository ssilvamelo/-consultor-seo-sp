const fs = require('fs');
const path = require('path');

const OPENROUTER_API_KEY = process.env.OPENROUTER_API_KEY;
const MODEL = "anthropic/claude-3.7-sonnet"; 

const slugs = [
  {
    slug: 'marketing-digital-sp-o-guia-completo-de-seo-para-2026',
    title: 'Marketing Digital em SP: O Guia Completo de SEO para 2026',
    image: '/images/artigos/marketing-digital.png'
  },
  {
    slug: 'auditoria-seo-gratuita-como-analisar-seu-site-hoje',
    title: 'Auditoria SEO Gratuita: Como Analisar seu Site Hoje',
    image: '/images/artigos/auditoria-seo.png'
  },
  {
    slug: 'seo-local-em-sao-paulo-estrategias-para-negocios-fisicos',
    title: 'SEO Local em São Paulo: Estratégias para Negócios Físicos',
    image: '/images/artigos/seo-local.png'
  },
  {
    slug: 'importancia-do-branding-para-o-posicionamento-organico',
    title: 'A Importância do Branding para o Posicionamento Orgânico',
    image: '/images/artigos/branding-seo.png'
  },
  {
    slug: 'como-escolher-a-melhor-agencia-de-seo-em-sao-paulo',
    title: 'Como Escolher a Melhor Agência de SEO em São Paulo',
    image: '/images/artigos/consultoria-seo-hero.png'
  },
  {
    slug: 'o-impacto-da-velocidade-do-site-no-seu-ranqueamento',
    title: 'O Impacto da Velocidade do Site no seu Ranqueamento',
    image: '/images/artigos/geosetter-seo-local.png'
  },
  {
    slug: 'link-building-sustentavel-para-empresas-paulistanas',
    title: 'Link Building Sustentável para Empresas Paulistanas',
    image: '/images/artigos/consultoria-seo-hero.png'
  },
  {
    slug: 'core-web-vitals-o-que-seu-negocio-em-sp-precisa-saber',
    title: 'Core Web Vitals: O que seu negócio em SP precisa saber',
    image: '/images/artigos/marketing-digital.png'
  }
];

const sleep = ms => new Promise(resolve => setTimeout(resolve, ms));

async function generateArticle(article) {
  console.log(`Generating article for: ${article.title}...`);
  
  const prompt = `You are an expert SEO consultant based in São Paulo. Write a highly optimized, engaging, and professional 400-word article about "${article.title}". 
Target audience: Business owners in São Paulo. 
Use modern, futuristic, and business-focused tone, referencing Sérgio Melo as the SEO consultant. 
Mention terms like "Consultor SEO SP", "visibilidade digital", "geotagging".

Output MUST BE ONLY valid Next.js React Functional Component code for 'page.js'. 
Do not wrap it in markdown block like \`\`\`jsx ... \`\`\`. Start immediately with imports. 
Do not add any explanation text.

Constraints for the component:
1. Must 'import Link from "next/link";'
2. Must 'import Image from "next/image";'
3. Must 'import styles from "./article.module.css";' (I will provide this CSS, assume it has classes: articleContainer, articleContent, heroWrapper, heroImage, ctaSection, ctaButton, backLinkWrapper, backLink)
4. Must export a 'metadata' object with 'title' and 'description'.
5. Must default export 'ArticlePage' function.
6. Return <main className={styles.articleContainer}> with <article className={styles.articleContent}>.
7. Include the hero image matching this image path exactly: "${article.image}" with 1200x600 dimensions.
8. Have a proper h1, h2, paragraphs.
9. Include a call to action section with 'CTA' to '/contato' labeled 'Fale com Sérgio Melo', using the class ctaButton.
10. Include a back link to '/' at the bottom.
`;

  try {
    const response = await fetch("https://openrouter.ai/api/v1/chat/completions", {
      method: "POST",
      headers: {
        "Authorization": "Bearer " + OPENROUTER_API_KEY,
        "HTTP-Referer": "http://localhost:3000",
        "X-Title": "Consultor SEO SP",
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        model: MODEL,
        messages: [{ role: "user", content: prompt }]
      })
    });

    if (!response.ok) {
        throw new Error("HTTP Error " + response.status + " " + response.statusText);
    }

    const data = await response.json();
    let content = data.choices[0].message.content;
    
    if (content.startsWith('\`\`\`')) {
      content = content.replace(/^\`\`\`[a-z]*\s*/, '').replace(/\`\`\`\s*$/, '');
    }

    const dir = path.join(__dirname, 'src/app/artigos', article.slug);
    if (!fs.existsSync(dir)){
        fs.mkdirSync(dir, { recursive: true });
    }
    
    fs.writeFileSync(path.join(dir, 'page.js'), content);
    console.log("Successfully generated and saved " + article.slug + "/page.js");
    
    const cssContent = `
.articleContainer {
  min-height: 100vh;
  padding: 8rem 2rem;
  background: var(--surface);
}

.articleContent {
  max-width: 800px;
  margin: 0 auto;
}

.heroWrapper {
  margin-bottom: 3rem;
  border-radius: 24px;
  overflow: hidden;
}

.heroImage {
  width: 100%;
  height: auto;
  display: block;
}

.articleContent h1 {
  font-size: 3rem;
  margin-bottom: 2rem;
  line-height: 1.2;
}

.articleContent h2 {
  font-size: 2rem;
  margin: 3rem 0 1.5rem;
}

.articleContent h3 {
  font-size: 1.5rem;
  margin: 2rem 0 1rem;
}

.articleContent p {
  font-size: 1.15rem;
  line-height: 1.8;
  color: var(--text-muted);
  margin-bottom: 1.5rem;
}

.articleContent strong {
  color: var(--text-main);
}

.ctaSection {
  margin: 4rem 0;
  padding: 3rem;
  background: rgba(79,70,229,0.1);
  border-radius: 16px;
  text-align: center;
  border: 1px solid rgba(79,70,229,0.3);
}

.ctaButton {
  display: inline-block;
  margin-top: 1.5rem;
  padding: 1rem 2.5rem;
  background: var(--primary);
  color: white;
  border-radius: 99px;
  font-weight: 700;
  text-decoration: none;
  transition: all 0.3s;
}

.ctaButton:hover {
  transform: translateY(-3px);
  box-shadow: 0 10px 20px rgba(79,70,229,0.3);
}

.backLinkWrapper {
  margin-top: 4rem;
  padding-top: 2rem;
  border-top: 1px solid rgba(255,255,255,0.05);
}

.backLink {
  color: var(--text-muted);
  text-decoration: none;
  transition: color 0.3s;
}

.backLink:hover {
  color: var(--primary);
}
`;
    fs.writeFileSync(path.join(dir, 'article.module.css'), cssContent.trim());
    
  } catch (err) {
    console.error("Error generating " + article.slug + ":", err);
  }
}

async function run() {
  for (const article of slugs) {
    await generateArticle(article);
    await sleep(2000); 
  }
  console.log("All 8 articles generated!");
}

run();

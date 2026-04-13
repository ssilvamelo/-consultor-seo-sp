import Link from 'next/link';
import Image from 'next/image';
import styles from './article.module.css';

export const metadata = {
  title: 'Consultoria SEO em São Paulo: Transforme Seu Negócio com Especialistas Locais',
  description: 'Descubra como uma consultoria SEO em São Paulo pode impulsionar sua visibilidade digital com Sérgio Melo. Estratégias personalizadas e futuristas.',
};

export default function ArticlePage() {
  return (
    <main className={styles.articleContainer}>
      <article className={styles.articleContent}>
        <div className={styles.heroWrapper}>
          <Image 
            src="/images/artigos/consultoria-seo-hero.png" 
            alt="Consultoria SEO São Paulo Sérgio Melo" 
            width={1200} 
            height={600} 
            className={styles.heroImage}
            priority
          />
        </div>

        <h1>Como uma Consultoria SEO em São Paulo pode Transformar seu Negócio</h1>
        <p>
          No cenário empresarial altamente competitivo de São Paulo, conquistar <strong>visibilidade digital</strong> é uma necessidade estratégica. Investir em uma <strong>consultoria SEO em São Paulo</strong> com <strong>Sérgio Melo</strong> é o diferencial decisivo para posicionar sua empresa no futuro da busca por IA e resultados orgânicos.
        </p>

        <h2>O que é SEO e por que ele é fundamental?</h2>
        <p>
          <strong>SEO (Search Engine Optimization)</strong> na era moderna envolve mais do que palavras-chave; trata-se de autoridade digital e georreferenciamento preciso. Quando executado por um especialista, o SEO gera tráfego qualificado de forma contínua, fortalecendo a marca <strong>Consultor SEO SP</strong>.
        </p>

        <h3>A importância do SEO Local</h3>
        <p>
          São Paulo exige estratégias geolocalizadas. Usamos técnicas avançadas de geotagging (como o GeoSetter) para garantir que sua empresa seja encontrada exatamente onde seu cliente está, seja na Paulista ou na Faria Lima.
        </p>

        <section className={styles.ctaSection}>
          <strong>Domine o Google em São Paulo</strong>
          <br />
          Estratégias fotorrealistas e futuristas integradas com o seu negócio.
          <br />
          <Link href="/contato" className={styles.ctaButton}>
            Fale com Sérgio Melo
          </Link>
        </section>

        <p className={styles.backLinkWrapper}>
          <Link href="/" className={styles.backLink}>
            &larr; Voltar para Home
          </Link>
        </p>
      </article>
    </main>
  );
}
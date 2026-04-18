'use client';

import { useEffect, useState } from 'react';
import Link from 'next/link';
import styles from './page.module.css';

export default function Home() {
  const [scrolled, setScrolled] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      setScrolled(window.scrollY > 50);
    };
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  return (
    <main className={styles.main}>
      <header className={`${styles.header} ${scrolled ? styles.headerScrolled : ''}`}>
        <div className="container">
           <div className={`glass ${styles.headerInner}`}>
              <div className={styles.logo}>ConsultorSEO<span className={styles.accent}>SP</span></div>
              <nav className={styles.nav}>
                <a href="#services">Serviços</a>
                <a href="#sobre">Fábrica SEO</a>
                <a href="#artigos">Artigos</a>
                <a href="https://wa.me/5511918738164?text=Ol%C3%A1%2C%20Sérgio!%20Vim%20pelo%20site%20e%20gostaria%20de%20um%20diagnóstico%20de%20SEO!" target="_blank" rel="noopener noreferrer" className="btn btn-primary">Fale com Sérgio</a>
              </nav>
           </div>
        </div>
      </header>

      <section className={styles.hero}>
        <div className="blob" style={{top: '-10%', right: '-5%'}}></div>
        <div className="blob" style={{bottom: '10%', left: '-5%', background: 'var(--secondary-glow)'}}></div>
        
        <div className={`container ${styles.heroContent} animate-fade-in`}>
          <span className={styles.heroSubtitle}>SEO & Branding de Alta Performance</span>
          <h1 className={styles.heroTitle}>Domine o Google com<br/><span className="gradient-text">SEO e BRANDING</span></h1>
          <p className={styles.heroText}>Aceleramos o crescimento da sua marca em São Paulo através de inteligência de busca e posicionamento de mercado estratégico.</p>
          <div className={styles.heroActions}>
            <a href="https://wa.me/5511918738164?text=Ol%C3%A1%2C%20Sérgio!%20Vim%20pelo%20site%20e%20gostaria%20de%20um%20diagnóstico%20de%20SEO!" className="btn btn-primary">Quero Resultados</a>
            <a href="#services" className="btn btn-outline">Ver Serviços</a>
          </div>
        </div>
      </section>

      <section id="services" className={styles.services}>
        <div className="container">
          <div className={`${styles.sectionHeader} animate-fade-in`}>
            <h2 className={styles.sectionTitle}>Nossa Expertise</h2>
            <p className={styles.heroText}>Soluções completas para empresas que não aceitam nada menos que a primeira página.</p>
          </div>
          <div className={styles.servicesGrid}>
             <div className={styles.serviceCard}>
                <div className={styles.serviceIcon}>🎯</div>
                <h3 className={styles.serviceTitle}>Estratégia SEO</h3>
                <p className={styles.serviceDesc}>Planejamento focado em conversão e autoridade real perante o Google.</p>
             </div>
             <div className={styles.serviceCard}>
                <div className={styles.serviceIcon}>⚡</div>
                <h3 className={styles.serviceTitle}>Performance Web</h3>
                <p className={styles.serviceDesc}>Otimizamos cada milissegundo. Velocidade que o Google e seus clientes amam.</p>
             </div>
             <div className={styles.serviceCard}>
                <div className={styles.serviceIcon}>📍</div>
                <h3 className={styles.serviceTitle}>SEO Local Elite</h3>
                <p className={styles.serviceDesc}>Domine o Google Maps em SP e seja a escolha número 1 da sua região.</p>
             </div>
             <div className={styles.serviceCard}>
                <div className={styles.serviceIcon}>💎</div>
                <h3 className={styles.serviceTitle}>Digital Branding</h3>
                <p className={styles.serviceDesc}>Posicionamento de marca que transmite confiança e solidez no mercado.</p>
             </div>
             <div className={styles.serviceCard}>
                <div className={styles.serviceIcon}>📟</div>
                <h3 className={styles.serviceTitle}>IA Content Factory</h3>
                <p className={styles.serviceDesc}>Nossa fábrica de conteúdo multi-modelo escala seu SEO em tempo recorde.</p>
             </div>
             <div className={styles.serviceCard}>
                <div className={styles.serviceIcon}>📈</div>
                <h3 className={styles.serviceTitle}>Auditoria 360º</h3>
                <p className={styles.serviceDesc}>Identificamos falhas críticas e oportunidades de ouro escondidas no seu site.</p>
             </div>
          </div>
        </div>
      </section>

      <section id="results" className={styles.services} style={{background: 'linear-gradient(to bottom, var(--bg-color), var(--surface))'}}>
        <div className="container">
          <div className={styles.aboutGrid} style={{display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '4rem', alignItems: 'center'}}>
            <div>
              <h2 className={styles.sectionTitle}>Resultados que escalam negócios</h2>
              <p className={styles.heroText} style={{marginLeft: 0, textAlign: 'left'}}>Abra mão do marketing de esperança. Usamos dados e tecnologia de ponta para garantir que sua marca seja encontrada por quem realmente quer comprar.</p>
              <ul style={{listStyle: 'none', marginTop: '2rem'}}>
                <li style={{marginBottom: '1rem', display: 'flex', alignItems: 'center', gap: '1rem'}}>
                  <span style={{color: 'var(--secondary)', fontSize: '1.5rem'}}>✓</span> +300% de Tráfego Orgânico Médio
                </li>
                <li style={{marginBottom: '1rem', display: 'flex', alignItems: 'center', gap: '1rem'}}>
                  <span style={{color: 'var(--secondary)', fontSize: '1.5rem'}}>✓</span> Domínio Total do Google Maps Local
                </li>
                <li style={{marginBottom: '1rem', display: 'flex', alignItems: 'center', gap: '1rem'}}>
                  <span style={{color: 'var(--secondary)', fontSize: '1.5rem'}}>✓</span> Autoridade E-E-A-T Inquestionável
                </li>
              </ul>
            </div>
            <div className={`glass ${styles.serviceCard}`} style={{padding: '4rem', textAlign: 'center'}}>
               <div style={{fontSize: '4rem', marginBottom: '1rem'}}>🚀</div>
               <h3 style={{fontSize: '2.5rem', marginBottom: '1rem'}}>Pronto para o Próximo Nível?</h3>
               <p style={{marginBottom: '2rem'}}>Migramos sua estrutura antiga para o futuro da web hoje.</p>
               <a href="https://wa.me/5511918738164" className="btn btn-primary">Falar com Especialista</a>
            </div>
          </div>
        </div>
      </section>

      <section id="artigos" className={styles.services}>
        <div className="container">
          <div className={styles.sectionHeader}>
            <h2 className={styles.sectionTitle}>Insights Estratégicos</h2>
            <p className={styles.heroText}>Acompanhe as últimas tendências de SEO, Branding e Geotagging em SP.</p>
          </div>
          
          <div className={styles.articlesGrid}>
            {/* O Guia Definitivo - Principal */}
            <a href="/artigos/geosetter-o-guia-definitivo-de-geotagging-para-seo-local-em-sao-paulo" className={styles.articleCard}>
              <div className={styles.articleImage} style={{backgroundImage: 'url(/images/artigos/geosetter-seo-local.png)'}}></div>
              <div className={styles.articleInfo}>
                <span className={styles.articleTag}>SEO LOCAL</span>
                <h3 className={styles.articleTitle}>GeoSetter: O Guia Definitivo de Geotagging</h3>
              </div>
            </a>

            {/* Transforme seu Negócio */}
            <a href="/artigos/como-uma-consultoria-seo-em-sao-paulo-pode-transformar-seu-negocio" className={styles.articleCard}>
              <div className={styles.articleImage} style={{backgroundImage: 'url(/images/artigos/consultoria-seo-hero.png)'}}></div>
              <div className={styles.articleInfo}>
                <span className={styles.articleTag}>CONSULTORIA</span>
                <h3 className={styles.articleTitle}>Transforme seu Negócio com SEO em SP</h3>
              </div>
            </a>

            {/* Marketing Digital 2026 */}
            <a href="/artigos/marketing-digital-sp-o-guia-completo-de-seo-para-2026" className={styles.articleCard}>
              <div className={styles.articleImage} style={{backgroundImage: 'url(/images/artigos/marketing-digital.png)'}}></div>
              <div className={styles.articleInfo}>
                <span className={styles.articleTag}>MARKETING DIGITAL</span>
                <h3 className={styles.articleTitle}>Guia Completo de SEO para 2026 em SP</h3>
              </div>
            </a>

            {/* Auditoria SEO */}
            <a href="/artigos/auditoria-seo-gratuita-como-analisar-seu-site-hoje" className={styles.articleCard}>
              <div className={styles.articleImage} style={{backgroundImage: 'url(/images/artigos/auditoria-seo.png)'}}></div>
              <div className={styles.articleInfo}>
                <span className={styles.articleTag}>AUDITORIA</span>
                <h3 className={styles.articleTitle}>Auditoria SEO: Como Analisar seu Site Hoje</h3>
              </div>
            </a>

            {/* SEO Local Negócios Físicos */}
            <a href="/artigos/seo-local-em-sao-paulo-estrategias-para-negocios-fisicos" className={styles.articleCard}>
              <div className={styles.articleImage} style={{backgroundImage: 'url(/images/artigos/seo-local.png)'}}></div>
              <div className={styles.articleInfo}>
                <span className={styles.articleTag}>MAPS</span>
                <h3 className={styles.articleTitle}>Estratégias de SEO Local para Negócios</h3>
              </div>
            </a>

            {/* Branding e Posicionamento */}
            <a href="/artigos/importancia-do-branding-para-o-posicionamento-organico" className={styles.articleCard}>
              <div className={styles.articleImage} style={{backgroundImage: 'url(/images/artigos/branding-seo.png)'}}></div>
              <div className={styles.articleInfo}>
                <span className={styles.articleTag}>BRANDING</span>
                <h3 className={styles.articleTitle}>O Poder do Branding no SEO</h3>
              </div>
            </a>
          </div>
        </div>
      </section>

      <footer className={styles.footer}>
        <div className="container">
          <div className={styles.logo}>ConsultorSEO<span className={styles.accent}>SP</span></div>
          <p style={{color: 'var(--text-muted)', marginTop: '1rem'}}>Sérgio Melo - Especialista em SEO & Branding</p>
          <p style={{marginTop: '3rem', fontSize: '0.8rem', opacity: 0.5}}>© {new Date().getFullYear()} Consultor SEO SP. Todos os direitos reservados.</p>
        </div>
      </footer>
    </main>
  );
}

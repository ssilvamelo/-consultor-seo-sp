import styles from './page.module.css';

export default function Home() {
  return (
    <main className={styles.main}>
      <header className={styles.header}>
        <div className="container">
           <div className={`glass ${styles.headerInner}`}>
             <div className={styles.logo}>ConsultorSEO<span className={styles.accent}>SP</span></div>
             <nav className={styles.nav}>
               <a href="#services">Serviços</a>
               <a href="#sobre">Sobre nós</a>
               <a href="#artigos">Artigos</a>
               <a href="https://wa.me/5511918738164?text=Ol%C3%A1%2C%20vim%20pelo%20site%20e%20gostaria%20de%20saber%20mais%20sobre%20SEO!" target="_blank" rel="noopener noreferrer" className="btn btn-primary">Fale conosco</a>
             </nav>
           </div>
        </div>
      </header>

      <section className={styles.hero}>
        <div className={styles.heroBg}></div>
        <div className={`container ${styles.heroContent}`}>
          <span className={styles.heroSubtitle}>SEO & Branding por Sérgio Melo</span>
          <h1 className={styles.heroTitle}>Somos uma agência de<br/><span className="gradient-text">SEO e BRANDING</span></h1>
          <p className={styles.heroText}>Expanda os negócios da sua marca. Aumente seu tráfego e visibilidade online com serviços de SEO premium.</p>
          <div className={styles.heroActions}>
            <a href="https://wa.me/5511918738164?text=Ol%C3%A1%2C%20vim%20pelo%20site%20e%20gostaria%20de%20saber%20mais%20sobre%20SEO!" target="_blank" rel="noopener noreferrer" className="btn btn-primary">Vamos aparecer?</a>
            <a href="#services" className="btn btn-outline">Nossos Serviços</a>
          </div>
        </div>
      </section>

      <section id="services" className={styles.services}>
        <div className="container">
          <div className={styles.sectionHeader}>
            <h2 className={styles.sectionTitle}>Nossos Serviços</h2>
            <p className={styles.heroText}>Aumente o tráfego do seu site e conquiste mais visibilidade online online com serviços de ponta.</p>
          </div>
          <div className={styles.servicesGrid}>
             <div className={styles.serviceCard}>
                <div className={styles.serviceIcon}>🔍</div>
                <h3 className={styles.serviceTitle}>Consultoria SEO</h3>
                <p className={styles.serviceDesc}>Tenha maior visibilidade online com serviços de SEO altamente eficazes para sua empresa.</p>
             </div>
             <div className={styles.serviceCard}>
                <div className={styles.serviceIcon}>📊</div>
                <h3 className={styles.serviceTitle}>Auditoria de site</h3>
                <p className={styles.serviceDesc}>Analise técnica de mercado e concorrentes para o seu site se posicionar melhor nos rankings.</p>
             </div>
             <div className={styles.serviceCard}>
                <div className={styles.serviceIcon}>✍️</div>
                <h3 className={styles.serviceTitle}>Blogging</h3>
                <p className={styles.serviceDesc}>Criamos artigos otimizados perfeitamente para a palavra-chave que você deseja posicionar.</p>
             </div>
             <div className={styles.serviceCard}>
                <div className={styles.serviceIcon}>📍</div>
                <h3 className={styles.serviceTitle}>Google Local</h3>
                <p className={styles.serviceDesc}>Apareça na frente dos concorrentes no Google Maps localmente e seja conhecido na sua região.</p>
             </div>
             <div className={styles.serviceCard}>
                <div className={styles.serviceIcon}>✨</div>
                <h3 className={styles.serviceTitle}>Branding</h3>
                <p className={styles.serviceDesc}>Fazemos sua marca se fixar por todo o Google e se posicionar de maneira sólida e memorável.</p>
             </div>
             <div className={styles.serviceCard}>
                <div className={styles.serviceIcon}>💻</div>
                <h3 className={styles.serviceTitle}>Desenvolvimento Web</h3>
                <p className={styles.serviceDesc}>Seu site precisa impressionar seus visitantes em poucos segundos. Otimizamos cada interação.</p>
             </div>
          </div>
        </div>
      </section>

      <section id="sobre" className={styles.about}>
        <div className="container">
          <div className={styles.aboutGrid}>
            <div>
              <h2 className={styles.sectionTitle}>Expanda seus negócios com nossa agência</h2>
              <p className={styles.serviceDesc} style={{fontSize: '1.2rem', lineHeight: '1.8'}}>Há mais de 10 anos, a ConsultoriaSEO ajuda empresas a atingirem seus objetivos de marca. Ao longo dos anos, trabalhamos com pessoas, empresas, indústrias e startups inovadoras.</p>
              <br/>
              <p className={styles.serviceDesc} style={{fontSize: '1.2rem', lineHeight: '1.8'}}>Ajudamos marcas ambiciosas como a sua a gerar mais resultado, aumentando o reconhecimento da marca, impulsionando o tráfego e alavancando suas vendas em geral.</p>
            </div>
            <div>
              <blockquote className={styles.aboutQuote}>
                "Tudo começou ajudando pessoas e empresas a se posicionar no Google e Maps de forma genuína, e as sementes que plantamos me trouxeram até aqui."
                <span className={styles.aboutAuthor}>— Sérgio Melo</span>
              </blockquote>
            </div>
          </div>
        </div>
      </section>

      <section id="artigos" className={styles.services} style={{background: 'var(--surface)'}}>
        <div className="container">
          <div className={styles.sectionHeader}>
            <h2 className={styles.sectionTitle}>Conteúdo e Estratégia</h2>
            <p className={styles.heroText}>Acompanhe as últimas tendências de SEO Local e Geotagging.</p>
          </div>
          <div className={styles.articlesGrid}>
            <a href="/artigos/geosetter-o-guia-definitivo-de-geotagging-para-seo-local-em-sao-paulo" className={styles.articleCard}>
              <div className={styles.articleImage} style={{backgroundImage: 'url(/images/artigos/geosetter-seo-local.png)'}}></div>
              <div className={styles.articleInfo}>
                <span className={styles.articleTag}>SEO LOCAL</span>
                <h3 className={styles.articleTitle}>GeoSetter: O Guia Definitivo de Geotagging</h3>
                <p className={styles.articleExcerpt}>Descubra como dominar o Google Maps em SP usando metadados geográficos.</p>
              </div>
            </a>
            <a href="/artigos/como-uma-consultoria-seo-em-sao-paulo-pode-transformar-seu-negocio" className={styles.articleCard}>
              <div className={styles.articleImage} style={{backgroundImage: 'url(/images/artigos/consultoria-seo-hero.png)'}}></div>
              <div className={styles.articleInfo}>
                <span className={styles.articleTag}>CONSULTORIA</span>
                <h3 className={styles.articleTitle}>Transforme seu Negócio com SEO em SP</h3>
                <p className={styles.articleExcerpt}>Estratégias fotorrealistas e futuristas para dominar o tráfego orgânico.</p>
              </div>
            </a>
          </div>
        </div>
      </section>

      <section id="contato" className={styles.services} style={{textAlign: 'center', padding: '12rem 0', position: 'relative'}}>
        <div className="container" style={{position: 'relative', zIndex: 10}}>
          <h2 className={styles.sectionTitle} style={{fontSize: '4.5rem', marginBottom: '1.5rem'}}>Quer posicionar seu site!</h2>
          <p className={styles.heroText} style={{marginBottom: '3rem', fontSize: '1.5rem'}}>Dê o primeiro passo para o sucesso digital e aumente seu faturamento.</p>
          <a href="https://wa.me/5511918738164?text=Ol%C3%A1%2C%20vim%20pelo%20site%20e%20gostaria%20de%20saber%20mais%20sobre%20SEO!" target="_blank" rel="noopener noreferrer" className="btn btn-primary" style={{transform: 'scale(1.2)'}}>Fale com Sérgio Melo</a>
        </div>
      </section>

      <footer className={styles.footer}>
        <div className="container">
          <div className={styles.logo}>ConsultorSEO<span className={styles.accent}>SP</span></div>
          <p className={styles.footerText}>© {new Date().getFullYear()} Consultor SEO SP - Desenvolvido para Sérgio Melo. Todos os direitos reservados.</p>
        </div>
      </footer>
    </main>
  );
}

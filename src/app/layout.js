import { Inter, Outfit } from 'next/font/google'
import './globals.css'

const inter = Inter({ subsets: ['latin'], variable: '--font-body', display: 'swap' })
const outfit = Outfit({ subsets: ['latin'], variable: '--font-heading', display: 'swap' })

export const metadata = {
  title: 'Consultor SEO em São Paulo | Estratégia de SEO e Branding Sérgio Melo',
  description: 'Alavanque sua visibilidade com consultoria de SEO e branding especializada em SP. Foco em resultados de alto impacto para expandir seu negócio online.',
  keywords: 'Consultor SEO SP, Agência de SEO São Paulo, Branding e SEO, Sérgio Melo SEO, Posicionamento Google',
  alternates: {
    canonical: 'https://consultorseosp.com.br/',
  },
  openGraph: {
    title: 'Consultor SEO em São Paulo | Sérgio Melo',
    description: 'Somos uma agência de SEO e BRANDING. Expanda seus negócios garantindo visibilidade online de alto impacto.',
    url: 'https://consultorseosp.com.br/',
    siteName: 'Consultor SEO SP',
    locale: 'pt_BR',
    type: 'website',
  },
  twitter: {
    card: 'summary_large_image',
    title: 'Consultor SEO em São Paulo | Sérgio Melo',
    description: 'Estratégia de SEO e Branding para resultados de alto impacto.',
  },
  verification: {
    google: 'E8QqD0NIqi0P9o2LYCl8FAy9vgJ5Od5xd8VfHu-M3l4',
  },
}

export default function RootLayout({ children }) {
  return (
    <html lang="pt-BR" className={`${inter.variable} ${outfit.variable}`}>
      <body>
        {children}
      </body>
    </html>
  )
}

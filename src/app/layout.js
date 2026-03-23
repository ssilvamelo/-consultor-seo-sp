import { Inter, Outfit } from 'next/font/google'
import './globals.css'

const inter = Inter({ subsets: ['latin'], variable: '--font-body', display: 'swap' })
const outfit = Outfit({ subsets: ['latin'], variable: '--font-heading', display: 'swap' })

export const metadata = {
  title: 'Consultor SEO SP | Sérgio Melo',
  description: 'Somos uma agência de SEO e BRANDING. Expanda seus negócios garantindo visibilidade online de alto impacto.',
  openGraph: {
    title: 'Consultor SEO SP | Sérgio Melo',
    description: 'Somos uma agência de SEO e BRANDING. Expanda seus negócios com serviços personalizados.',
    url: 'https://consultorseosp.com.br/',
    siteName: 'Consultor SEO SP',
    locale: 'pt_BR',
    type: 'website',
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

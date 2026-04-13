import { Outfit } from 'next/font/google'
import Link from 'next/link'

const outfit = Outfit({ subsets: ['latin'], variable: '--font-heading', display: 'swap' })

export default function ArtigoPage({ params }) {
  // Nota: Em um ambiente real, você buscaria os dados do artigo baseado no slug.
  // Como o agente de IA irá gerar páginas estáticas ou arquivos TSX individuais,
  // este arquivo serve como um placeholder ou base.
  
  return (
    <main className={`${outfit.variable} min-h-screen bg-slate-50 p-8`}>
      <article className="max-w-3xl mx-auto bg-white p-12 rounded-2xl shadow-sm">
        <header className="mb-8">
          <Link href="/" className="text-blue-600 hover:underline mb-4 inline-block">
            ← Voltar para Home
          </Link>
          <h1 className="text-4xl font-bold font-heading text-slate-900 capitalize">
            {params.slug.replace(/-/g, ' ')}
          </h1>
        </header>
        
        <div className="prose prose-slate lg:prose-xl">
          <p>O conteúdo deste artigo está sendo processado pela nossa IA...</p>
        </div>
      </article>
    </main>
  )
}

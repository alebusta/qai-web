import { useEffect } from 'react'
import { useParams, Link } from 'react-router-dom'
import { getProposal } from '../propuestas/registry'

const ProposalPage = () => {
  const { slug } = useParams()
  const proposal = getProposal(slug)

  useEffect(() => {
    if (!proposal) return

    document.title = proposal.title

    let robotsMeta = document.querySelector('meta[name="robots"]')
    if (proposal.confidential) {
      if (!robotsMeta) {
        robotsMeta = document.createElement('meta')
        robotsMeta.name = 'robots'
        document.head.appendChild(robotsMeta)
      }
      robotsMeta.content = 'noindex, nofollow'
    }

    return () => {
      document.title = 'The QAI Company'
      if (robotsMeta) {
        robotsMeta.remove()
      }
    }
  }, [proposal])

  if (!proposal) {
    return (
      <div className="flex min-h-screen flex-col items-center justify-center bg-qai-light px-6 text-center text-qai-text">
        <p className="font-mono text-sm uppercase tracking-widest text-gray-500">404</p>
        <h1 className="mt-4 text-2xl font-serif">Propuesta no encontrada</h1>
        <p className="mt-2 max-w-md text-gray-500">
          El enlace no corresponde a una propuesta activa. Verifica la URL o contacta a QAI.
        </p>
        <Link
          to="/"
          className="mt-8 border border-qai-text px-5 py-2 text-sm transition hover:bg-qai-text hover:text-white"
        >
          Ir al inicio
        </Link>
      </div>
    )
  }

  return (
    <iframe
      src={proposal.src}
      title={proposal.title}
      className="fixed inset-0 h-full w-full border-0 bg-white"
    />
  )
}

export default ProposalPage

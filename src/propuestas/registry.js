/**
 * Registro de propuestas compartibles por link directo (/propuestas/:slug).
 * Para agregar una nueva: copiar el HTML a public/propuestas/documents/ y añadir entrada aquí.
 */
export const proposals = {
  'saam-towage': {
    title: 'QAI · Propuesta SAAM Towage — Radar Inteligente',
    client: 'SAAM Towage',
    src: '/propuestas/documents/saam-towage.html',
    confidential: true,
  },
}

export function getProposal(slug) {
  return proposals[slug] ?? null
}

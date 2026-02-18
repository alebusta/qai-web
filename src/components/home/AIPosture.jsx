
import { Check, X } from 'lucide-react'

const AIPosture = () => {
    return (
        <section className="py-24 bg-gray-50 relative overflow-hidden text-gray-900">

            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div className="text-center mb-16">
                    <span className="text-sm font-mono text-gray-900 font-bold uppercase tracking-widest mb-4 block bg-gray-200 inline-block px-2 py-1 rounded">Anti-Hype</span>
                    <h2 className="text-3xl md:text-5xl font-serif font-bold text-black mb-4 leading-tight">
                        Nuestra Postura sobre la IA
                    </h2>
                    <p className="text-xl md:text-2xl text-gray-800 italic max-w-2xl mx-auto font-medium mb-8">
                        Ni apocalípticos ni integrados, pragmáticos. Sin el criterio humano, la IA es solo ruido generativo.
                    </p>
                    <p className="text-lg text-gray-800 max-w-4xl mx-auto font-normal leading-relaxed">
                        Usamos Inteligencia Artificial intensivamente, pero no vendemos promesas mágicas. Conocemos sus capacidades y somos conscientes de sus limitaciones.
                        Por eso, diseñamos procesos bajo el principio de <b>Human-in-the-Loop</b>: La IA genera, procesa y escala, pero el humano juzga, valida y dirige.
                    </p>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-2 gap-12 max-w-5xl mx-auto">
                    {/* Good at */}
                    <div className="bg-white p-8 rounded-2xl border border-gray-100 shadow-sm hover:shadow-md transition-shadow">
                        <h3 className="text-xl font-bold text-gray-900 mb-6 flex items-center">
                            La IA es excepcionalmente buena para:
                        </h3>
                        <ul className="space-y-2">
                            {[
                                "Procesar volúmenes masivos de datos estructurados",
                                "Detectar patrones en información repetitiva",
                                "Automatizar tareas predecibles y bien definidas",
                                "Acelerar la ejecución de procesos especificados"
                            ].map((item, i) => (
                                <li key={i} className="flex items-start text-gray-600 text-base font-light">
                                    <span className="w-1.5 h-1.5 bg-gray-400 rounded-full mt-2 mr-3 flex-shrink-0" />
                                    {item}
                                </li>
                            ))}
                        </ul>
                    </div>

                    {/* Bad at */}
                    <div className="bg-white p-8 rounded-2xl border border-gray-100 shadow-sm hover:shadow-md transition-shadow">
                        <h3 className="text-xl font-bold text-gray-900 mb-6 flex items-center">
                            La IA es excepcionalmente mala para:
                        </h3>
                        <ul className="space-y-2">
                            {[
                                "Entender contexto matizado sin supervisión",
                                "Tomar decisiones estratégicas complejas",
                                "Validar su propia exactitud",
                                "Operar sin consecuencias cuando se equivoca"
                            ].map((item, i) => (
                                <li key={i} className="flex items-start text-gray-600 text-base font-light">
                                    <span className="w-1.5 h-1.5 bg-gray-400 rounded-full mt-2 mr-3 flex-shrink-0" />
                                    {item}
                                </li>
                            ))}
                        </ul>
                    </div>
                </div>

                {/*<div className="mt-16 text-center max-w-3xl mx-auto bg-blue-50 p-8 rounded-2xl border border-blue-100 text-blue-900 shadow-sm">
                    <h4 className="text-lg font-bold mb-2">Human-in-the-Loop</h4>
                    <p className="font-medium leading-relaxed">
                        Por eso, diseñamos procesos bajo el principio de <strong>Human-in-the-Loop</strong>: la IA ejecuta, el humano valida. No sustituimos criterio. Amplificamos capacidad.
                    </p>
                </div>*/}

                <div className="text-center mt-10">
                    <p className="text-[10px] font-mono text-gray-400 uppercase tracking-widest">
                        No sustituimos criterio, amplificamos capacidades. Creemos en la transparencia técnica.
                    </p>
                </div>
            </div>
        </section>
    )
}

export default AIPosture

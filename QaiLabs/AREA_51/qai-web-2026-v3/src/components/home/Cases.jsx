
import { useState } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import { ArrowRight, X } from 'lucide-react'
import { cn } from '../../lib/utils'

const CaseStudy = ({ title, subtitle, problem, friction, solution, result, quote }) => {
    const [isOpen, setIsOpen] = useState(false);

    return (
        <>
            <div className="bg-white rounded-3xl p-8 border border-gray-100 shadow-sm hover:shadow-2xl hover:-translate-y-1 transition-all duration-300 group flex flex-col items-start h-full text-left">
                <h3 className="text-2xl font-serif font-bold text-qai-dark mb-4">{title}</h3>
                <p className="text-gray-500 font-sans font-light leading-relaxed mb-8 flex-grow">
                    {subtitle}
                </p>

                <button
                    onClick={() => setIsOpen(true)}
                    className="px-6 py-2 border border-gray-100 rounded-full text-[10px] font-mono tracking-widest text-gray-400 hover:border-qai-dark hover:text-qai-dark transition-all uppercase"
                >
                    Ver Más
                </button>
            </div>

            <AnimatePresence>
                {isOpen && (
                    <div className="fixed inset-0 z-[100] flex items-center justify-center p-4">
                        <motion.div
                            initial={{ opacity: 0 }}
                            animate={{ opacity: 1 }}
                            exit={{ opacity: 0 }}
                            onClick={() => setIsOpen(false)}
                            className="absolute inset-0 bg-black/60 backdrop-blur-sm"
                        />
                        <motion.div
                            initial={{ opacity: 0, scale: 0.95, y: 20 }}
                            animate={{ opacity: 1, scale: 1, y: 0 }}
                            exit={{ opacity: 0, scale: 0.95, y: 20 }}
                            className="relative bg-white w-full max-w-2xl max-h-[90vh] overflow-y-auto rounded-3xl shadow-2xl z-10"
                        >
                            <button
                                onClick={() => setIsOpen(false)}
                                className="absolute top-6 right-6 p-2 rounded-full hover:bg-gray-100 transition-colors z-[11]"
                            >
                                <X className="w-5 h-5 text-gray-400" />
                            </button>

                            <div className="p-8 md:p-12">
                                <div className="mb-12">
                                    <h3 className="text-3xl font-serif font-bold text-qai-dark mb-4">{title}</h3>
                                    <p className="text-gray-500 font-sans font-light">{subtitle}</p>
                                </div>

                                <div className="space-y-4">
                                    {/* El Problema - Light Gray */}
                                    <div className="bg-gray-50 p-8 rounded-2xl border border-gray-100">
                                        <h4 className="text-xs font-mono uppercase tracking-widest text-gray-400 mb-2 font-bold">El Problema</h4>
                                        <p className="text-sm text-gray-600 font-light leading-relaxed">{problem}</p>
                                    </div>

                                    {/* La Fricción - Medium Gray */}
                                    <div className="bg-gray-100 p-8 rounded-2xl border border-gray-200">
                                        <h4 className="text-xs font-mono uppercase tracking-widest text-gray-500 mb-2 font-bold">La Fricción Económica</h4>
                                        <p className="text-sm text-gray-800 font-medium leading-relaxed">{friction}</p>
                                    </div>

                                    {/* Nuestra Solución - Dark Gray/Black */}
                                    <div className="bg-gray-900 p-8 rounded-2xl text-white">
                                        <h4 className="text-xs font-mono uppercase tracking-widest text-gray-400 mb-4 font-bold">Nuestra Solución</h4>
                                        <ul className="grid grid-cols-1 gap-4">
                                            {solution.map((item, i) => (
                                                <li key={i} className="flex items-start text-sm text-gray-300 font-light">
                                                    <span className="w-1.5 h-1.5 bg-gray-500 rounded-full mt-1.5 mr-3 flex-shrink-0" />
                                                    {item}
                                                </li>
                                            ))}
                                        </ul>
                                    </div>

                                    {/* Resultado */}
                                    <div className="pt-8 space-y-3">
                                        <h4 className="text-xs font-mono uppercase tracking-widest text-gray-400 mb-4 font-bold text-center">Impacto Medible</h4>
                                        <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                                            {result.map((item, i) => (
                                                <div key={i} className="flex items-start p-4 border border-gray-100 rounded-xl bg-white shadow-sm">
                                                    <span className="text-gray-900 mr-3 font-bold">✓</span>
                                                    <span className="text-sm font-medium text-qai-dark">{item}</span>
                                                </div>
                                            ))}
                                        </div>
                                    </div>

                                    {quote && (
                                        <div className="pt-8 text-center">
                                            <p className="text-sm text-gray-500 italic px-8">
                                                "{quote}"
                                            </p>
                                        </div>
                                    )}
                                </div>
                            </div>
                        </motion.div>
                    </div>
                )}
            </AnimatePresence>
        </>
    )
}

const Cases = () => {
    return (
        <section id="cases" className="py-24 bg-gray-50/50">
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div className="text-center mb-12">
                    <span className="text-sm font-mono text-gray-400 uppercase tracking-widest mb-4 block font-bold">Casos de Uso</span>
                    <h2 className="text-3xl md:text-5xl font-serif font-bold text-qai-dark mb-4 leading-tight">
                        Fricción Resuelta
                    </h2>
                    <p className="text-lg text-gray-600 font-light italic">
                        Ineficiencias operativas convertidas en ventaja competitiva. No son soluciones mágicas, <br />es inteligencia artificial aplicada a casos del mundo real.
                    </p>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 mb-1">
                    <CaseStudy
                        title="Matching Inteligente de Documentos"
                        subtitle="IA para extracción de datos más humano para validación de excepciones"
                        problem="Cliente procesa cientos de facturas por mes que debe asociar manualmente. Este proceso requiere un gran volumen de trabajo rutinario humano, potenciales errores en matching y retrasos en pagos a proveedores."
                        friction="Cada factura mal conciliada puede generar disputa con proveedores, retraso en flujo de caja, pérdida de descuentos por pronto pago, y horas de staff administrativo apagando incendios."
                        solution={[
                            "Extrae datos no estructurados de POs e invoices",
                            "Reconciliación automáticamente con alto porcentaje de precisión",
                            "Escala casos ambiguos a revisión humana",
                            "Aprende de correcciones humanas para mejorar continuamente"
                        ]}
                        result={[
                            "90% de reducción en trabajo mecánico (120h → 8h/mes)",
                            "100% de decisiones críticas validadas por humano",
                            "Cero errores en producción (supervisión humana en casos ambiguos)"
                        ]}
                        quote="Esto no es 'IA mágica'. Es ingeniería de procesos con IA."
                    />

                    <CaseStudy
                        title="Gestión Inteligente de Comunidades"
                        subtitle="Sistema de gestión de condominios asistido por IA"
                        problem="Administradores gestionando edificios con: comunicación fragmentada (WhatsApp, email, llamadas), presupuestos en Excel compartidos por correo, sistemas de gestión complejos e incompletos que dificultan el seguimiento de los gastos de una comunidad."
                        friction="Desconfianza, morosidad, potenciales conflictos vecinales y tiempo excesivo del administrador en tareas manuales repetitivas que dificultan su gestión."
                        solution={[
                            "Plataforma que simplifica la gestión de una comunidad, el seguimiento y monitoreo de los gastos comunes, y la comunicación.",
                            "Reportería automática basada en IA y de acceso en tiempo real.",
                            "Rendición de cuentas para todas las partes."
                        ]}
                        result={[
                            "70% menos tiempo administrativo (tareas repetitivas automatizadas)",
                            "100% transparencia para residentes",
                            "Reducción del 30% en morosidad (mayor confianza = mejor pago)"
                        ]}
                        quote="Estado: Beta con 3 comunidades. Validando modelo de escalamiento."
                    />

                    <CaseStudy
                        title="Sistemas de Vigilancia Estratégica"
                        subtitle="Radar de vigilancia tecnológica y anticipación inteligente"
                        problem="Organizaciones que operan con 'puntos ciegos' respecto a competidores, regulación o startups. Los informes tradicionales son estáticos, caros y quedan obsoletos rápidamente."
                        friction="La falta de anticipación genera reacciones tardías, pérdida de competitividad y duplicación de esfuerzos al evaluar tecnologías que ya fueron descartadas por otros equipos."
                        solution={[
                            "Radar Vivo 24/7 con ingesta masiva de noticias, patentes y mercados",
                            "IA para filtrado semántico de señales de ruido",
                            "Validación experta (Human-in-the-loop) para asegurar impacto operativo",
                            "Memoria Institucional centralizada para consultas históricas"
                        ]}
                        result={[
                            "Anticipación real de riesgos regulatorios y tecnológicos",
                            "30% de ahorro vs consultoría estática tradicional",
                            "Memoria centralizada que evita duplicidad de evaluaciones"
                        ]}
                        quote="No es buscar información, es filtrar el ruido para encontrar señales accionables."
                    />
                </div>

                {/* Subtle Footer-style CTA */}
                <div className="pt-10 text-center max-w-5xl mx-auto">
                    <h3 className="text-xl font-serif font-bold text-qai-dark mb-4">
                        ¿Tu Organización Tiene Otro Desafío?
                    </h3>
                    <p className="text-gray-500 font-sans font-light text-base mb-8 leading-relaxed italic">
                        Si tu empresa tiene procesos manuales repetitivos, datos que nadie puede usar para decidir, o fricción operativa... podemos ayudarte.
                    </p>
                    <div className="flex flex-col items-center gap-6">
                        <a
                            href="mailto:hola@theqai.co"
                            className="group flex items-center gap-3 px-8 py-4 bg-qai-dark text-white rounded-full font-medium text-sm hover:bg-black transition-all shadow-lg"
                        >
                            Describir tu Caso
                            <ArrowRight className="w-4 h-4 ml-2" />
                        </a>
                        <p className="text-[10px] font-mono text-gray-400 uppercase tracking-widest">
                            No todas las ineficiencias son automatizables. Pero cuando lo son, el retorno puede ser significativo.
                        </p>
                    </div>
                </div>
            </div>
        </section>
    )
}

export default Cases

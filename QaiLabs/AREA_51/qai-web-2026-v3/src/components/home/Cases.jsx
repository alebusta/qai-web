
import { useState } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import { ArrowRight, X, ChevronLeft, ChevronRight } from 'lucide-react'

// Fondos progresivos: de púrpura muy tenue → cian más intenso
const slideStyles = [
    {
        bg: 'rgba(155, 111, 212, 0.06)',
        border: 'rgba(155, 111, 212, 0.15)',
        accent: '#9B6FD4',
        label: 'El Problema',
    },
    {
        bg: 'rgba(130, 100, 220, 0.10)',
        border: 'rgba(130, 100, 220, 0.20)',
        accent: '#8264DC',
        label: 'La Fricción Económica',
    },
    {
        bg: 'rgba(77, 190, 210, 0.10)',
        border: 'rgba(77, 190, 210, 0.20)',
        accent: '#4DBED2',
        label: 'Nuestra Solución',
    },
    {
        bg: 'rgba(77, 217, 224, 0.14)',
        border: 'rgba(77, 217, 224, 0.25)',
        accent: '#4DD9E0',
        label: 'Impacto Medible',
    },
]

const CaseStudy = ({ title, subtitle, problem, friction, solution, result, quote }) => {
    const [isOpen, setIsOpen] = useState(false)
    const [slide, setSlide] = useState(0)
    const [direction, setDirection] = useState(1)

    const slides = [
        {
            content: (
                <p className="text-base text-gray-700 font-light leading-relaxed">{problem}</p>
            )
        },
        {
            content: (
                <p className="text-base text-gray-800 font-medium leading-relaxed">{friction}</p>
            )
        },
        {
            content: (
                <ul className="space-y-3">
                    {solution.map((item, i) => (
                        <li key={i} className="flex items-start text-base text-gray-700 font-light">
                            <span
                                className="w-1.5 h-1.5 rounded-full mt-1.5 mr-3 flex-shrink-0"
                                style={{ backgroundColor: slideStyles[2].accent }}
                            />
                            {item}
                        </li>
                    ))}
                </ul>
            )
        },
        {
            content: (
                <div className="space-y-3">
                    {result.map((item, i) => (
                        <div key={i} className="flex items-start p-3 rounded-xl bg-white/60 border border-white/80">
                            <span className="font-bold mr-3 text-sm" style={{ color: slideStyles[3].accent }}>✓</span>
                            <span className="text-base font-medium text-gray-800">{item}</span>
                        </div>
                    ))}
                    {quote && (
                        <p className="text-[10px] font-mono text-gray-400 uppercase tracking-widest pt-2 text-center">
                            {quote}
                        </p>
                    )}
                </div>
            )
        },
    ]

    const goTo = (next) => {
        setDirection(next > slide ? 1 : -1)
        setSlide(next)
    }

    const variants = {
        enter: (dir) => ({ x: dir > 0 ? 60 : -60, opacity: 0 }),
        center: { x: 0, opacity: 1 },
        exit: (dir) => ({ x: dir > 0 ? -60 : 60, opacity: 0 }),
    }

    const style = slideStyles[slide]

    return (
        <>
            <div className="bg-white rounded-3xl p-8 border border-gray-100 shadow-sm hover:shadow-2xl hover:-translate-y-1 transition-all duration-300 group flex flex-col items-start h-full text-left">
                <h3 className="text-2xl font-serif font-bold text-qai-dark mb-4">{title}</h3>
                <p className="text-gray-500 font-sans font-light leading-relaxed mb-8 flex-grow">
                    {subtitle}
                </p>
                <button
                    onClick={() => { setIsOpen(true); setSlide(0) }}
                    className="px-6 py-2 border-2 border-gray-200 rounded-full text-[10px] font-mono tracking-widest text-gray-400 hover:border-qai-dark hover:text-qai-dark transition-all uppercase"
                >
                    Ver Más
                </button>
            </div>

            <AnimatePresence>
                {isOpen && (
                    <div className="fixed inset-0 z-[100] flex items-center justify-center p-4">
                        {/* Backdrop */}
                        <motion.div
                            initial={{ opacity: 0 }}
                            animate={{ opacity: 1 }}
                            exit={{ opacity: 0 }}
                            onClick={() => setIsOpen(false)}
                            className="absolute inset-0 bg-black/50 backdrop-blur-sm"
                        />

                        {/* Modal */}
                        <motion.div
                            initial={{ opacity: 0, scale: 0.95, y: 20 }}
                            animate={{ opacity: 1, scale: 1, y: 0 }}
                            exit={{ opacity: 0, scale: 0.95, y: 20 }}
                            className="relative w-full max-w-xl z-10 rounded-3xl overflow-hidden shadow-2xl"
                            style={{
                                background: style.bg,
                                border: `1px solid ${style.border}`,
                                backdropFilter: 'blur(20px)',
                                transition: 'background 0.5s ease, border-color 0.5s ease',
                            }}
                        >
                            {/* Glassmorphism base */}
                            <div className="absolute inset-0 bg-white/75 backdrop-blur-xl -z-10 rounded-3xl" />

                            {/* Header */}
                            <div className="px-8 pt-8 pb-4">
                                <div className="flex items-start justify-between mb-1">
                                    <div>
                                        <h3 className="text-xl font-serif font-bold text-qai-dark">{title}</h3>
                                        <p className="text-xs text-gray-400 font-light">{subtitle}</p>
                                    </div>
                                    <button
                                        onClick={() => setIsOpen(false)}
                                        className="p-2 rounded-full hover:bg-black/5 transition-colors ml-4 flex-shrink-0"
                                    >
                                        <X className="w-4 h-4 text-gray-400" />
                                    </button>
                                </div>

                                {/* Progress pills */}
                                <div className="flex items-center gap-3 mt-4">
                                    <span
                                        className="text-xs font-mono font-semibold uppercase tracking-widest transition-colors duration-300"
                                        style={{ color: style.accent }}
                                    >
                                        {style.label}
                                    </span>
                                    <div className="ml-auto flex items-center gap-2">
                                        {slideStyles.map((s, i) => (
                                            <button
                                                key={i}
                                                onClick={() => goTo(i)}
                                                className="h-1 rounded-full transition-all duration-300"
                                                style={{
                                                    width: i === slide ? '2rem' : '0.5rem',
                                                    backgroundColor: i === slide ? s.accent : '#D1D5DB',
                                                }}
                                            />
                                        ))}
                                    </div>
                                </div>
                            </div>

                            {/* Slide content */}
                            <div className="px-8 pb-8 h-[260px] relative overflow-hidden">
                                <AnimatePresence custom={direction} mode="wait">
                                    <motion.div
                                        key={slide}
                                        custom={direction}
                                        variants={variants}
                                        initial="enter"
                                        animate="center"
                                        exit="exit"
                                        transition={{ duration: 0.3, ease: 'easeInOut' }}
                                    >
                                        {slides[slide].content}
                                    </motion.div>
                                </AnimatePresence>
                            </div>

                            {/* Navigation */}
                            <div className="px-8 pb-6 flex items-center justify-between border-t border-black/5 pt-4">
                                <button
                                    onClick={() => goTo(slide - 1)}
                                    disabled={slide === 0}
                                    className="flex items-center gap-1 text-xs font-mono text-gray-400 hover:text-gray-700 disabled:opacity-20 transition-all uppercase tracking-widest"
                                >
                                    <ChevronLeft className="w-3 h-3" /> Anterior
                                </button>
                                <span className="text-[10px] font-mono text-gray-300">{slide + 1} / {slides.length}</span>
                                <button
                                    onClick={() => slide < slides.length - 1 ? goTo(slide + 1) : setIsOpen(false)}
                                    className="flex items-center gap-1 text-xs font-mono hover:opacity-70 transition-all uppercase tracking-widest font-medium"
                                    style={{ color: style.accent }}
                                >
                                    {slide < slides.length - 1 ? 'Siguiente' : 'Cerrar'}
                                    {slide < slides.length - 1 && <ChevronRight className="w-3 h-3" />}
                                </button>
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

                {/* CTA */}
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
                            className="btn-qai-primary group flex items-center gap-3 px-8 py-4 rounded-full font-medium text-sm"
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


import { motion } from 'framer-motion'

const ProcessCard = ({ number, title, desc, delay, time }) => {
    return (
        <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.6, delay }}
            className="group relative bg-white p-8 rounded-2xl border border-gray-100 shadow-sm hover:shadow-lg hover:-translate-y-2 transition-all duration-300 h-full flex flex-col items-center text-center"
        >
            <div className="process-number text-6xl font-mono font-bold mb-6">
                {number}
            </div>

            <h3 className="text-xl font-bold text-qai-dark mb-4 font-serif">{title}</h3>

            <p className="text-gray-600 font-light leading-relaxed text-sm flex-grow">
                {desc}
            </p>

            <div className="mt-6 pt-4 border-t border-gray-50 w-full">
                <span className="text-xs font-mono uppercase tracking-widest text-gray-400 group-hover:text-qai-dark group-hover:font-bold transition-all duration-300">
                    Tiempo: {time}
                </span>
            </div>
        </motion.div>
    )
}

const HowWeWork = () => {
    return (
        <section id="how-we-work" className="py-24 bg-white relative">
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div className="text-center mb-16">
                    <span className="text-sm font-mono text-gray-400 uppercase tracking-widest mb-4 block">Metodología</span>
                    <h2 className="text-3xl md:text-5xl font-serif font-bold text-qai-dark mb-6 leading-tight">
                        Cómo Trabajamos
                    </h2>
                    <p className="text-lg text-gray-600 max-w-3xl mx-auto font-light">
                        Combinamos rigor de laboratorio con velocidad de ejecución sin sacrificar el juicio crítico que solo el expertise humano puede aportar.
                    </p>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-3 gap-8 mb-8 relative">
                    {/* Connector lines (Desktop only) */}
                    <div className="hidden md:block absolute top-[28%] left-[16%] w-[68%] h-px bg-gradient-to-r from-gray-200 via-gray-300 to-gray-200 -z-0" />

                    <ProcessCard
                        number="01"
                        title="Diagnóstico"
                        desc="No empezamos con tecnología. Empezamos con tu problema. ¿Cuál es la fricción? ¿Cuánto valor se pierde? ¿Dónde está el cuello de botella real? Resultado: Una hipótesis clara y un ROI estimado antes de escribir código."
                        time="1-2 semanas"
                        delay={0.1}
                    />
                    <ProcessCard
                        number="02"
                        title="Prototipo Científico"
                        desc="Construimos un experimento funcional con tus datos reales. No un mockup, no un demo. Un sistema que trabaja. Resultado: Validación empírica de que la solución funciona con tu operación específica."
                        time="3-6 semanas"
                        delay={0.2}
                    />
                    <ProcessCard
                        number="03"
                        title="Producción & Evolución"
                        desc="Desplegamos, monitoreamos y refinamos basados en uso real. Los sistemas no se 'terminan', se mejoran continuamente con feedback operativo. Resultado: Una solución viva que se adapta a tu operación."
                        time="Continuo"
                        delay={0.3}
                    />
                </div>

                <p className="text-[11px] font-mono text-gray-400 uppercase tracking-widest text-center leading-relaxed">
                    Tú tienes el expertise, la IA tiene la velocidad. · Tú defines el criterio, la IA ejecuta el proceso. · Tú validas el resultado, la IA escala la operación.
                </p>
                {/*<div className="grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                        <ul className="space-y-4">
                            <li className="flex items-start">
                                <span className="w-1.5 h-1.5 bg-qai-dark rounded-full mt-2 mr-3 flex-shrink-0" />
                                <p className="text-gray-700 font-light text-sm">Tú tienes el expertise, <strong>la IA tiene la velocidad.</strong></p>
                            </li>
                            <li className="flex items-start">
                                <span className="w-1.5 h-1.5 bg-qai-dark rounded-full mt-2 mr-3 flex-shrink-0" />
                                <p className="text-gray-700 font-light text-sm">Tú defines el criterio, <strong>la IA ejecuta el proceso.</strong></p>
                            </li>
                            <li className="flex items-start">
                                <span className="w-1.5 h-1.5 bg-qai-dark rounded-full mt-2 mr-3 flex-shrink-0" />
                                <p className="text-gray-700 font-light text-sm">Tú validas el resultado, <strong>la IA escala la operación.</strong></p>
                            </li>
                        </ul>
                        <div className="space-y-4">
                            <p className="text-lg italic text-gray-500 font-serif leading-relaxed text-center md:text-left border-l-2 border-gray-200 pl-6">
                                "La IA nos permite operar con la eficiencia de equipos grandes mientras mantenemos la agilidad de equipos pequeños."
                            </p>
                            <p className="text-lg italic text-gray-500 font-serif leading-relaxed text-center md:text-left border-l-2 border-gray-200 pl-6">
                                "No es 'IA en vez de humanos'. Es 'IA + humanos = más capacidad con menos fricción'."
                            </p>
                            <p className="text-sm text-gray-400">
                                Resultado: Velocidad de ejecución sin sacrificar el juicio crítico que solo el expertise humano puede aportar. La tecnología es el medio. Tu problema resuelto es el fin.
                            </p>
                        </div>
                    </div>*/}
            </div>
        </section>
    )
}

export default HowWeWork

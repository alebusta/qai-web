
import { motion } from 'framer-motion'
import { FlaskConical, Zap, Scale } from 'lucide-react'

const Tag = ({ word, tooltip }) => (
    <span className="relative inline-block group cursor-default">
        <span className="hover:text-gray-600 transition-colors duration-200">
            {word}
        </span>
        {/* Tooltip */}
        <span className="
            pointer-events-none absolute bottom-full left-1/2 -translate-x-1/2 mb-3
            w-56 px-4 py-3 rounded-xl
            bg-white border border-gray-100 shadow-lg
            text-[10px] font-sans font-normal normal-case tracking-normal text-gray-500 leading-relaxed text-left
            opacity-0 group-hover:opacity-100
            translate-y-1 group-hover:translate-y-0
            transition-all duration-200 ease-out
            z-50
        ">
            {tooltip}
            {/* Arrow */}
            <span className="absolute top-full left-1/2 -translate-x-1/2 border-4 border-transparent border-t-gray-100" />
        </span>
    </span>
)

const About = () => {
    return (
        <section id="about" className="py-24 bg-white relative overflow-hidden">
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div className="max-w-4xl mx-auto text-center mb-16">
                    <span className="text-sm font-mono text-gray-400 uppercase tracking-widest mb-4 block">Identidad</span>
                    <h2 className="text-3xl md:text-5xl font-serif font-bold text-qai-dark mb-6 leading-tight">
                        Un Laboratorio de arquitectura de soluciones <br />
                        {/* <span className="text-gray-500 italic font-light">No una Consultora</span> */}
                    </h2>

                    <p className="text-lg md:text-xl text-gray-600 font-light leading-relaxed mb-8">
                        QAI nace como respuesta pragmática a la era de la IA. No somos una consultora tradicional vendiendo horas-hombre. Somos un laboratorio boutique que combina:
                    </p>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-3 gap-8 mb-8">
                    <div className="card-qai-border p-8 bg-gray-50 rounded-2xl">
                        <h3 className="text-xl font-bold text-qai-dark mb-3">Expertise en dominios <br />complejos</h3>
                        <p className="text-gray-600 leading-relaxed font-light text-sm">
                            Priorizamos calidad sobre cantidad. Ejecución sobre planificación. Valor tangible sobre complejidad innecesaria. Donde otros ven código, nosotros vemos el potencial de generar valor.
                        </p>
                    </div>
                    <div className="card-qai-border p-8 bg-gray-50 rounded-2xl">
                        <h3 className="text-xl font-bold text-qai-dark mb-3">Capacidad de ejecución acelerada</h3>
                        <p className="text-gray-600 leading-relaxed font-light text-sm">
                            La IA nos permite operar con la eficiencia de equipos grandes mientras mantenemos la agilidad de equipos pequeños.
                        </p>
                    </div>
                    <div className="card-qai-border p-8 bg-gray-50 rounded-2xl">
                        <h3 className="text-xl font-bold text-qai-dark mb-3">Humildad científica</h3>
                        <p className="text-gray-600 leading-relaxed font-light text-sm">
                            Validamos con datos, no con promesas. Rigor científico aplicado al negocio. Te decimos qué hace la tecnología, sus limitaciones, y por qué elegimos cada herramienta. No ocultamos complejidad para parecer mágicos.
                        </p>
                    </div>
                </div>

                <div className="text-center max-w-3xl mx-auto border-t border-gray-100 pt-6">
                    <p className="text-sm font-mono text-gray-400 uppercase tracking-widest flex items-center justify-center gap-2 flex-wrap">
                        <Tag
                            word="Bootstrapped"
                            tooltip="Sin inversión externa. Crecemos con lo que generamos. Cada decisión responde a valor real, no a métricas de vanidad para un VC."
                        />
                        <span className="text-gray-300">·</span>
                        <Tag
                            word="Independiente"
                            tooltip="Sin accionistas que dicten el roadmap. Elegimos los clientes y proyectos en los que creemos. Nuestra única lealtad es con el resultado."
                        />
                        <span className="text-gray-300">·</span>
                        <Tag
                            word="En Santiago de Chile"
                            tooltip="Desde Santiago para organizaciones locales, globales, de cualquier tamaño y en cualquier lugar. La geografía no limita el impacto."
                        />
                    </p>
                </div>
            </div>
        </section>
    )
}

export default About


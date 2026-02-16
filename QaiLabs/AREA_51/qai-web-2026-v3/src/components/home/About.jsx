
import { motion } from 'framer-motion'
import { FlaskConical, Zap, Scale } from 'lucide-react'

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

                    {/* <p className="text-lg md:text-xl text-gray-600 font-light leading-relaxed">
                        Somos un laboratorio boutique que combina:
                    </p> */}
                </div>

                <div className="grid grid-cols-1 md:grid-cols-3 gap-8 mb-8">
                    <div className="p-8 bg-gray-50 rounded-2xl border border-gray-100 hover:border-gray-200 transition-colors">
                        {/*<FlaskConical className="w-8 h-8 text-qai-dark mb-4 stroke-1" />*/}
                        <h3 className="text-xl font-bold text-qai-dark mb-3">Expertise en dominios <br />complejos</h3>
                        <p className="text-gray-600 leading-relaxed font-light text-sm">
                            Priorizamos calidad sobre cantidad. Ejecución sobre planificación. Valor tangible sobre complejidad innecesaria. Donde otros ven código, nosotros vemos el potencial de generar valor.
                        </p>
                    </div>
                    <div className="p-8 bg-gray-50 rounded-2xl border border-gray-100 hover:border-gray-200 transition-colors">
                        {/*<Zap className="w-8 h-8 text-qai-dark mb-4 stroke-1" />*/}
                        <h3 className="text-xl font-bold text-qai-dark mb-3">Capacidad de ejecución acelerada</h3>
                        <p className="text-gray-600 leading-relaxed font-light text-sm">
                            La IA nos permite operar con la eficiencia de equipos grandes mientras mantenemos la agilidad de equipos pequeños.
                        </p>
                    </div>
                    <div className="p-8 bg-gray-50 rounded-2xl border border-gray-100 hover:border-gray-200 transition-colors">
                        {/*<Scale className="w-8 h-8 text-qai-dark mb-4 stroke-1" />*/}
                        <h3 className="text-xl font-bold text-qai-dark mb-3">Humildad científica</h3>
                        <p className="text-gray-600 leading-relaxed font-light text-sm">
                            Validamos con datos, no con promesas. Rigor científico aplicado al negocio. Te decimos qué hace la tecnología, sus limitaciones, y por qué elegimos cada herramienta. No ocultamos complejidad para parecer mágicos.
                        </p>
                    </div>
                </div>

                <div className="text-center max-w-3xl mx-auto border-t border-gray-100 pt-6">
                    {/*<p className="text-lg text-gray-800 font-normal mb-8 leading-relaxed">
                        Operamos bajo una filosofía simple:
                    </p>
                    <p className="text-xl font-serif italic text-gray-800 mb-8 leading-relaxed">
                        "Calidad sobre cantidad. Ejecución sobre planificación. Valor tangible sobre complejidad innecesaria. Donde otros ven código, nosotros vemos el potencial de generar valor."
                    </p>*/}
                    <p className="text-sm font-mono text-gray-400 uppercase tracking-widest">
                        Bootstrapped. Independiente. Desde Santiago de Chile para organizaciones locales, globales de cualquier tamaño y en cualquier lugar.
                    </p>
                </div>
            </div>
        </section>
    )
}

export default About

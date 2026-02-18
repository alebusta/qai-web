
import { motion } from 'framer-motion'
import { ArrowRight, ChevronDown } from 'lucide-react'

const Hero = () => {
    return (
        <section className="relative min-h-[90vh] flex items-center justify-center overflow-hidden bg-qai-light">

            <div className="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center z-10 pt-20">
                <motion.div
                    initial={{ opacity: 0, y: 20 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ duration: 0.8, ease: "easeOut" }}
                    className="space-y-8"
                >
                    <h1 className="text-5xl md:text-7xl font-serif font-bold text-qai-dark tracking-tight leading-[1.1]">
                        Arquitectura de Soluciones <br />
                        <span className="italic font-light text-gray-800">
                            Impulsadas por IA
                        </span>
                    </h1>

                    <p className="text-xl md:text-2xl text-gray-600 max-w-4xl mx-auto font-sans font-light leading-relaxed">
                        Reducimos la fricción operativa en organizaciones que buscan eficiencia sin complejidad innecesaria. Convertimos datos caóticos en sistemas de inteligencia que amplifican capacidades y eliminan ineficiencias.
                    </p>

                    <motion.div
                        initial={{ opacity: 0, y: 10 }}
                        animate={{ opacity: 1, y: 0 }}
                        transition={{ delay: 0.4, duration: 0.6 }}
                        className="flex flex-col sm:flex-row items-center justify-center gap-4 pt-8"
                    >
                        <a
                            href="#cases"
                            className="btn-qai-primary px-8 py-4 rounded-full font-medium text-lg flex items-center group"
                        >
                            Ver Casos Reales
                            <ArrowRight className="ml-2 h-5 w-5 group-hover:translate-x-1 transition-transform" />
                        </a>
                        <a
                            href="#manifesto"
                            className="px-8 py-4 bg-white text-qai-dark border border-gray-200 rounded-full font-medium text-lg hover:border-gray-900 transition-all hover:bg-gray-50"
                        >
                            Nuestra Filosofía
                        </a>
                    </motion.div>

                    <p className="text-[10px] font-mono text-gray-400 uppercase tracking-widest pt-2">
                        No vendemos tecnología mágica. Vendemos problemas resueltos con herramientas apropiadas.
                    </p>
                </motion.div>
            </div>

            {/* Scroll indicator */}
            <motion.div
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                transition={{ delay: 1, duration: 1 }}
                className="absolute bottom-10 left-1/2 -translate-x-1/2 cursor-pointer"
                onClick={() => document.getElementById('about').scrollIntoView({ behavior: 'smooth' })}
            >
                <div className="w-6 h-10 flex justify-center p-1">
                    <ChevronDown className="w-6 h-6 text-gray-400 animate-bounce" />
                </div>
            </motion.div>

        </section>
    )
}

export default Hero

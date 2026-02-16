
import { motion } from 'framer-motion'
import { ArrowRight } from 'lucide-react'

const Hero = () => {
    return (
        <section className="relative min-h-[90vh] flex items-center justify-center overflow-hidden">
            {/* Background Elements */}
            <div className="absolute inset-0 bg-qai-light">
                <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[800px] h-[800px] bg-white rounded-full blur-3xl opacity-50 mix-blend-multiply filter pointer-events-none" />
                <div className="absolute top-0 right-0 w-[600px] h-[600px] bg-blue-50/30 rounded-full blur-3xl mix-blend-multiply filter pointer-events-none" />
            </div>

            <div className="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center z-10">
                <motion.div
                    initial={{ opacity: 0, y: 20 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ duration: 0.8, ease: "easeOut" }}
                    className="space-y-8"
                >
                    <h1 className="text-5xl md:text-7xl font-serif font-bold text-qai-dark tracking-tight leading-tight">
                        El Humano en el Centro, <br />
                        <span className="italic font-light">
                            la IA como Palanca
                        </span>
                    </h1>

                    <p className="text-xl md:text-2xl text-qai-subtext max-w-3xl mx-auto font-light leading-relaxed">
                        Soluciones de calidad que mejoran vidas y organizaciones, impulsadas por IA, con pragmatismo y excelencia.
                    </p>

                    <motion.div
                        initial={{ opacity: 0, y: 10 }}
                        animate={{ opacity: 1, y: 0 }}
                        transition={{ delay: 0.4, duration: 0.6 }}
                        className="flex flex-col sm:flex-row items-center justify-center gap-4 pt-4"
                    >
                        <a
                            href="#manifesto"
                            className="px-8 py-4 bg-qai-dark text-white rounded-full font-medium text-lg hover:bg-black transition-all transform hover:scale-105 shadow-lg flex items-center group"
                        >
                            Nuestra Filosofía
                            <ArrowRight className="ml-2 h-5 w-5 group-hover:translate-x-1 transition-transform" />
                        </a>
                        <a
                            href="#contact"
                            className="px-8 py-4 bg-white text-qai-dark border border-gray-200 rounded-full font-medium text-lg hover:border-gray-400 transition-all hover:bg-gray-50"
                        >
                            Hablemos
                        </a>
                    </motion.div>
                </motion.div>
            </div>

            {/* Scroll indicator */}
            <motion.div
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                transition={{ delay: 1, duration: 1 }}
                className="absolute bottom-10 left-1/2 -translate-x-1/2"
            >
                <div className="w-6 h-10 border-2 border-gray-300 rounded-full flex justify-center p-1">
                    <motion.div
                        animate={{ y: [0, 12, 0] }}
                        transition={{ repeat: Infinity, duration: 1.5, ease: "easeInOut" }}
                        className="w-1.5 h-1.5 bg-gray-400 rounded-full"
                    />
                </div>
            </motion.div>
        </section>
    )
}

export default Hero

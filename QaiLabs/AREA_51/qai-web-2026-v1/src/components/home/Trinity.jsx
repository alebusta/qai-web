
import { motion } from 'framer-motion'
import { Brain, FlaskConical, Rocket } from 'lucide-react'

const TrinityCard = ({ icon: Icon, title, subtitle, desc, delay }) => {
    return (
        <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.6, delay }}
            className="bg-white p-8 rounded-2xl border border-gray-100 shadow-sm hover:shadow-md transition-shadow relative overflow-hidden group"
        >
            <div className="absolute top-0 right-0 -mt-4 -mr-4 w-24 h-24 bg-gray-50 rounded-full group-hover:scale-150 transition-transform duration-500 ease-in-out z-0" />
            <div className="relative z-10">
                <div className="w-12 h-12 bg-qai-light rounded-xl flex items-center justify-center mb-6 text-qai-dark">
                    <Icon className="w-6 h-6 stroke-1" />
                </div>
                <h3 className="text-2xl font-display font-bold text-qai-dark mb-1">{title}</h3>
                <span className="text-xs font-mono uppercase tracking-widest text-gray-400 mb-4 block">{subtitle}</span>
                <p className="text-gray-600 font-light leading-relaxed">
                    {desc}
                </p>
            </div>
        </motion.div>
    )
}

const Trinity = () => {
    return (
        <section id="how-we-work" className="py-24 bg-white">
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div className="text-center mb-16">
                    <h2 className="text-3xl md:text-4xl font-display font-bold text-qai-dark mb-4">Nuestro Motor</h2>
                    <p className="text-lg text-gray-600 max-w-2xl mx-auto">
                        De la investigación aplicada a soluciones robustas. Un proceso continuo que transforma estrategia en realidad.
                    </p>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-3 gap-8 relative">
                    {/* Connector lines (Desktop only) */}
                    <div className="hidden md:block absolute top-1/2 left-0 w-full h-0.5 bg-gradient-to-r from-transparent via-gray-200 to-transparent -z-0 -translate-y-8" />

                    <TrinityCard
                        icon={Brain}
                        title="TheQai"
                        subtitle="Estrategia"
                        desc="El cerebro que define el rumbo. Gestión estratégica y financiera que asegura la viabilidad y el propósito de cada iniciativa."
                        delay={0.1}
                    />
                    <TrinityCard
                        icon={FlaskConical}
                        title="QaiLabs"
                        subtitle="Innovación (R&D)"
                        desc="El laboratorio donde rompemos cosas para aprender. Investigación aplicada y experimentación rápida para validar el futuro."
                        delay={0.2}
                    />
                    <TrinityCard
                        icon={Rocket}
                        title="QaiProd"
                        subtitle="Solución"
                        desc="La cara al cliente. Transformamos experimentos exitosos en productos y servicios escalables, robustos y sin fricción."
                        delay={0.3}
                    />
                </div>
            </div>
        </section>
    )
}

export default Trinity

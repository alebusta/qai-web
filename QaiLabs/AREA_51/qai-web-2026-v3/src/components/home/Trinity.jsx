
import { motion } from 'framer-motion'

const TrinityCard = ({ number, title, subtitle, desc, delay }) => {
    return (
        <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.6, delay }}
            className="bg-gray-50 p-8 rounded-[24px] relative overflow-hidden group h-full"
        >
            <div className="relative z-10">
                <div className="text-4xl font-mono font-medium text-gray-200 mb-6">
                    {number}
                </div>
                <h3 className="text-2xl font-serif font-bold text-qai-dark mb-1 tracking-tight">{title}</h3>
                <span className="text-xs font-mono uppercase tracking-widest text-gray-400 mb-4 block">{subtitle}</span>
                <p className="text-gray-600 font-light leading-relaxed text-sm">
                    {desc}
                </p>
            </div>
        </motion.div>
    )
}

const Trinity = () => {
    return (
        <section id="how-we-work" className="py-24 bg-white relative">
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div className="text-center mb-16">
                    <h2 className="text-3xl md:text-4xl font-serif font-bold text-qai-dark mb-4 tracking-tight">Nuestro Motor</h2>
                    <p className="text-lg text-gray-600 max-w-2xl mx-auto font-light">
                        De la investigación aplicada a soluciones robustas.
                    </p>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-3 gap-6 relative">
                    <TrinityCard
                        number="01"
                        title="TheQai"
                        subtitle="Estrategia"
                        desc="El cerebro que define el rumbo. Gestión estratégica y financiera que asegura la viabilidad y el propósito de cada iniciativa."
                        delay={0.1}
                    />
                    <TrinityCard
                        number="02"
                        title="QaiLabs"
                        subtitle="Innovación (R&D)"
                        desc="El laboratorio donde rompemos cosas para aprender. Investigación aplicada y experimentación rápida para validar el futuro."
                        delay={0.2}
                    />
                    <TrinityCard
                        number="03"
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

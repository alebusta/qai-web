
import { motion } from 'framer-motion'
import { FileText, Briefcase, Lightbulb } from 'lucide-react'

const SolutionCard = ({ icon: Icon, title, desc, link }) => {
    return (
        <div className="group bg-gray-50 rounded-2xl p-8 hover:bg-white hover:shadow-xl transition-all duration-300 border border-transparent hover:border-gray-100">
            <div className="w-12 h-12 bg-white rounded-xl shadow-sm flex items-center justify-center mb-6 text-qai-dark group-hover:bg-qai-dark group-hover:text-white transition-colors">
                <Icon className="w-6 h-6" />
            </div>
            <h3 className="text-xl font-bold text-qai-dark mb-3">{title}</h3>
            <p className="text-gray-600 mb-6 leading-relaxed">
                {desc}
            </p>
            <button className="inline-flex items-center text-sm font-medium text-gray-400 cursor-not-allowed">
                Próximamente
            </button>
        </div>
    )
}

const Solutions = () => {
    return (
        <section id="solutions" className="py-24 bg-white">
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div className="text-center mb-16">
                    <span className="text-sm font-mono text-qai-blue uppercase tracking-widest mb-2 block">Impacto Real</span>
                    <h2 className="text-3xl md:text-5xl font-display font-bold text-qai-dark mb-4">
                        Automatizar lo rutinario para <br className="hidden md:block" /> potenciar lo humano.
                    </h2>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
                    <SolutionCard
                        icon={FileText}
                        title="Gestión Financiera Inteligente"
                        desc="Conciliación bancaria automática, lectura de facturas y control de flujo de caja. Cerramos brechas de productividad administrativa."
                        link="#"
                    />
                    <SolutionCard
                        icon={Briefcase}
                        title="Gestión Empresarial Moderna"
                        desc="Plataformas de gestión que centralizan la operación. Desde la logística hasta la relación con clientes, todo en un solo lugar."
                        link="#"
                    />
                    <SolutionCard
                        icon={Lightbulb}
                        title="Consultoría Estratégica"
                        desc="Acompañamiento experto para decidir mejor. Diagnóstico, estrategia e implementación de IA para transformar tu organización."
                        link="#"
                    />
                </div>
            </div>
        </section>
    )
}

export default Solutions

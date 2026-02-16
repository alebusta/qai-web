
import { FileText, Briefcase, Lightbulb } from 'lucide-react'

const SolutionCard = ({ icon: Icon, title, desc, link }) => {
    return (
        <div className="group bg-white rounded-2xl p-8 hover:shadow-xl transition-all duration-300 border border-gray-100/50 hover:border-gray-200">
            <div className="w-12 h-12 bg-gray-50 rounded-xl flex items-center justify-center mb-6 text-qai-dark group-hover:bg-qai-dark group-hover:text-white transition-colors">
                <Icon className="w-5 h-5 stroke-[1.5]" />
            </div>
            <h3 className="text-2xl font-serif font-bold text-qai-dark mb-3 tracking-tight">{title}</h3>
            <p className="text-gray-600 mb-8 leading-relaxed font-light text-sm">
                {desc}
            </p>

            <div className="inline-flex items-center justify-center px-4 py-1.5 border border-gray-200 rounded-full text-[10px] font-mono font-medium uppercase tracking-widest text-gray-500 bg-transparent">
                Próximamente
            </div>
        </div>
    )
}

const Solutions = () => {
    return (
        <section id="solutions" className="py-24 bg-gray-50/50 relative">
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div className="text-left mb-16">
                    <span className="text-xs font-mono text-gray-400 uppercase tracking-widest mb-4 block">Impacto Real</span>
                    <h2 className="text-3xl md:text-5xl font-serif font-bold text-qai-dark mb-4 leading-tight">
                        Automatizar lo rutinario para <br className="hidden md:block" /> potenciar lo humano.
                    </h2>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
                    <SolutionCard
                        icon={FileText}
                        title="Gestión Financiera"
                        desc="Conciliación bancaria automática, lectura de facturas y control de flujo de caja. Cerramos brechas de productividad administrativa."
                        link="#"
                    />
                    <SolutionCard
                        icon={Briefcase}
                        title="Gestión Empresarial"
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

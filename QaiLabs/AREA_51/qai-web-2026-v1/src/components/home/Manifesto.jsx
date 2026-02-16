
const Manifesto = () => {
    return (
        <section id="manifesto" className="py-24 bg-qai-dark text-white relative overflow-hidden">
            {/* Abstract shapes */}
            <div className="absolute top-0 right-0 -mr-20 -mt-20 w-96 h-96 bg-gray-800 rounded-full blur-3xl opacity-20" />
            <div className="absolute bottom-0 left-0 -ml-20 -mb-20 w-80 h-80 bg-gray-800 rounded-full blur-3xl opacity-20" />

            <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10 text-center">
                <span className="text-sm font-mono text-gray-400 uppercase tracking-widest mb-6 block">Nuestra Filosofía</span>

                <h2 className="text-3xl md:text-5xl font-display font-bold mb-12 leading-tight">
                    No somos una startup buscando el próximo unicornio. Somos una <span className="text-gray-400">bisagra</span>.
                </h2>

                <div className="space-y-8 text-lg md:text-xl text-gray-300 font-light leading-relaxed text-left max-w-2xl mx-auto">
                    <p>
                        Vemos una desconexión crítica. Por un lado, expertos de dominio que conocen los problemas reales. Por otro, tecnólogos creando soluciones para problemas que no existen.
                    </p>
                    <p>
                        <strong className="text-white font-medium">QAI une estos mundos.</strong>
                    </p>
                    <p>
                        Nuestro rol es unir la profundidad del conocimiento experto con la potencia de la IA, creando soluciones que realmente "solucionen la vida" a la gente.
                    </p>

                    <div className="grid grid-cols-1 sm:grid-cols-3 gap-6 py-8 border-t border-gray-800 mt-12">
                        <div className="text-center sm:text-left">
                            <h4 className="text-white font-bold mb-1">Bootstrapped</h4>
                            <p className="text-sm text-gray-500">Sin capital externo. Rendimos cuentas a la calidad, no a inversores.</p>
                        </div>
                        <div className="text-center sm:text-left">
                            <h4 className="text-white font-bold mb-1">AI-First</h4>
                            <p className="text-sm text-gray-500">Pocos humanos, muchos agentes. Escalabilidad real.</p>
                        </div>
                        <div className="text-center sm:text-left">
                            <h4 className="text-white font-bold mb-1">Democratización</h4>
                            <p className="text-sm text-gray-500">Tecnología de élite al alcance de todos.</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    )
}

export default Manifesto

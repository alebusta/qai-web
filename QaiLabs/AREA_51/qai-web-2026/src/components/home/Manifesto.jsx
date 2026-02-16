
const Manifesto = () => {
    return (
        <section id="manifesto" className="py-32 bg-qai-dark text-white relative overflow-hidden">
            {/* Abstract shape */}
            <div className="absolute top-0 right-0 -mr-40 -mt-40 w-[600px] h-[600px] bg-gray-900 rounded-full blur-[100px] opacity-40 pointer-events-none" />

            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
                <span className="text-sm font-mono text-gray-400 uppercase tracking-widest mb-8 block ml-1">Nuestra Filosofía</span>

                <h2 className="text-4xl md:text-6xl font-serif font-bold mb-16 leading-[1.1] max-w-4xl tracking-tight">
                    No somos una startup buscando el próximo unicornio. Somos una <span className="font-serif italic text-white/90">bisagra</span>.
                </h2>

                <div className="w-full h-px bg-white/20 mb-16"></div>

                <div className="grid grid-cols-1 md:grid-cols-2 gap-16">
                    <div className="space-y-8 text-xl text-gray-300 font-light leading-relaxed max-w-[60ch]">
                        <p>
                            Vemos una desconexión crítica. Por un lado, expertos de dominio que conocen los problemas reales. Por otro, tecnólogos creando soluciones para problemas que no existen.
                        </p>
                        <p>
                            <strong className="text-white font-medium">QAI une estos mundos.</strong>
                        </p>
                        <p>
                            Nuestro rol es unir la profundidad del conocimiento experto con la potencia de la IA, creando soluciones que realmente "solucionen la vida" a la gente.
                        </p>
                    </div>

                    <div className="grid grid-cols-1 sm:grid-cols-2 gap-x-8 gap-y-12 h-fit">
                        <div>
                            <h4 className="text-white font-bold mb-2 font-serif text-lg">Bootstrapped</h4>
                            <p className="text-sm text-gray-500 leading-relaxed">Sin capital externo. Rendimos cuentas a la calidad, no a inversores.</p>
                        </div>
                        <div>
                            <h4 className="text-white font-bold mb-2 font-serif text-lg">AI-First</h4>
                            <p className="text-sm text-gray-500 leading-relaxed">Pocos humanos, muchos agentes. Escalabilidad real.</p>
                        </div>
                        <div>
                            <h4 className="text-white font-bold mb-2 font-serif text-lg">Democratización</h4>
                            <p className="text-sm text-gray-500 leading-relaxed">Tecnología de élite al alcance de todos.</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    )
}

export default Manifesto

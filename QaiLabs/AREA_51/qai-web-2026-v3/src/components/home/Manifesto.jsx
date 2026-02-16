
const Manifesto = () => {
    return (
        <section id="manifesto" className="py-16 md:py-24 bg-qai-dark text-white relative overflow-hidden">
            {/* Abstract shape */}
            <div className="absolute top-0 right-0 -mr-40 -mt-40 w-[600px] h-[600px] bg-gray-900 rounded-full blur-[100px] opacity-40 pointer-events-none" />
            <div className="absolute bottom-0 left-0 -ml-20 -mb-20 w-80 h-80 bg-gray-800 rounded-full blur-3xl opacity-20 pointer-events-none" />

            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">

                <span className="text-sm font-mono text-gray-400 uppercase tracking-widest mb-6 block">Nuestra Filosofía</span>

                <h2 className="text-4xl md:text-6xl font-serif font-bold mb-4 leading-[1.1] max-w-4xl tracking-tight">
                    No somos una startup buscando ser el próximo unicornio.
                </h2>
                <h2 className="text-4xl md:text-6xl font-serif font-bold mb-16 leading-[1.1] max-w-4xl tracking-tight italic text-gray-400">
                    Somos una Bisagra.
                </h2>

                <div className="w-full h-px bg-white/10 mb-10"></div>

                <div className="grid grid-cols-1 md:grid-cols-2 gap-16 md:gap-24">
                    <div className="space-y-8 text-xl text-gray-300 font-light leading-relaxed">
                        <p className="font-bold text-white mb-4 block">Problemas críticos en la actualidad respecto aplicaciones de la IA:</p>

                        <div className="mb-8">
                            <h3 className="text-white font-bold text-lg mb-2">Vende Humo Tecnológico</h3>
                            <p className="text-sm md:text-base">Empresas que prometen 'IA revolucionaria' sin entender las limitaciones reales de la tecnología. Generan expectativas imposibles y desperdician recursos de clientes que necesitan soluciones, no fantasías.</p>
                        </div>

                        <div>
                            <h3 className="text-white font-bold text-lg mb-2">Desconexión entre Problema y Solución</h3>
                            <p className="text-sm md:text-base">Por un lado, expertos de dominio (gerentes, administradores, operadores, abogados, médicos, emprendedores) que conocen los problemas reales de su ámbito pero desconfían —con razón— del hype tecnológico, o desconocen como aprovechar sus potenciales.</p>
                            <p className="text-sm md:text-base mt-4">Por otro, tecnólogos brillantes creando soluciones para problemas que no existen o que nadie puede pagar.</p>
                        </div>
                    </div>

                    <div className="grid grid-cols-1 gap-12 h-fit">
                        <div className="relative pl-8 border-l border-white/20">
                            <h4 className="text-white font-bold mb-2 font-serif text-lg">Lo que no hacemos</h4>
                            <ul className="space-y-2 text-sm text-gray-400">
                                <li className="flex items-center"><span className="text-gray-300 mr-2">✗</span> No prometemos "revolucionar tu industria"</li>
                                <li className="flex items-center"><span className="text-gray-300 mr-2">✗</span> No vendemos "IA que lo hace todo sola"</li>
                                <li className="flex items-center"><span className="text-gray-300 mr-2">✗</span> No ocultamos las limitaciones de la tecnología</li>
                                <li className="flex items-center"><span className="text-gray-300 mr-2">✗</span> No inflamos presupuestos con complejidad innecesaria</li>
                                <li className="flex items-center"><span className="text-gray-300 mr-2">✗</span> No vendemos antes de entender tu problema real</li>
                                <li className="flex items-center"><span className="text-gray-300 mr-2">✗</span> No vendemos 'transformación digital' ni 'disrupción'.</li>
                            </ul>
                        </div>
                        <div className="relative pl-8 border-l border-white/20">
                            <h4 className="text-white font-bold mb-2 font-serif text-lg">Lo que Sí Hacemos</h4>
                            <ul className="space-y-2 text-sm text-gray-300">
                                <li className="flex items-center"><span className="text-gray-100 mr-2">✓</span> Resolver problemas concretos con tecnología apropiada.</li>
                                <li className="flex items-center"><span className="text-gray-100 mr-2">✓</span> Supervisión humana</li>
                                <li className="flex items-center"><span className="text-gray-100 mr-2">✓</span> Transparencia técnica sobre qué funciona y qué no.</li>
                                <li className="flex items-center"><span className="text-gray-100 mr-2">✓</span> Vendemos fricción reducida y valor económico medible.</li>
                            </ul>
                        </div>

                    </div>
                </div>

                {/* Highlighted Connector Section */}
                <div className="mt-6 md:mt-10 text-center max-w-5xl mx-auto py-16 px-8 bg-white/5 rounded-[2.5rem] border border-white/10 relative overflow-hidden group">
                    <div className="absolute top-0 right-0 w-64 h-64 bg-gray-500 rounded-full blur-[120px] opacity-10 -mr-32 -mt-32 group-hover:opacity-20 transition-opacity" />

                    <div className="relative z-10">
                        <p className="text-3xl md:text-4xl font-serif text-white font-bold mb-8 tracking-tight">
                            QAI es el conector entre estos mundos.
                        </p>
                        <p className="text-lg md:text-xl text-gray-300 font-light leading-relaxed max-w-4xl mx-auto">
                            Unimos esa expertise profunda de tu ámbito de dominio con la tecnología que te permite ampliar capacidades, de manera responsable y honesta respecto a lo que funciona y lo que no.
                        </p>
                    </div>
                </div>

                <div className="mt-0 pt-8 border-t border-white/10 text-center max-w-4xl mx-auto">
                    <p className="text-2xl font-serif italic text-white mb-8 leading-relaxed">
                        "La tecnología es el medio. Tu problema resuelto es el fin."
                    </p>
                    <p className="text-sm text-gray-400 font-mono">
                        Si buscas un pitch de "nuestra IA mágica va a cambiar el mundo", no somos tu laboratorio. Si buscas soluciones que funcionen hoy, con honestidad técnica y resultados medibles, hablemos.
                    </p>
                </div>

            </div>
        </section>
    )
}

export default Manifesto

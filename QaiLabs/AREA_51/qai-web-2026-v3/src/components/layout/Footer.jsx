
const Footer = () => {
    return (
        <footer id="contact" className="bg-white border-t border-gray-100 relative overflow-hidden">
            {/* CTA Section */}
            <div className="py-24 bg-gray-50 border-b border-gray-100 text-center">
                <div className="max-w-4xl mx-auto px-4">
                    <h2 className="text-3xl md:text-5xl font-serif font-bold text-qai-dark mb-6 leading-tight">
                        ¿Tu Organización Tiene Fricción Operativa?
                    </h2>
                    <p className="text-lg md:text-xl text-gray-600 font-light mb-12 max-w-2xl mx-auto font-sans">
                        Ineficiencias que destruyen valor. Procesos manuales que consumen tiempo crítico. Datos que nadie puede usar para decidir.
                    </p>

                    <p className="text-lg font-medium text-gray-800 mb-8">
                        Agenda 30 minutos. Analizamos tu caso y te decimos —con honestidad— si podemos reducir esa fricción.
                    </p>

                    <a
                        href="mailto:hola@theqai.co"
                        className="btn-qai-primary inline-flex items-center px-8 py-4 rounded-full font-medium text-lg mb-8"
                    >
                        Agendar Diagnóstico
                    </a>

                    <p className="text-sm text-gray-500 font-mono tracking-wide font-bold mb-4">
                        Sin costo. Sin compromiso. Solo rigor científico.
                    </p>

                    <p className="text-sm text-gray-400 italic">
                        O escribe a hola@theqai.co con una descripción de tu desafío.
                    </p>
                </div>
            </div>

            {/* Links Section */}
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
                <div className="flex flex-col md:flex-row justify-between items-center">

                    <div className="mb-8 md:mb-0 flex items-center gap-4">
                        {/* Logo Image */}
                        <img src="/logo.png" alt="QAI Logo" className="h-8 w-auto opacity-90 filter grayscale brightness-0" />

                        <span className="w-px h-6 bg-gray-300"></span>

                        <span className="text-xs font-mono text-gray-500 uppercase tracking-widest">
                            Laboratorio de Soluciones
                        </span>
                    </div>

                    <div className="mb-4 md:mb-0 md:absolute md:left-8 md:bottom-4 pl-4 sm:pl-0">
                        <span className="text-xs text-gray-400 font-light">
                            © {new Date().getFullYear()} The QAI Company.
                        </span>
                    </div>

                    <div className="flex space-x-8 items-center">
                        {['LinkedIn', 'GitHub', 'Email'].map((item) => (
                            <a
                                key={item}
                                href="#"
                                className="text-sm font-medium text-gray-500 hover:text-black transition-colors relative group"
                            >
                                {item}
                                <span className="absolute left-0 bottom-0 w-0 h-px bg-black transition-all duration-300 group-hover:w-full" />
                            </a>
                        ))}
                    </div>
                </div>
            </div>
        </footer>
    )
}

export default Footer

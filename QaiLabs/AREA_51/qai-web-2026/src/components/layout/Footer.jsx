
const Footer = () => {
    return (
        <footer className="bg-white border-t border-gray-100 py-16">
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div className="flex flex-col md:flex-row justify-between items-start md:items-center">

                    <div className="mb-8 md:mb-0 space-y-4">
                        <img
                            src="/logo.png"
                            alt="The QAI Company"
                            className="h-6 w-auto grayscale opacity-100 transition-all"
                        />
                        <p className="text-xs text-gray-400 font-mono tracking-wide">
                            © {new Date().getFullYear()} The QAI Company. Santiago, Chile.
                        </p>
                    </div>

                    <div className="flex space-x-8">
                        {['LinkedIn', 'GitHub', 'Contact'].map((item) => (
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

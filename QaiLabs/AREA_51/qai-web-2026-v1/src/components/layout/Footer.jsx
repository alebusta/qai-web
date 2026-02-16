
const Footer = () => {
    return (
        <footer className="bg-white border-t border-gray-100 py-12">
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div className="flex flex-col md:flex-row justify-between items-center">
                    <div className="mb-4 md:mb-0">
                        <div className="flex items-center gap-2 mb-2">
                            <img src="/logo.png" alt="The QAI Company" className="h-8 w-auto grayscale opacity-80 hover:grayscale-0 hover:opacity-100 transition-all" />
                        </div>
                        <p className="text-sm text-gray-500 mt-1">
                            © {new Date().getFullYear()} The QAI Company. All rights reserved.
                        </p>
                    </div>
                    <div className="flex space-x-6">
                        <a href="#" className="text-gray-400 hover:text-gray-900 transition-colors">
                            LinkedIn
                        </a>
                        <a href="#" className="text-gray-400 hover:text-gray-900 transition-colors">
                            GitHub
                        </a>
                        <a href="#" className="text-gray-400 hover:text-gray-900 transition-colors">
                            Contact
                        </a>
                    </div>
                </div>
            </div>
        </footer>
    )
}

export default Footer

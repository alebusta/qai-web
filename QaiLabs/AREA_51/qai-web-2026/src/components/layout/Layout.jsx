
import Navbar from './Navbar'
import Footer from './Footer'

const Layout = ({ children }) => {
    return (
        <div className="flex flex-col min-h-screen bg-qai-light font-sans text-qai-text antialiased selection:bg-black selection:text-white">
            <div className="bg-noise fixed inset-0 z-50 pointer-events-none opacity-[0.03] mix-blend-multiply"></div>
            <Navbar />
            <main className="flex-grow pt-16 md:pt-20">
                {children}
            </main>
            <Footer />
        </div>
    )
}

export default Layout

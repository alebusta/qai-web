
import Navbar from './Navbar'
import Footer from './Footer'

const Layout = ({ children }) => {
    return (
        <div className="flex flex-col min-h-screen bg-qai-light">
            <Navbar />
            <main className="flex-grow pt-16 md:pt-20">
                {children}
            </main>
            <Footer />
        </div>
    )
}

export default Layout

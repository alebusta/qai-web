
import Hero from '../components/home/Hero'
import About from '../components/home/About'
import AIPosture from '../components/home/AIPosture'
import HowWeWork from '../components/home/HowWeWork'
import Cases from '../components/home/Cases'
import Manifesto from '../components/home/Manifesto'

const Home = () => {
    return (
        <div className="bg-qai-light min-h-screen">
            <Hero />
            <About />
            <AIPosture />
            <HowWeWork />
            <Cases />
            <Manifesto />
        </div>
    )
}

export default Home

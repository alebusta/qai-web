import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Layout from './components/layout/Layout'
import Home from './pages/Home'
import ProposalPage from './pages/ProposalPage'

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/propuestas/:slug" element={<ProposalPage />} />
        <Route
          path="/"
          element={
            <Layout>
              <Home />
            </Layout>
          }
        />
      </Routes>
    </BrowserRouter>
  )
}

export default App

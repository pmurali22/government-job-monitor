import { Route, Routes, Link } from 'react-router-dom'
import Home from './pages/Home'
import Login from './pages/Login'
import Dashboard from './pages/Dashboard'

function App() {
  return (
    <div className="app-shell">
      <header className="app-header">
        <Link to="/">Job Monitor</Link>
        <nav>
          <Link to="/dashboard">Dashboard</Link>
          <Link to="/login">Login</Link>
        </nav>
      </header>
      <main>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/login" element={<Login />} />
          <Route path="/dashboard" element={<Dashboard />} />
        </Routes>
      </main>
    </div>
  )
}

export default App

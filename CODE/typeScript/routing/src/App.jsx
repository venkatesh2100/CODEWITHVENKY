import { useState } from 'react';
import './App.css';
import { BrowserRouter as Router, Route, Link, Routes} from 'react-router-dom';
import Home from './components/Home';
import About from './components/About';
import Footer from './components/Footer';

function App() {
  const [count, setCount] = useState(0);

  return (
    <Router>
      <div>
        <nav>
          <ul>
            <li>
              <Link to="/">Home</Link>
            </li>
            <li>
              <Link to="/About">About</Link>
            </li>
            <li>
              <Link to="/Footer">Footer</Link>
            </li>
          </ul>
        </nav>

        <Routes>
          <Route path="/" exact element={Home} />
          <Route path="/about" element={About} />
          <Route path="/footer" element={Footer} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;

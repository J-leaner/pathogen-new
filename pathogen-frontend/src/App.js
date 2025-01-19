import React from 'react';
import { Routes, Route, Link } from 'react-router-dom';
import Home from './pages/Home';
import Search from './pages/Search';
import Details from './pages/Details';

function App() {
  return (
    <div className="min-h-screen bg-gray-100">
      <header className="bg-blue-600 text-white p-4">
        <nav className="container mx-auto flex justify-between">
          <Link to="/" className="text-lg font-bold">Pathogen Database</Link>
          <div>
            <Link to="/search" className="mr-4 hover:underline">Search</Link>
          </div>
        </nav>
      </header>
      <main className="container mx-auto p-4">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/search" element={<Search />} />
          <Route path="/details/:id" element={<Details />} />
        </Routes>
      </main>
    </div>
  );
}

export default App;

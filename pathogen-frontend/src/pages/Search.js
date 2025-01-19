import React, { useState } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';

function Search() {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleSearch = async () => {
    setLoading(true);
    try {
      const response = await axios.get(`http://localhost:8000/api/genes/?search=${query}`);
      setResults(response.data);
    } catch (error) {
      console.error('Error fetching data:', error);
    }
    setLoading(false);
  };

  return (
    <div className="bg-white p-6 rounded shadow">
      <h2 className="text-xl font-bold mb-4">Search Genes</h2>
      <div className="flex items-center space-x-2">
        <input
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Enter pathogen or gene name"
          className="flex-1 p-2 border border-gray-300 rounded"
        />
        <button onClick={handleSearch} className="bg-blue-600 text-white px-4 py-2 rounded">
          Search
        </button>
      </div>

      {loading && <p className="mt-4 text-gray-600">Loading...</p>}

      <div className="mt-6">
        {results.length > 0 ? (
          <ul className="space-y-4">
            {results.map((result) => (
              <li key={result.id} className="p-4 bg-gray-50 rounded shadow">
                <h3 className="font-bold text-blue-600">{result.name}</h3>
                <p>{result.function_annotation}</p>
                <Link to={`/details/${result.id}`} className="text-blue-500 hover:underline">
                  View Details
                </Link>
              </li>
            ))}
          </ul>
        ) : (
          !loading && <p className="text-gray-600">No results found.</p>
        )}
      </div>
    </div>
  );
}

export default Search;


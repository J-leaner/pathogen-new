import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';

function Details() {
  const { id } = useParams();
  const [gene, setGene] = useState(null);

  useEffect(() => {
    const fetchGeneDetails = async () => {
      try {
        const response = await axios.get(`http://localhost:8000/api/genes/${id}/`);
        setGene(response.data);
      } catch (error) {
        console.error('Error fetching gene details:', error);
      }
    };

    fetchGeneDetails();
  }, [id]);

  if (!gene) {
    return <p>Loading...</p>;
  }

  return (
    <div className="bg-white p-6 rounded shadow">
      <h2 className="text-xl font-bold text-blue-600">{gene.name}</h2>
      <p className="mt-2"><strong>Function Annotation:</strong> {gene.function_annotation}</p>
      <p className="mt-2"><strong>Sequence:</strong> {gene.sequence}</p>
    </div>
  );
}

export default Details;



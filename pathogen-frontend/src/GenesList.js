import React, { useState, useEffect } from 'react';
import { getGenes } from './api'; // 假设你已经定义了 getGenes API

function GenesList() {
  const [genes, setGenes] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const data = await getGenes();  // 假设 getGenes 会返回基因数据
      setGenes(data);
    };

    fetchData();
  }, []);

  if (!genes || genes.length === 0) {
    return <div>Loading...</div>; // 或者你可以显示一个空状态
  }

  return (
    <div>
      <h1>Genes List</h1>
      <ul>
        {genes.map(gene => (
          <li key={gene.gene_id}>{gene.name}</li>
        ))}
      </ul>
    </div>
  );
}

export default GenesList;


import axios from 'axios';

const API_URL = 'http://localhost:8000/api/';

export const getSpecies = async () => {
  try {
    const response = await axios.get(`${API_URL}species/`);
    return response.data;
  } catch (error) {
    console.error("Error fetching species:", error);
  }
};

export const getGenes = async () => {
  try {
    const response = await axios.get(`${API_URL}genes/`);
    return response.data;
  } catch (error) {
    console.error("Error fetching genes:", error);
  }
};



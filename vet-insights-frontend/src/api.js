import axios from 'axios';

const API_BASE_URL = 'http://127.0.0.1:5000';  // Your backend

export const fetchData = async (cid) => {
    try {
        const response = await axios.post(`${API_BASE_URL}/fetch`, { cid });
        return response.data;
    } catch (error) {
        console.error('Error fetching data:', error);
        throw error;
    }
};

export const uploadReport = async (reportData) => {
    try {
        const response = await axios.post(`${API_BASE_URL}/upload`, reportData);
        return response.data;
    } catch (error) {
        console.error('Error uploading report:', error);
        throw error;
    }
};

import React, { useState } from 'react';
import { fetchData } from '../api';

const FetchData = ({ setAnalysisData }) => {
    const [cid, setCid] = useState('');
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState('');

    const handleFetch = async () => {
        setLoading(true);
        setError('');
        try {
            const data = await fetchData(cid);
            setAnalysisData(data);
        } catch (err) {
            setError('Failed to fetch data. Check CID.');
        }
        setLoading(false);
    };

    return (
        <div>
            <input 
                type="text" 
                value={cid} 
                onChange={(e) => setCid(e.target.value)} 
                placeholder="Enter Filecoin CID" 
            />
            <button onClick={handleFetch} disabled={loading}>
                {loading ? 'Fetching...' : 'Fetch Data'}
            </button>
            {error && <p style={{ color: 'red' }}>{error}</p>}
        </div>
    );
};

export default FetchData;

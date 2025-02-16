import React from 'react';

const DisplayData = ({ analysisData }) => {
    if (!analysisData) return <p>No data available.</p>;

    return (
        <div>
            <h2>Analysis Results</h2>
            <pre>{JSON.stringify(analysisData, null, 2)}</pre>
        </div>
    );
};

export default DisplayData;

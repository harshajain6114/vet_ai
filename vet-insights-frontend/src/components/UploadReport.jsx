import React, { useState } from 'react';
import { uploadReport } from '../api';

const UploadReport = ({ analysisData }) => {
    const [cid, setCid] = useState('');
    const [loading, setLoading] = useState(false);

    const handleUpload = async () => {
        setLoading(true);
        try {
            const response = await uploadReport({ report: analysisData });
            setCid(response.cid);
        } catch (err) {
            console.error('Upload failed');
        }
        setLoading(false);
    };

    return (
        <div>
            <button onClick={handleUpload} disabled={loading}>
                {loading ? 'Uploading...' : 'Upload Report'}
            </button>
            {cid && <p>Report stored at CID: {cid}</p>}
        </div>
    );
};

export default UploadReport;

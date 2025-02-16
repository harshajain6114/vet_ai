import React, { useState } from "react";
import axios from "axios";

function App() {
  const [cid, setCid] = useState(""); // User input for CID
  const [data, setData] = useState(null); // Fetched JSON data
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const fetchData = async () => {
    setLoading(true);
    setError("");
    try {
      const response = await axios.post("http://127.0.0.1:5000/fetch", {
        cid: cid, // Send CID to backend
      });

      setData(response.data); // Store response data
    } catch (err) {
      setError("Failed to fetch data. Check CID or backend.");
    }
    setLoading(false);
  };

  return (
    <div style={{ padding: "20px" }}>
      <h2>📂 Fetch JSON from Lighthouse</h2>
      
      <input
        type="text"
        value={cid}
        onChange={(e) => setCid(e.target.value)}
        placeholder="Enter Filecoin CID"
        style={{ padding: "10px", width: "300px", marginRight: "10px" }}
      />
      <button onClick={fetchData} disabled={!cid}>
        Fetch Data
      </button>

      {loading && <p>Loading...</p>}
      {error && <p style={{ color: "red" }}>{error}</p>}

      {data && (
        <pre style={{ background: "#f4f4f4", padding: "10px", marginTop: "10px" }}>
          {JSON.stringify(data, null, 2)}
        </pre>
      )}
    </div>
  );
}

export default App;


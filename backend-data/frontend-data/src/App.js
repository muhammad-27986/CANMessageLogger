import { useState, useEffect } from "react";

function App() {
  const [data, setData] = useState({
    speed: 0,
    rpm: 0,
    fuel: 0,
    temperature: 0,
  });

  useEffect(() => {
    const interval = setInterval(() => {
      fetch("http://127.0.0.1:5000/data")
        .then((res) => res.json())
        .then((d) => setData(d))
        .catch((err) => console.error("Fetch error:", err));
    }, 1000);

    return () => clearInterval(interval);
  }, []);

  return (
    <div style={{ padding: 20 }}>
      <h1>Dashcam Data</h1>
      <p>Speed: {data.speed} km/h</p>
      <p>RPM: {data.rpm}</p>
      <p>Fuel: {data.fuel} %</p>
      <p>Temperature: {data.temperature} °C</p>
    </div>
  );
}

export default App;

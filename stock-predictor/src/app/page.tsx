"use client";

import { useState, useEffect } from "react";
import axios from "axios";

export default function Home() {
  const [stocks, setStocks] = useState<string[]>([]);

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/data")
      .then((response) => {
        setStocks(response.data.stocks);
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
      });
  }, []);

  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold">Stock List</h1>
      <ul>
        {stocks.map((stock, index) => (
          <li key={index}>{stock}</li>
        ))}
      </ul>
    </div>
  );
}

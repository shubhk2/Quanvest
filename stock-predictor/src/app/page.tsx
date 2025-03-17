"use client";
import { useState, useEffect } from "react";
import axios from "axios";

export default function Home() {
  const [fundamentals, setFundamentals] = useState<any>(null);
  const symbol = 'AAPL'; // Example stock

  useEffect(() => {
    axios.get(`/income/route.ts`)
      .then((response) => {
        console.log("API Response:", response.data);
        setFundamentals(response.data);
      })
      .catch((error) => {
        console.error("Error fetching stock fundamentals:", error);
      });
  }, []);

  return (
    <div>
      <h1>Stock Fundamentals</h1>
      {fundamentals ? (
        <div>
          <p><strong>Company:</strong> {fundamentals.Name}</p>
          <p><strong>Market Cap:</strong> {fundamentals.MarketCapitalization}</p>
          <p><strong>P/E Ratio:</strong> {fundamentals.PERatio}</p>
          <p><strong>Dividend Yield:</strong> {fundamentals.DividendYield}</p>
          <p><strong>Profit Margin:</strong> {fundamentals.ProfitMargin}</p>
        </div>
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
}

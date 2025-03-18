import { NextResponse } from "next/server";
import axios from "axios";

export async function GET() {
  try {
    console.log("Fetching Balance Sheet...");
    const res = await axios.get("http://127.0.0.1:8000/stock_prices/monthly/AAPL");
    return NextResponse.json(res.data);
  } catch (error: any) {
    console.error("Error in Next.js API Route:", error.message);
    return NextResponse.json({ error: error.message }, { status: 500 });
  }
}
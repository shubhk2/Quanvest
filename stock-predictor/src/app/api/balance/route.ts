import { NextResponse } from "next/server";
import axios from "axios";

export async function GET() {
  try {
    console.log("Fetching Balance Sheet...");
    const res = await axios.get("http://127.0.0.1:8000/balance/AAPL");
    // console.log("API Response:", res.data);
    return NextResponse.json(res.data);
  } catch (error: any) {
    console.error("Error in Next.js API Route:", error.message);
    return NextResponse.json({ error: error.message }, { status: 500 });
  }
}
// Compare this snippet from stocks-predictor/src/app/api/income/route.ts:
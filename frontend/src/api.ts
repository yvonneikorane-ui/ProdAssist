export interface ProductionRecord {
  production_id: string;
  timestamp: string;
  machine_id: string;
  product_type: string;
  order_id: string;
  shift: string;
  target_output: number;
  actual_output: number;
  downtime_minutes: number;
  defect_count: number;
  total_units: number;
  machine_temperature_c: number;
  machine_status: string;
}


export interface AnalysisResult {
  production_id: string;
  output_deviation_pct: number;
  defect_rate_pct: number;
  severity: string;
  deviation_detected: boolean;
  contributing_factors: string[];
  explanation: string;
  recommendation: string;
}


const API_BASE =
  import.meta.env.VITE_API_BASE ??
  "http://localhost:8000";


async function request<T>(
  path: string,
  options?: RequestInit,
): Promise<T> {

  const response = await fetch(
    `${API_BASE}${path}`,
    {
      headers: {
        "Content-Type": "application/json",
      },
      ...options,
    },
  );

  if (!response.ok) {
    const message =
      await response.text();

    throw new Error(
      message ||
        `Request failed: ${response.status}`,
    );
  }

  return response.json() as Promise<T>;
}


export function getProduction():
  Promise<ProductionRecord[]> {

  return request<ProductionRecord[]>(
    "/api/production",
  );
}


export function getAnalysis(
  productionId: string,
): Promise<AnalysisResult> {

  return request<AnalysisResult>(
    `/api/production/${productionId}/analysis`,
  );
}


export function submitDecision(
  productionId: string,
  decision:
    | "investigate"
    | "accept"
    | "dismiss"
    | "escalate",
): Promise<void> {

  return request(
    "/api/decisions",
    {
      method: "POST",
      body: JSON.stringify({
        production_id: productionId,
        decision,
      }),
    },
  ).then(() => undefined);
}

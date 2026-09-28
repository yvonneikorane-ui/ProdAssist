import {
  useEffect,
  useMemo,
  useState,
} from "react";

import {
  getAnalysis,
  getProduction,
  submitDecision,
  type AnalysisResult,
  type ProductionRecord,
} from "./api";


function App() {
  const [
    records,
    setRecords,
  ] = useState<ProductionRecord[]>([]);

  const [
    selectedId,
    setSelectedId,
  ] = useState<string>("");

  const [
    analysis,
    setAnalysis,
  ] = useState<AnalysisResult | null>(
    null,
  );

  const [
    loading,
    setLoading,
  ] = useState(true);

  const [
    error,
    setError,
  ] = useState("");

  const [
    decisionMessage,
    setDecisionMessage,
  ] = useState("");


  useEffect(() => {
    getProduction()
      .then((data) => {
        setRecords(data);

        if (data.length > 0) {
          setSelectedId(
            data[0].production_id,
          );
        }
      })
      .catch((err: Error) =>
        setError(err.message),
      )
      .finally(() =>
        setLoading(false),
      );
  }, []);


  useEffect(() => {
    if (!selectedId) {
      return;
    }

    setAnalysis(null);

    getAnalysis(selectedId)
      .then(setAnalysis)
      .catch((err: Error) =>
        setError(err.message),
      );
  }, [selectedId]);


  const selected = useMemo(
    () =>
      records.find(
        (record) =>
          record.production_id ===
          selectedId,
      ),
    [records, selectedId],
  );


  const handleDecision = async (
    decision:
      | "investigate"
      | "accept"
      | "dismiss"
      | "escalate",
  ) => {

    if (!selectedId) {
      return;
    }

    try {
      await submitDecision(
        selectedId,
        decision,
      );

      setDecisionMessage(
        `Decision recorded: ${decision}`,
      );
    } catch (err) {
      setError(
        err instanceof Error
          ? err.message
          : "Unable to record decision",
      );
    }
  };


  if (loading) {
    return (
      <main className="page">
        <p>
          Loading production data…
        </p>
      </main>
    );
  }


  return (
    <main className="page">

      <header className="header">

        <div>

          <p className="eyebrow">
            PRODASSIST
          </p>

          <h1>
            Production Management Assistance
          </h1>

          <p className="subtitle">
            Human-in-the-loop production
            deviation analysis demonstrator
          </p>

        </div>

        <div className="status">
          SYSTEM ONLINE
        </div>

      </header>


      {error && (
        <div className="error">
          {error}
        </div>
      )}


      <section className="workspace">

        <aside className="panel runs">

          <div className="panel-heading">

            <h2>
              Production runs
            </h2>

            <span>
              {records.length}
            </span>

          </div>


          <div className="run-list">

            {records.map((record) => (

              <button
                className={`run ${
                  record.production_id ===
                  selectedId
                    ? "selected"
                    : ""
                }`}
                key={record.production_id}
                onClick={() =>
                  setSelectedId(
                    record.production_id,
                  )
                }
              >

                <strong>
                  {record.production_id}
                </strong>

                <span>
                  {record.machine_id}
                  {" · "}
                  {record.product_type}
                </span>

                <span>
                  {record.actual_output}
                  {" / "}
                  {record.target_output}
                  {" units"}
                </span>

              </button>

            ))}

          </div>

        </aside>


        <section className="panel detail">

          {selected && analysis ? (

            <>

              <div className="detail-header">

                <div>

                  <p className="eyebrow">
                    PRODUCTION RUN
                  </p>

                  <h2>
                    {selected.production_id}
                  </h2>

                  <p>
                    {selected.machine_id}
                    {" · "}
                    {selected.product_type}
                    {" · Order "}
                    {selected.order_id}
                  </p>

                </div>


                <span
                  className={`severity ${analysis.severity}`}
                >
                  {analysis.severity.toUpperCase()}
                </span>

              </div>


              <div className="metrics">

                <Metric
                  label="Target output"
                  value={`${selected.target_output} units`}
                />

                <Metric
                  label="Actual output"
                  value={`${selected.actual_output} units`}
                />

                <Metric
                  label="Output deviation"
                  value={`${analysis.output_deviation_pct.toFixed(1)}%`}
                />

                <Metric
                  label="Downtime"
                  value={`${selected.downtime_minutes} min`}
                />

                <Metric
                  label="Defect rate"
                  value={`${analysis.defect_rate_pct.toFixed(1)}%`}
                />

                <Metric
                  label="Temperature"
                  value={`${selected.machine_temperature_c.toFixed(1)} °C`}
                />

              </div>


              <section className="assessment">

                <h3>
                  System assessment
                </h3>

                <p>
                  {analysis.explanation}
                </p>

              </section>


              <section className="two-column">

                <div>

                  <h3>
                    Contributing indicators
                  </h3>

                  {analysis
                    .contributing_factors
                    .length > 0 ? (

                    <ul>

                      {analysis
                        .contributing_factors
                        .map((factor) => (

                          <li key={factor}>
                            {factor}
                          </li>

                        ))}

                    </ul>

                  ) : (

                    <p>
                      No additional indicators.
                    </p>

                  )}

                </div>


                <div>

                  <h3>
                    Suggested action
                  </h3>

                  <p>
                    {analysis.recommendation}
                  </p>

                </div>

              </section>


              <section className="human-decision">

                <div>

                  <h3>
                    Human decision
                  </h3>

                  <p>
                    The system provides support;
                    the production decision remains
                    with the human decision-maker.
                  </p>

                </div>


                <div className="actions">

                  <button
                    onClick={() =>
                      handleDecision(
                        "investigate",
                      )
                    }
                  >
                    Investigate
                  </button>

                  <button
                    onClick={() =>
                      handleDecision("accept")
                    }
                  >
                    Accept
                  </button>

                  <button
                    onClick={() =>
                      handleDecision("dismiss")
                    }
                  >
                    Dismiss
                  </button>

                  <button
                    onClick={() =>
                      handleDecision(
                        "escalate",
                      )
                    }
                  >
                    Escalate
                  </button>

                </div>


                {decisionMessage && (

                  <p className="confirmation">
                    {decisionMessage}
                  </p>

                )}

              </section>

            </>

          ) : (

            <p>
              Select a production run.
            </p>

          )}

        </section>

      </section>

    </main>
  );
}


function Metric({
  label,
  value,
}: {
  label: string;
  value: string;
}) {

  return (
    <div className="metric">

      <span>
        {label}
      </span>

      <strong>
        {value}
      </strong>

    </div>
  );
}


export default App;

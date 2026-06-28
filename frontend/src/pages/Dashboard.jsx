import { useEffect, useState } from "react";

import Navbar from "../components/Navbar";
import Sidebar from "../components/Sidebar";

import TrustScoreCard from "../components/TrustScoreCard";
import DeviceCard from "../components/DeviceCard";
import DecisionCard from "../components/DecisionCard";
import RiskCard from "../components/RiskCard";
import RecentLogins from "../components/RecentLogins";

import { getDashboardSummary } from "../services/dashboard";

function Dashboard() {
  const [summary, setSummary] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadDashboard();
  }, []);

  const loadDashboard = async () => {
    try {
      const data = await getDashboardSummary();
      setSummary(data);
    } catch (error) {
      console.error("Dashboard Error:", error);
    } finally {
      setLoading(false);
    }
  };

  if (loading || !summary) {
  return (
    <div className="min-h-screen bg-slate-950 flex items-center justify-center">
      <h1 className="text-white text-3xl">
        Loading Dashboard...
      </h1>
    </div>
  );
}

  return (
    <div className="bg-slate-950 min-h-screen">
      <Navbar />

      <div className="flex">
        <Sidebar />

        <main className="flex-1 p-8">
          <h1 className="text-4xl font-bold text-white mb-8">
            Dashboard
          </h1>

          <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-6">
            <TrustScoreCard score={summary.trust_score} />

            <DeviceCard
              device={summary.device}
              browser={summary.browser}
              status={summary.status}
            />

            <DecisionCard decision={summary.decision} />

            <RiskCard risk={summary.risk} />
            <RecentLogins />
          </div>
        </main>
      </div>
    </div>
  );
}

export default Dashboard;
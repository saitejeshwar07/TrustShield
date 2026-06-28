import { ShieldCheck } from "lucide-react";

function TrustScoreCard({ score }) {
  // Decide the risk level and color based on the score
  let riskLevel = "Low Risk";
  let color = "text-green-400";

  if (score < 80) {
    riskLevel = "Medium Risk";
    color = "text-yellow-400";
  }

  if (score < 50) {
    riskLevel = "High Risk";
    color = "text-red-400";
  }

  return (
    <div className="bg-slate-900 rounded-2xl p-6 border border-slate-700 shadow-lg hover:shadow-blue-500/10 transition-all duration-300">
      <div className="flex justify-between items-center">
        <div>
          <p className="text-slate-400 text-sm">
            Trust Score
          </p>

          <h1 className={`text-5xl font-bold mt-3 ${color}`}>
            {score}
          </h1>

          <p className={`mt-2 font-semibold ${color}`}>
            {riskLevel}
          </p>
        </div>

        <ShieldCheck
          className={color}
          size={52}
        />
      </div>
    </div>
  );
}

export default TrustScoreCard;
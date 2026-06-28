import { TriangleAlert } from "lucide-react";

function RiskCard({ risk }) {
  let color = "text-green-400";
  let bgColor = "bg-green-500/20";
  let level = "Low";

  if (risk >= 30) {
    color = "text-yellow-400";
    bgColor = "bg-yellow-500/20";
    level = "Medium";
  }

  if (risk >= 70) {
    color = "text-red-400";
    bgColor = "bg-red-500/20";
    level = "High";
  }

  return (
    <div className="bg-slate-900 rounded-2xl p-6 border border-slate-700 shadow-lg hover:shadow-blue-500/10 transition-all duration-300">
      <div className="flex justify-between items-center">
        <div>
          <p className="text-slate-400 text-sm">
            Risk Score
          </p>

          <h1 className={`text-5xl font-bold mt-3 ${color}`}>
            {risk}
          </h1>

          <span
            className={`inline-block mt-3 px-3 py-1 rounded-full ${bgColor} ${color} text-sm font-semibold`}
          >
            {level} Risk
          </span>
        </div>

        <TriangleAlert
          className={color}
          size={50}
        />
      </div>
    </div>
  );
}

export default RiskCard;
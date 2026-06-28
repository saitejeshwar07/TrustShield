import {
  CircleCheckBig,
  ShieldAlert,
  ShieldX,
} from "lucide-react";

function DecisionCard({ decision }) {
  let color = "text-green-400";
  let Icon = CircleCheckBig;

  if (decision === "STEP_UP_AUTH") {
    color = "text-yellow-400";
    Icon = ShieldAlert;
  }

  if (decision === "BLOCK") {
    color = "text-red-400";
    Icon = ShieldX;
  }

  return (
    <div className="bg-slate-900 rounded-2xl p-6 border border-slate-700 shadow-lg hover:shadow-blue-500/10 transition-all duration-300">
      <p className="text-slate-400 text-sm">
        Decision
      </p>

      <h1 className={`text-3xl font-bold mt-4 ${color}`}>
        {decision}
      </h1>

      <Icon
        className={`${color} mt-5`}
        size={48}
      />
    </div>
  );
}

export default DecisionCard;
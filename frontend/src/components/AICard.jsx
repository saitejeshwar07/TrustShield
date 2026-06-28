import { Bot } from "lucide-react";

function AICard({ prediction, model }) {
  const isNormal = prediction === "NORMAL";

  return (
    <div className="bg-slate-900 rounded-2xl p-6 border border-slate-700 shadow-lg">
      <div className="flex justify-between items-center">
        <div>
          <p className="text-slate-400 text-sm">
            AI Detection
          </p>

          <h2
            className={`text-3xl font-bold mt-3 ${
              isNormal ? "text-green-400" : "text-red-400"
            }`}
          >
            {prediction}
          </h2>

          <p className="text-slate-400 mt-2">
            {model}
          </p>
        </div>

        <Bot
          size={48}
          className={isNormal ? "text-green-400" : "text-red-400"}
        />
      </div>
    </div>
  );
}

export default AICard;
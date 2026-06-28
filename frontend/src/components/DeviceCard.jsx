import { Laptop } from "lucide-react";

function DeviceCard({ device, browser, status }) {
  return (
    <div className="bg-slate-900 rounded-2xl p-6 border border-slate-700 shadow-lg hover:shadow-blue-500/10 transition-all duration-300">
      <div className="flex justify-between items-center">
        <div>
          <p className="text-slate-400 text-sm">
            Current Device
          </p>

          <h2 className="text-white text-xl font-semibold mt-3">
            {device}
          </h2>

          <p className="text-slate-400 mt-1">
            {browser}
          </p>

          <span className="inline-block mt-3 px-3 py-1 rounded-full bg-green-500/20 text-green-400 text-sm">
            {status}
          </span>
        </div>

        <Laptop
          className="text-blue-400"
          size={50}
        />
      </div>
    </div>
  );
}

export default DeviceCard;
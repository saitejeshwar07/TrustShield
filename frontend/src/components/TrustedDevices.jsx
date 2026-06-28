import { useEffect, useState } from "react";
import { getDevices } from "../services/device";

function TrustedDevices() {
  const [devices, setDevices] = useState([]);

  useEffect(() => {
    loadDevices();
  }, []);

  const loadDevices = async () => {
    try {
      const data = await getDevices();
      setDevices(data);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div className="bg-slate-900 rounded-2xl p-6 border border-slate-700">
      <h2 className="text-white text-xl font-semibold mb-4">
        Trusted Devices
      </h2>

      {devices.length === 0 ? (
        <p className="text-slate-400">
          No trusted devices found.
        </p>
      ) : (
        <div className="space-y-3">
          {devices.map((device) => (
            <div
              key={device.id}
              className="rounded-lg bg-slate-800 p-3 border border-slate-700"
            >
              <p className="text-white font-medium">
                {device.operating_system}
              </p>

              <p className="text-slate-400 text-sm">
                {device.browser}
              </p>

              <p className="text-green-400 text-sm">
                Trusted
              </p>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default TrustedDevices;
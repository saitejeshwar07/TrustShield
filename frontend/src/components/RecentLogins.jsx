import { useEffect, useState } from "react";
import { getRecentLogins } from "../services/loginHistory";

function RecentLogins() {
  const [logins, setLogins] = useState([]);

  useEffect(() => {
    loadLogins();
  }, []);

  const loadLogins = async () => {
    try {
      const data = await getRecentLogins();
      setLogins(data);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div className="bg-slate-900 rounded-2xl border border-slate-700 p-6 mt-8">
      <h2 className="text-white text-2xl font-bold mb-5">
        Recent Login Activity
      </h2>

      <div className="overflow-x-auto">
        <table className="w-full text-left">
          <thead>
            <tr className="text-slate-400 border-b border-slate-700">
              <th className="py-3">Time</th>
              <th>Browser</th>
              <th>Device</th>
              <th>Risk</th>
              <th>Decision</th>
            </tr>
          </thead>

          <tbody>
            {logins.map((login) => (
              <tr
                key={login.id}
                className="border-b border-slate-800"
              >
                <td className="py-4 text-white">
                  {new Date(login.created_at).toLocaleString()}
                </td>

                <td className="text-slate-300">
                  {login.browser}
                </td>

                <td className="text-slate-300">
                  {login.device_id}
                </td>

                <td className="text-yellow-400">
                  {login.risk_score}
                </td>

                <td className="text-green-400">
                  {login.decision}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default RecentLogins;
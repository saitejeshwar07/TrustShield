import { useState } from "react";
import { motion } from "framer-motion";
import { ShieldCheck, Lock, Mail } from "lucide-react";
import { Link, useNavigate } from "react-router-dom";
import { loginUser } from "../services/auth";
import { getDeviceInfo } from "../utils/deviceInfo";
import { registerDevice } from "../services/device";

function Login() {
  const navigate = useNavigate();

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

const handleLogin = async (e) => {
  e.preventDefault();

  setLoading(true);
  setError("");

  try {
    // Login
    const data = await loginUser(email, password);

    // Save JWT
    localStorage.setItem("access_token", data.access_token);

    /*
      For now we're using a fixed user ID.
      Later we'll decode the JWT and get the actual user ID.
    */
    const userId = 1;

    // Collect device info
    const device = await getDeviceInfo();

    // Send to backend
    await registerDevice({
      user_id: userId,
      ...device,
    });

    navigate("/dashboard");

  } catch (err) {
    console.error(err);
    setError("Invalid email or password.");
  } finally {
    setLoading(false);
  }
};

  return (
    <div className="min-h-screen bg-linear-to-br from-slate-950 via-slate-900 to-blue-950 flex items-center justify-center px-6">
      <motion.div
        initial={{ opacity: 0, y: 40 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.7 }}
        className="w-full max-w-md"
      >
        <div className="bg-white/10 backdrop-blur-xl border border-white/20 rounded-3xl shadow-2xl p-8">
          <div className="flex justify-center mb-5">
            <div className="bg-blue-600 p-4 rounded-full">
              <ShieldCheck size={36} className="text-white" />
            </div>
          </div>

          <h1 className="text-4xl font-bold text-center text-white">
            TrustShield AI
          </h1>

          <p className="text-center text-slate-300 mt-2 mb-8">
            AI Powered Identity Trust Platform
          </p>

          <form onSubmit={handleLogin} className="space-y-5">
            <div className="relative">
              <Mail
                size={18}
                className="absolute left-4 top-4 text-slate-400"
              />

              <input
                type="email"
                placeholder="Email"
                className="w-full rounded-xl bg-slate-900/70 border border-slate-700 py-3 pl-12 pr-4 text-white outline-none focus:border-blue-500"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                required
              />
            </div>

            <div className="relative">
              <Lock
                size={18}
                className="absolute left-4 top-4 text-slate-400"
              />

              <input
                type="password"
                placeholder="Password"
                className="w-full rounded-xl bg-slate-900/70 border border-slate-700 py-3 pl-12 pr-4 text-white outline-none focus:border-blue-500"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                required
              />
            </div>

            {error && (
              <p className="text-red-400 text-sm text-center">{error}</p>
            )}

            <button
              type="submit"
              disabled={loading}
              className="w-full rounded-xl bg-blue-600 py-3 text-white font-semibold hover:bg-blue-700 transition disabled:opacity-50"
            >
              {loading ? "Signing In..." : "Secure Login"}
            </button>
          </form>

          <div className="mt-8 text-center text-slate-300">
            Don't have an account?

            <Link
              to="/register"
              className="text-blue-400 ml-2 hover:text-blue-300"
            >
              Register
            </Link>
          </div>
        </div>

        <div className="mt-8 text-center text-slate-400 text-sm">
          ✓ AI Risk Detection &nbsp;&nbsp;
          ✓ Device Intelligence &nbsp;&nbsp;
          ✓ Privacy First
        </div>
      </motion.div>
    </div>
  );
}

export default Login;
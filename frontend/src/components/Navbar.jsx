import { ShieldCheck, Bell, UserCircle } from "lucide-react";

function Navbar() {
  return (
    <header className="h-16 bg-slate-900 border-b border-slate-700 flex items-center justify-between px-8">

      <div className="flex items-center gap-3">
        <ShieldCheck className="text-blue-500" size={28} />
        <h1 className="text-white text-xl font-bold">
          TrustShield AI
        </h1>
      </div>

      <div className="flex items-center gap-6">
        <Bell className="text-white cursor-pointer" />

        <div className="flex items-center gap-2">
          <UserCircle className="text-blue-400" size={34} />
          <span className="text-white">
            Sai
          </span>
        </div>
      </div>

    </header>
  );
}

export default Navbar;
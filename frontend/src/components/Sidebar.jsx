import {
  LayoutDashboard,
  Laptop,
  History,
  TriangleAlert
} from "lucide-react";

function Sidebar() {
  return (
    <aside className="w-64 bg-slate-900 border-r border-slate-700 min-h-screen p-6">

      <nav className="space-y-6">

        <div className="flex items-center gap-3 text-blue-400">
          <LayoutDashboard />
          Dashboard
        </div>

        <div className="flex items-center gap-3 text-slate-300">
          <Laptop />
          Devices
        </div>

        <div className="flex items-center gap-3 text-slate-300">
          <History />
          Login History
        </div>

        <div className="flex items-center gap-3 text-slate-300">
          <TriangleAlert />
          Alerts
        </div>

      </nav>

    </aside>
  );
}

export default Sidebar;
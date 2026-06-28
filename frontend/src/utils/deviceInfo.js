import axios from "axios";
import FingerprintJS from "@fingerprintjs/fingerprintjs";

export const getDeviceInfo = async () => {
  const fp = await FingerprintJS.load();
  const result = await fp.get();

  let ip = "";

  try {
    const response = await axios.get("https://api.ipify.org?format=json");
    ip = response.data.ip;
  } catch {
    ip = "Unknown";
  }

  return {
    device_id: result.visitorId,
    browser: navigator.userAgent,
    operating_system: navigator.platform,
    screen_resolution: `${window.screen.width}x${window.screen.height}`,
    timezone: Intl.DateTimeFormat().resolvedOptions().timeZone,
    language: navigator.language,
    ip_address: ip,
    login_time: new Date().toISOString(),
  };
};
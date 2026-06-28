import api from "./api";

export const registerDevice = async (device) => {
  const response = await api.post("/api/device/register", device);

  return response.data;
};

export const getDevices = async () => {
  const response = await api.get("/api/devices");
  return response.data;
};
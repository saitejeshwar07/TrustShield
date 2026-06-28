import api from "./api";

export const getRecentLogins = async () => {
    const response = await api.get("/api/dashboard/recent-logins");
    return response.data;
};
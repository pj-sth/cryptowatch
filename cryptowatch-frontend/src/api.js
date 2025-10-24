import axios from 'axios';

const API_BASE = "http://127.0.0.1:8000"; // FastAPI here

export const fetchPrice = async (coin) => {
    const res = await axios.get(`${API_BASE}/price/${coin}`);
    return res.data;
}

export const fetchTrending = async() => {
    const res = await axios.get(`${API_BASE}/trending`);
    return res.data;
}

export const fetchWatchlist = async() => {
    const res = await axios.get(`${API_BASE}/watchlist`);
    return res.data;
}
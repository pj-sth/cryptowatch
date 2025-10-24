import { useEffect, useState } from "react";
import { fetchTrending } from "../api";


export default function TrendingList() {

    const [ trending, setTrending ] = useState({ gainers: [], losers: [] });

    useEffect(() => {
        fetchTrending().then(setTrending);
    })

    return (
        <div className="p-4 bg-gray-900 text-white rounded-2xl shadow-md mt-6">
            <h2 className="text-xl font-semibold mb-3">
                Trending Coins
            </h2>
            <div className="grid grid-cols-2 gap-4">
                <div>
                    <h3 className="text-green-400 mb-2">
                        Top Gainers
                    </h3>
                    <ul>
                        {trending.gainers.map((coin, i) => {
                            <li key={i}>{coin}</li>
                        })}
                    </ul>
                </div>
                <div>
                    <h3 className="text-red-400 mb-2">
                        Top Losers
                    </h3>
                    <ul>
                        {trending.losers.map((coin, i) => (
                            <li key={i}>{coin}</li>
                        ))}
                    </ul>
                </div>
            </div>
        </div>
    );
}
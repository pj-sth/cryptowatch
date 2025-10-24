import { useState } from "react";
import { fetchPrice } from "../api";

export default function PriceCard() {
    
    const [ coin, setCoin ] = useState('bitcoin');
    const [ data, setData ] = useState(null);

    const getPrice = async() => {
        const result = await fetchPrice(coin);
        setData(result);
    }

    return (
        <div className="p-4 bg-gray-800 text-white rounded-2xl shadow-md w-full max-w-md mx-auto">
            <h2 className="text-xl font-semibold mb-3">
                Crypto Price Checker
            </h2>
            <input 
                type="text" 
                value={coin}
                onChange={(e) => setCoin(e.target.value)}
                className="p-2 w-full text-black rounded-md"
                placeholder="Enter coin name..."
            />
            <button
                onClick={getPrice}
                className="mt-3 bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 rounded-md"
            >
                Fetch Price
            </button>

            {
                data && (
                    <div className="mt-4">
                        <p className="text-lg">
                            {data.name} - ${data.price_usd}
                        </p>
                    </div>
                )
            }
            
        </div>
    )

}
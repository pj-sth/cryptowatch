import PriceCard from "./components/PriceCard";
import TrendingList from "./components/TrendingList";


export default function App() {
  return (
    <div className="min-h-screen bg-gray-950 p-6 flex flex-col items-center space-y-8">
      <h1 className="text-3xl font-bold text-blue-400 mb-4">
        CryptoWatch Dashboard
      </h1>
      <PriceCard />
      <TrendingList />
    </div>
  )
}
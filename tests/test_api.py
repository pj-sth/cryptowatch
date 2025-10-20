from cryptowatch_src import api

def test_fetch_price_returns_dict():
    result = api.fetch_price("bitcoin")
    assert isinstance(result, dict)
    assert "price_usd" in result
    assert result["name"].lower() == "bitcoin"
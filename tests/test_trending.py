from cryptowatch_src import trending

def test_trending_returns_two_lists():
    gainers, losers = trending.fetch_trending(limit=2)
    assert isinstance(gainers, list)
    assert isinstance(losers, list)
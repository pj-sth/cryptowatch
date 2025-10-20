import os
from cryptowatch_src import storage

def test_add_and_load_watchlist(tmp_path):
    test_file = tmp_path / "test_watchlist.json"
    storage.WATCHLIST_FILE = test_file

    storage.add_to_watchlist("bitcoin")
    data = storage.load_watchlist()
    assert "bitcoin" in data
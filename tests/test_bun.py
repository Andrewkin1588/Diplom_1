from bun import Bun
from unittest.mock import Mock



class TestBun:
    mock_bun = Mock()
    mock_bun.name = 'test'
    mock_bun.price = 15.6

    def test_get_name_bun(self):
        assert Bun.get_name(self.mock_bun) == 'test'

    def test_get_price_bun(self):
        assert Bun.get_price(self.mock_bun) == 15.6

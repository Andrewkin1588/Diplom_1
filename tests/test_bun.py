from bun import Bun


class TestBun:

    def test_get_name_bun(self, ingredient_mock):
        assert Bun.get_name(ingredient_mock) == 'test'

    def test_get_price_bun(self, ingredient_mock):
        assert Bun.get_price(ingredient_mock) == 15.6

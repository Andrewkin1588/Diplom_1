from ingredient import Ingredient
from unittest.mock import Mock


class TestIngredient:
    mock_ingredient = Mock()
    mock_ingredient.price = 15.5
    mock_ingredient.name = 'test'
    mock_ingredient.type = 'test'

    def test_get_ingredient_price(self):
        assert Ingredient.get_price(self.mock_ingredient) == 15.5

    def test_get_ingredient_name(self):
        assert Ingredient.get_name(self.mock_ingredient) == 'test'

    def test_get_ingredient_type(self):
        assert Ingredient.get_type(self.mock_ingredient) == 'test'

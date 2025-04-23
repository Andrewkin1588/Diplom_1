import pytest

from ingredient import Ingredient

class TestIngredient:

    def test_get_ingredient_price(self, ingredient_mock):
        assert Ingredient.get_price(ingredient_mock) == 15.5

    def test_get_ingredient_name(self, ingredient_mock):
        assert Ingredient.get_name(ingredient_mock) == 'test'

    def test_get_ingredient_type(self, ingredient_mock):
        assert Ingredient.get_type(ingredient_mock) == 'test'

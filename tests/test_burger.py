from bun import Bun
from burger import Burger
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger:

    def test_get_buns_from_burger(self):
        bun = Bun('test', 15)
        burger = Burger()
        burger.set_buns(bun)

        assert burger.bun.name == 'test'
        assert burger.bun.price == 15

    def test_add_ingredient(self):
        burger = Burger()
        ingr = Ingredient(INGREDIENT_TYPE_SAUCE, 'test', 15)
        burger.add_ingredient(ingr)

        assert burger.ingredients[0] == ingr

    def test_remove_ingredient(self):
        ingr = Ingredient(INGREDIENT_TYPE_SAUCE, 'test', 15)
        burger = Burger()
        burger.add_ingredient(ingr)
        burger.remove_ingredient(0)

        assert len(burger.ingredients) == 0

    def test_move_ingredient(self):
        ingr_index_0 = Ingredient(INGREDIENT_TYPE_SAUCE, 'test', 15)
        ingr_index_1 = Ingredient(INGREDIENT_TYPE_FILLING, 'test', 15)
        burger = Burger()
        burger.add_ingredient(ingr_index_0)
        burger.add_ingredient(ingr_index_1)
        burger.move_ingredient(0, 1)

        assert burger.ingredients[1] == ingr_index_0

    def test_get_price_bun_for_burger(self):
        burger = Burger()
        burger.set_buns(Bun('test', 15))

        assert burger.get_price() == 30

    def test_get_receipt(self):
        bun = Bun("test", 15)
        ingredient_filling = Ingredient(INGREDIENT_TYPE_FILLING, 'test filling', 15)
        ingredient_sauce = Ingredient(INGREDIENT_TYPE_SAUCE, 'test sauce', 15)
        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(ingredient_filling)
        burger.add_ingredient(ingredient_sauce)

        expected_receipt = (f'(==== {bun.get_name()} ====)'
                            f'\n= {ingredient_filling.get_type().lower()} {ingredient_filling.get_name()} ='
                            f'\n= {ingredient_sauce.get_type().lower()} {ingredient_sauce.get_name()} ='
                            f'\n(==== {bun.get_name()} ====)'
                            f'\n\nPrice: {burger.get_price()}')
        actual_receipt = burger.get_receipt()

        assert expected_receipt == actual_receipt

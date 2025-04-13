from database import Database


class TestDataBase:

    def test_available_buns(self):
        db = Database()

        assert db.available_buns() == db.buns

    def test_available_ingredients(self):
        db = Database()

        assert db.available_ingredients() == db.ingredients
import pytest
from unittest.mock import Mock


@pytest.fixture(scope="function")
def ingredient_mock():
    mock_ingredient = Mock()
    mock_ingredient.price = 15.5
    mock_ingredient.name = 'test'
    mock_ingredient.type = 'test'
    return mock_ingredient

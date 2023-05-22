import pytest
from unittest.mock import patch
import unittest.mock as mock
import src.static.diets as diets
from src.controllers.receipecontroller import ReceipeController

# # add your test case implementation here
# @pytest.mark.unit
# def test():
#     assert False

my_recepie = {
    "name": "Erik recepie",
    "diets": [
        "normal", "vegetarian"
    ],
    "ingredients": {
        "Butter": 100,
        "Banana": 4,
        "Sugar": 200,
        "Egg": 1,
        "Vanilla Sugar": 1,
        "Baking Powder": 0.5,
        "Salt": 5,
        "Cinnamon": 10,
        "Flour": 220,
        "Walnuts": 10
    }
}

available_items = {
    "Butter": 400,
    "Banana": 4,
    "Sugar": 200,
    "Egg": 1,
}


@pytest.fixture
def sut(readiness):
    with patch("src.util.calculator.calculate_readiness", autospec=True) as mocked_calculator:
            mocked_calculator.return_value = readiness
            mockedsut = ReceipeController()
            return mockedsut


@pytest.mark.unit
@pytest.mark.parametrize('readiness, diet, expected',
    [
        (0, diets.Diet("normal"), None),
        (0.1, diets.Diet("normal"), 0.1),
        (0.1, diets.Diet("vegan"), 0.1),
    ]
)
def test_readiness(sut, expected):
    result = sut.get_receipe_readiness(my_recepie, available_items)
    assert result == expected
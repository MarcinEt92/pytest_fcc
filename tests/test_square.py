import pytest
import resources.shapes as shapes



class TestSquare:
    @staticmethod
    def _get_area_data():
        return [(4, 16), (5, 25), (1, 1), (9, 81)]

    @staticmethod
    def _get_perimeter_data():
        return [(3, 12), (4, 16), (5, 20)]

    @pytest.mark.parametrize("side, expected_area", _get_area_data())
    def test_multiple_square_areas(self, side, expected_area):
        assert shapes.Square(side).area() == expected_area

    @pytest.mark.parametrize("side, expected_perimeter", _get_perimeter_data())
    def test_multiple_perimeters(self, side, expected_perimeter):
        assert shapes.Square(side).perimeter() == expected_perimeter

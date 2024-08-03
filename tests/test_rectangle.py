import pytest
import resources.shapes as shapes


class TestRectangle:
    def test_area(self, rectangle_01):
        assert rectangle_01.area() == 10 * 20

    def test_perimeter(self, rectangle_01):
        assert rectangle_01.perimeter() == 2 * 10 + 2 * 20

    def test_rectangle_equal(self, rectangle_01, rectangle_02):
        assert rectangle_01 != rectangle_02

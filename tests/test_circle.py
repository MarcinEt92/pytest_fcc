import math

import pytest
import resources.shapes as shapes


class TestCircle:
    def setup_method(self, method):
        circle_radius = 10
        self.circle = shapes.Circle(circle_radius)
        print(f"Setting up with Circle of radius: {circle_radius}")

    def teardown_method(selfself, method):
        print(f"Tear for down {method}")

    def test_area(self):
        assert self.circle.area() == math.pi * self.circle.radius ** 2

    def test_perimeter(self):
        assert self.circle.perimeter() == 2 * math.pi * self.circle.radius

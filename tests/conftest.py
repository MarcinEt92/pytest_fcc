import pytest
import resources.shapes as shapes


@pytest.fixture
def rectangle_01():
    return shapes.Rectangle(10, 20)


@pytest.fixture
def rectangle_02():
    return shapes.Rectangle(5, 6)

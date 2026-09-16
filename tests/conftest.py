import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import pytest
from rectangle import Rectangle
from circle import Circle
from square import Square
from triangle import Triangle

@pytest.fixture
def sample_rectangle():
    """Фикстура для создания прямоугольника"""
    return Rectangle(2, 3)

@pytest.fixture
def sample_rectangle2():
    """Фикстура для создания второго прямоугольника"""
    return Rectangle(4, 5)

@pytest.fixture
def sample_circle():
    """Фикстура для создания окружности"""
    return Circle(5)

@pytest.fixture
def sample_circle2():
    """Фикстура для создания второй окружности"""
    return Circle(3.5)

@pytest.fixture
def sample_square():
    """Фикстура для создания квадрата"""
    return Square(5)

@pytest.fixture
def sample_square2():
    """Фикстура для создания второго квадрата"""
    return Square(3.5)

@pytest.fixture
def sample_triangle():
    """Фикстура для создания треугольника"""
    return Triangle(3, 4, 5)

@pytest.fixture
def sample_triangle2():
    """Фикстура для создания второго треугольника"""
    return Triangle(6, 8, 10)

@pytest.fixture
def sample_triangle_equilateral():
    """Фикстура для создания равностороннего треугольника"""
    return Triangle(6, 6, 6)

@pytest.fixture
def all_figures(sample_rectangle, sample_circle, sample_square, sample_triangle):
    """Фикстура со всеми фигурами"""
    return [sample_rectangle, sample_circle, sample_square, sample_triangle]
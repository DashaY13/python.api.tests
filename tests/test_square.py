import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import pytest
from figure import Figure
from rectangle import Rectangle
from square import Square


class TestSquare:
    """Тесты для класса Square"""
    
    def test_square_creation(self):
        """Проверяем создание квадрата с корректной стороной"""
        square = Square(5)
        assert square.a == 5
        assert square.b == 5  # Квадрат наследует от Rectangle, где a = b = side
    
    def test_square_is_instance_of_rectangle(self, sample_square):
        """Проверяем, что Square наследуется от Rectangle"""
        assert isinstance(sample_square, Rectangle)
    
    def test_square_is_instance_of_figure(self, sample_square):
        """Проверяем, что Square наследуется от Figure"""
        assert isinstance(sample_square, Figure)
    
    def test_square_has_required_methods(self, sample_square):
        """Проверяем наличие обязательных методов"""
        assert hasattr(sample_square, 'get_area')
        assert hasattr(sample_square, 'get_perimeter')
        assert hasattr(sample_square, 'add_area')
    
    # Тесты на валидацию
    def test_square_side_zero_raises_error(self):
        """Проверяем, что сторона 0 вызывает ошибку"""
        with pytest.raises(ValueError, match="Square sides can't be less than or equal to 0"):
            Square(0)
    
    def test_square_side_negative_raises_error(self):
        """Проверяем, что отрицательная сторона вызывает ошибку"""
        with pytest.raises(ValueError, match="Square sides can't be less than or equal to 0"):
            Square(-5)
    
    def test_square_side_negative_float_raises_error(self):
        """Проверяем, что отрицательная дробная сторона вызывает ошибку"""
        with pytest.raises(ValueError, match="Square sides can't be less than or equal to 0"):
            Square(-3.14)
    
    def test_square_side_positive_works(self):
        """Проверяем, что положительная сторона работает"""
        square = Square(0.1)
        assert square.a == 0.1
        assert square.b == 0.1
    
    # Тесты на get_area
    def test_get_area_with_integer_side(self, sample_square):
        """Проверяем расчет площади с целой стороной"""
        assert sample_square.get_area() == 25  # 5²
    
    def test_get_area_with_float_side(self, sample_square2):
        """Проверяем расчет площади с дробной стороной"""
        expected_area = 3.5 ** 2
        assert sample_square2.get_area() == pytest.approx(expected_area, rel=1e-9)
    
    def test_get_area_with_side_one(self):
        """Проверяем расчет площади с стороной 1"""
        square = Square(1)
        assert square.get_area() == 1
    
    # Тесты на get_perimeter
    def test_get_perimeter_with_integer_side(self, sample_square):
        """Проверяем расчет периметра с целой стороной"""
        assert sample_square.get_perimeter() == 20  # 4 * 5
    
    def test_get_perimeter_with_float_side(self, sample_square2):
        """Проверяем расчет периметра с дробной стороной"""
        expected_perimeter = 4 * 3.5
        assert sample_square2.get_perimeter() == pytest.approx(expected_perimeter, rel=1e-9)
    
    def test_get_perimeter_with_side_one(self):
        """Проверяем расчет периметра с стороной 1"""
        square = Square(1)
        assert square.get_perimeter() == 4
    
    # Тесты на использование методов Rectangle
    def test_square_uses_rectangle_area(self, sample_square):
        """Проверяем, что площадь квадрата вычисляется через Rectangle"""
        rect = Rectangle(5, 5)
        assert sample_square.get_area() == rect.get_area()
    
    def test_square_uses_rectangle_perimeter(self, sample_square):
        """Проверяем, что периметр квадрата вычисляется через Rectangle"""
        rect = Rectangle(5, 5)
        assert sample_square.get_perimeter() == rect.get_perimeter()
    
    # Тесты на свойства
    def test_area_property(self, sample_square):
        """Проверяем свойство area"""
        assert sample_square.area == sample_square.get_area()
    
    def test_perimeter_property(self, sample_square):
        """Проверяем свойство perimeter"""
        assert sample_square.perimeter == sample_square.get_perimeter()
    
    # Тесты на add_area
    def test_add_area_with_another_square(self, sample_square, sample_square2):
        """Проверяем сложение площадей двух квадратов"""
        expected_sum = sample_square.get_area() + sample_square2.get_area()
        assert sample_square.add_area(sample_square2) == pytest.approx(expected_sum, rel=1e-9)
    
    def test_add_area_with_rectangle(self, sample_square, sample_rectangle):
        """Проверяем сложение площадей квадрата и прямоугольника"""
        expected_sum = sample_square.get_area() + sample_rectangle.get_area()
        assert sample_square.add_area(sample_rectangle) == expected_sum
    
    def test_add_area_with_same_square(self, sample_square):
        """Проверяем сложение площади с самой собой"""
        expected_sum = 2 * sample_square.get_area()
        assert sample_square.add_area(sample_square) == expected_sum
    
    # Параметризованные тесты
    @pytest.mark.parametrize("side, expected_area, expected_perimeter", [
        (1, 1, 4),
        (2, 4, 8),
        (5, 25, 20),
        (10, 100, 40),
        (2.5, 6.25, 10.0),
    ])
    def test_square_with_params(self, side, expected_area, expected_perimeter):
        """Параметризованный тест для разных квадратов"""
        square = Square(side)
        assert square.get_area() == pytest.approx(expected_area, rel=1e-9)
        assert square.get_perimeter() == pytest.approx(expected_perimeter, rel=1e-9)
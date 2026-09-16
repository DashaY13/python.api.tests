import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))


import pytest
import math
from figure import Figure
from circle import Circle
from rectangle import Rectangle


class TestCircle:
    """Тесты для класса Circle"""

    def test_circle_creation(self):
        """Проверяем создание окружности с корректным радиусом"""
        circle = Circle(5)
        assert circle.r == 5
    
    def test_circle_is_instance_of_figure(self, sample_circle):
        """Проверяем, что Circle наследуется от Figure"""
        assert isinstance(sample_circle, Figure)
    
    def test_circle_has_required_methods(self, sample_circle):
        """Проверяем наличие обязательных методов"""
        assert hasattr(sample_circle, 'get_area')
        assert hasattr(sample_circle, 'get_perimeter')
        assert hasattr(sample_circle, 'add_area')
    
    # Тесты на валидацию
    def test_circle_radius_zero_raises_error(self):
        """Проверяем, что радиус 0 вызывает ошибку"""
        with pytest.raises(ValueError, match="Circle radius can't be less than or equal to 0"):
            Circle(0)
    
    def test_circle_radius_negative_raises_error(self):
        """Проверяем, что отрицательный радиус вызывает ошибку"""
        with pytest.raises(ValueError, match="Circle radius can't be less than or equal to 0"):
            Circle(-5)
    
    def test_circle_radius_negative_float_raises_error(self):
        """Проверяем, что отрицательный дробный радиус вызывает ошибку"""
        with pytest.raises(ValueError, match="Circle radius can't be less than or equal to 0"):
            Circle(-3.14)
    
    def test_circle_radius_positive_works(self):
        """Проверяем, что положительный радиус работает"""
        circle = Circle(0.1)
        assert circle.r == 0.1
    
    # Тесты на get_area
    def test_get_area_with_integer_radius(self, sample_circle):
        """Проверяем расчет площади с целым радиусом"""
        expected_area = math.pi * 25  # π * 5²
        assert sample_circle.get_area() == pytest.approx(expected_area, rel=1e-9)
    
    def test_get_area_with_float_radius(self, sample_circle2):
        """Проверяем расчет площади с дробным радиусом"""
        expected_area = math.pi * (3.5 ** 2)
        assert sample_circle2.get_area() == pytest.approx(expected_area, rel=1e-9)
    
    def test_get_area_with_radius_one(self):
        """Проверяем расчет площади с радиусом 1"""
        circle = Circle(1)
        assert circle.get_area() == pytest.approx(math.pi, rel=1e-9)
    
    # Тесты на get_perimeter
    def test_get_perimeter_with_integer_radius(self, sample_circle):
        """Проверяем расчет периметра с целым радиусом"""
        expected_perimeter = 2 * math.pi * 5
        assert sample_circle.get_perimeter() == pytest.approx(expected_perimeter, rel=1e-9)
    
    def test_get_perimeter_with_float_radius(self, sample_circle2):
        """Проверяем расчет периметра с дробным радиусом"""
        expected_perimeter = 2 * math.pi * 3.5
        assert sample_circle2.get_perimeter() == pytest.approx(expected_perimeter, rel=1e-9)
    
    def test_get_perimeter_with_radius_one(self):
        """Проверяем расчет периметра с радиусом 1"""
        circle = Circle(1)
        assert circle.get_perimeter() == pytest.approx(2 * math.pi, rel=1e-9)
    
    # Тесты на свойства
    def test_area_property(self, sample_circle):
        """Проверяем свойство area"""
        assert sample_circle.area == sample_circle.get_area()
    
    def test_perimeter_property(self, sample_circle):
        """Проверяем свойство perimeter"""
        assert sample_circle.perimeter == sample_circle.get_perimeter()
    
    # Тесты на add_area
    def test_add_area_with_another_circle(self, sample_circle, sample_circle2):
        """Проверяем сложение площадей двух окружностей"""
        expected_sum = sample_circle.get_area() + sample_circle2.get_area()
        assert sample_circle.add_area(sample_circle2) == pytest.approx(expected_sum, rel=1e-9)
    
    def test_add_area_with_rectangle(self, sample_circle, sample_rectangle):
        """Проверяем сложение площадей окружности и прямоугольника"""
        expected_sum = sample_circle.get_area() + sample_rectangle.get_area()
        assert sample_circle.add_area(sample_rectangle) == pytest.approx(expected_sum, rel=1e-9)
    
    def test_add_area_with_same_circle(self, sample_circle):
        """Проверяем сложение площади с самой собой"""
        expected_sum = 2 * sample_circle.get_area()
        assert sample_circle.add_area(sample_circle) == pytest.approx(expected_sum, rel=1e-9)
    
    # Параметризованные тесты
    @pytest.mark.parametrize("radius, expected_area, expected_perimeter", [
        (1, math.pi, 2 * math.pi),
        (2, math.pi * 4, 4 * math.pi),
        (5, math.pi * 25, 10 * math.pi),
        (0.5, math.pi * 0.25, math.pi),
        (10, math.pi * 100, 20 * math.pi),
    ])
    def test_circle_with_params(self, radius, expected_area, expected_perimeter):
        """Параметризованный тест для разных окружностей"""
        circle = Circle(radius)
        assert circle.get_area() == pytest.approx(expected_area, rel=1e-9)
        assert circle.get_perimeter() == pytest.approx(expected_perimeter, rel=1e-9)
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import pytest
from figure import Figure
from rectangle import Rectangle


class TestRectangle:
    """Тесты для класса Rectangle"""
    
    def test_rectangle_creation(self):
        """Проверяем создание прямоугольника с корректными сторонами"""
        rect = Rectangle(2, 3)
        assert rect.a == 2
        assert rect.b == 3
    
    def test_rectangle_is_instance_of_figure(self, sample_rectangle):
        """Проверяем, что Rectangle наследуется от Figure"""
        assert isinstance(sample_rectangle, Figure)
    
    def test_rectangle_has_required_methods(self, sample_rectangle):
        """Проверяем наличие обязательных методов"""
        assert hasattr(sample_rectangle, 'get_area')
        assert hasattr(sample_rectangle, 'get_perimeter')
        assert hasattr(sample_rectangle, 'add_area')
    
    # Тесты на get_area
    def test_get_area_with_positive_values(self, sample_rectangle):
        """Проверяем расчет площади с положительными значениями"""
        area = sample_rectangle.get_area()
        assert area == 6  # 2 * 3 = 6
    
    def test_get_area_with_large_values(self):
        """Проверяем расчет площади с большими значениями"""
        rect = Rectangle(100, 200)
        assert rect.get_area() == 20000
    
    def test_get_area_with_square(self):
        """Проверяем расчет площади квадрата через Rectangle"""
        rect = Rectangle(5, 5)
        assert rect.get_area() == 25
    
    def test_get_area_with_zero_value(self):
        """Проверяем расчет площади с нулевым значением"""
        rect = Rectangle(0, 5)
        assert rect.get_area() == 0
    
    # Тесты на get_perimeter
    def test_get_perimeter_with_positive_values(self, sample_rectangle):
        """Проверяем расчет периметра с положительными значениями"""
        perimeter = sample_rectangle.get_perimeter()
        assert perimeter == 10  # 2 * (2 + 3) = 10
    
    def test_get_perimeter_with_large_values(self):
        """Проверяем расчет периметра с большими значениями"""
        rect = Rectangle(100, 200)
        assert rect.get_perimeter() == 600  # 2 * (100 + 200) = 600
    
    def test_get_perimeter_with_square(self):
        """Проверяем расчет периметра квадрата через Rectangle"""
        rect = Rectangle(5, 5)
        assert rect.get_perimeter() == 20  # 2 * (5 + 5) = 20
    
    def test_get_perimeter_with_zero_value(self):
        """Проверяем расчет периметра с нулевым значением"""
        rect = Rectangle(0, 5)
        assert rect.get_perimeter() == 10  # 2 * (0 + 5) = 10
    
    # Тесты на свойства
    def test_area_property(self, sample_rectangle, sample_rectangle2):
        """Проверяем, что свойство area возвращает корректное значение"""
        assert sample_rectangle.area == 6
        assert sample_rectangle2.area == 20
    
    def test_perimeter_property(self, sample_rectangle, sample_rectangle2):
        """Проверяем, что свойство perimeter возвращает корректное значение"""
        assert sample_rectangle.perimeter == 10
        assert sample_rectangle2.perimeter == 18
    
    def test_area_and_get_area_are_equal(self, sample_rectangle):
        """Проверяем, что свойство area и метод get_area возвращают одинаковые значения"""
        assert sample_rectangle.area == sample_rectangle.get_area()
    
    def test_perimeter_and_get_perimeter_are_equal(self, sample_rectangle):
        """Проверяем, что свойство perimeter и метод get_perimeter возвращают одинаковые значения"""
        assert sample_rectangle.perimeter == sample_rectangle.get_perimeter()
    
    # Тесты на add_area
    def test_add_area_with_another_rectangle(self, sample_rectangle, sample_rectangle2):
        """Проверяем сложение площадей двух прямоугольников"""
        result = sample_rectangle.add_area(sample_rectangle2)
        assert result == 26  # 6 + 20 = 26
    
    def test_add_area_with_same_rectangle(self, sample_rectangle):
        """Проверяем сложение площади прямоугольника с самим собой"""
        result = sample_rectangle.add_area(sample_rectangle)
        assert result == 12  # 6 + 6 = 12
    
    def test_add_area_commutativity(self, sample_rectangle, sample_rectangle2):
        """Проверяем коммутативность сложения площадей"""
        result1 = sample_rectangle.add_area(sample_rectangle2)
        result2 = sample_rectangle2.add_area(sample_rectangle)
        assert result1 == result2
    
    def test_add_area_with_invalid_type(self, sample_rectangle):
        """Проверяем, что add_area выбрасывает исключение для неправильного типа"""
        with pytest.raises(ValueError, match="Should be a Figure"):
            sample_rectangle.add_area("not a figure")
    
    # Параметризованные тесты
    @pytest.mark.parametrize("a, b, expected_area, expected_perimeter", [
        (2, 3, 6, 10),
        (4, 5, 20, 18),
        (1, 1, 1, 4),
        (0, 5, 0, 10),
        (10.5, 2.5, 26.25, 26.0),
    ])
    def test_rectangle_with_params(self, a, b, expected_area, expected_perimeter):
        """Параметризованный тест для разных прямоугольников"""
        rect = Rectangle(a, b)
        assert rect.get_area() == expected_area
        assert rect.get_perimeter() == expected_perimeter
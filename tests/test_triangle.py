import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import pytest
from figure import Figure
from triangle import Triangle
from rectangle import Rectangle


class TestTriangle:
    """Тесты для класса Triangle"""
    
    def test_triangle_creation(self):
        """Проверяем создание треугольника с корректными сторонами"""
        triangle = Triangle(3, 4, 5)
        assert triangle.a == 3
        assert triangle.b == 4
        assert triangle.c == 5
    
    def test_triangle_is_instance_of_figure(self, sample_triangle):
        """Проверяем, что Triangle наследуется от Figure"""
        assert isinstance(sample_triangle, Figure)
    
    def test_triangle_has_required_methods(self, sample_triangle):
        """Проверяем наличие обязательных методов"""
        assert hasattr(sample_triangle, 'get_area')
        assert hasattr(sample_triangle, 'get_perimeter')
        assert hasattr(sample_triangle, 'add_area')
    
    # Тесты на валидацию сторон
    def test_triangle_negative_side_raises_error(self):
        """Проверяем, что отрицательная сторона вызывает ошибку"""
        with pytest.raises(ValueError, match="Triangle sides must be positive"):
            Triangle(-1, 2, 3)
    
    def test_triangle_zero_side_raises_error(self):
        """Проверяем, что нулевая сторона вызывает ошибку"""
        with pytest.raises(ValueError, match="Triangle sides must be positive"):
            Triangle(0, 2, 3)
    
    def test_triangle_all_negative_sides_raises_error(self):
        """Проверяем, что все отрицательные стороны вызывают ошибку"""
        with pytest.raises(ValueError, match="Triangle sides must be positive"):
            Triangle(-1, -2, -3)
    
    # Тесты на проверку существования треугольника
    def test_triangle_impossible_sides_raises_error(self):
        """Проверяем, что невозможный треугольник вызывает ошибку"""
        with pytest.raises(ValueError, match="Impossible triangle sides"):
            Triangle(1, 2, 3)  # 1 + 2 = 3, не треугольник
    
    def test_triangle_too_small_side_raises_error(self):
        """Проверяем, что слишком маленькая сторона вызывает ошибку"""
        with pytest.raises(ValueError, match="Impossible triangle sides"):
            Triangle(1, 1, 3)  # 1 + 1 = 2 < 3
    
    def test_triangle_one_side_too_long_raises_error(self):
        """Проверяем, что слишком длинная сторона вызывает ошибку"""
        with pytest.raises(ValueError, match="Impossible triangle sides"):
            Triangle(10, 2, 3)  # 2 + 3 = 5 < 10
    
    def test_triangle_valid_sides_work(self):
        """Проверяем, что корректные стороны работают"""
        triangle = Triangle(3, 4, 5)
        assert triangle.a == 3
        assert triangle.b == 4
        assert triangle.c == 5
    
    # Тесты на get_area
    def test_get_area_of_right_triangle(self, sample_triangle):
        """Проверяем расчет площади прямоугольного треугольника"""
        # Для треугольника 3-4-5: площадь = (3 * 4) / 2 = 6
        assert sample_triangle.get_area() == 6
    
    def test_get_area_of_similar_triangle(self, sample_triangle2):
        """Проверяем расчет площади подобного треугольника"""
        # Для треугольника 6-8-10: площадь = (6 * 8) / 2 = 24
        assert sample_triangle2.get_area() == 24
    
    def test_get_area_of_equilateral_triangle(self, sample_triangle_equilateral):
        """Проверяем расчет площади равностороннего треугольника"""
        # Для треугольника 6-6-6: p = 9, площадь = sqrt(9 * 3 * 3 * 3) = sqrt(243)
        expected_area = (9 * 3 * 3 * 3) ** 0.5  # sqrt(243)
        assert sample_triangle_equilateral.get_area() == pytest.approx(expected_area, rel=1e-9)
    
    def test_get_area_of_isosceles_triangle(self):
        """Проверяем расчет площади равнобедренного треугольника"""
        triangle = Triangle(5, 5, 6)
        # p = 8, площадь = sqrt(8 * 3 * 3 * 2) = sqrt(144) = 12
        expected_area = 12
        assert triangle.get_area() == pytest.approx(expected_area, rel=1e-9)
    
    # Тесты на get_perimeter
    def test_get_perimeter_of_right_triangle(self, sample_triangle):
        """Проверяем расчет периметра прямоугольного треугольника"""
        assert sample_triangle.get_perimeter() == 12  # 3 + 4 + 5 = 12
    
    def test_get_perimeter_of_similar_triangle(self, sample_triangle2):
        """Проверяем расчет периметра подобного треугольника"""
        assert sample_triangle2.get_perimeter() == 24  # 6 + 8 + 10 = 24
    
    def test_get_perimeter_of_equilateral_triangle(self, sample_triangle_equilateral):
        """Проверяем расчет периметра равностороннего треугольника"""
        assert sample_triangle_equilateral.get_perimeter() == 18  # 6 + 6 + 6 = 18
    
    def test_get_perimeter_of_isosceles_triangle(self):
        """Проверяем расчет периметра равнобедренного треугольника"""
        triangle = Triangle(5, 5, 6)
        assert triangle.get_perimeter() == 16  # 5 + 5 + 6 = 16
    
    # Тесты на свойства
    def test_area_property(self, sample_triangle):
        """Проверяем свойство area"""
        assert sample_triangle.area == sample_triangle.get_area()
    
    def test_perimeter_property(self, sample_triangle):
        """Проверяем свойство perimeter"""
        assert sample_triangle.perimeter == sample_triangle.get_perimeter()
    
    # Тесты на add_area
    def test_add_area_with_another_triangle(self, sample_triangle, sample_triangle2):
        """Проверяем сложение площадей двух треугольников"""
        expected_sum = sample_triangle.get_area() + sample_triangle2.get_area()
        assert sample_triangle.add_area(sample_triangle2) == expected_sum
    
    def test_add_area_with_rectangle(self, sample_triangle, sample_rectangle):
        """Проверяем сложение площадей треугольника и прямоугольника"""
        expected_sum = sample_triangle.get_area() + sample_rectangle.get_area()
        assert sample_triangle.add_area(sample_rectangle) == expected_sum
    
    def test_add_area_with_same_triangle(self, sample_triangle):
        """Проверяем сложение площади с самой собой"""
        expected_sum = 2 * sample_triangle.get_area()
        assert sample_triangle.add_area(sample_triangle) == expected_sum
    
    def test_add_area_with_circle(self, sample_triangle, sample_circle):
        """Проверяем сложение площадей треугольника и окружности"""
        expected_sum = sample_triangle.get_area() + sample_circle.get_area()
        assert sample_triangle.add_area(sample_circle) == pytest.approx(expected_sum, rel=1e-9)
    
    # Параметризованные тесты
    @pytest.mark.parametrize("a, b, c, expected_area, expected_perimeter", [
        (3, 4, 5, 6, 12),        # Прямоугольный треугольник
        (5, 5, 6, 12, 16),       # Равнобедренный треугольник
        (6, 8, 10, 24, 24),      # Подобный первому
        (6, 6, 6, (9 * 3 * 3 * 3) ** 0.5, 18),  # Равносторонний
        (7, 8, 9, (12 * 5 * 4 * 3) ** 0.5, 24),  # Разносторонний
    ])
    def test_triangle_with_params(self, a, b, c, expected_area, expected_perimeter):
        """Параметризованный тест для разных треугольников"""
        triangle = Triangle(a, b, c)
        assert triangle.get_perimeter() == expected_perimeter
        assert triangle.get_area() == pytest.approx(expected_area, rel=1e-9)
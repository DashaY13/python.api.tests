import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import pytest
from figure import Figure
from rectangle import Rectangle


class TestFigure:
    """Тесты для абстрактного класса Figure"""
    
    def test_cannot_instantiate_abstract_class(self):
        """Проверяем, что нельзя создать экземпляр абстрактного класса"""
        with pytest.raises(TypeError):
            Figure()
    
    def test_add_area_with_invalid_object(self):
        """Проверяем, что add_area выбрасывает исключение для не-Figure"""
        rectangle = Rectangle(2, 3)
        with pytest.raises(ValueError, match="Should be a Figure"):
            rectangle.add_area("not a figure")
    
    def test_add_area_with_none(self):
        """Проверяем, что add_area выбрасывает исключение для None"""
        rectangle = Rectangle(2, 3)
        with pytest.raises(ValueError, match="Should be a Figure"):
            rectangle.add_area(None)
    
    def test_add_area_with_number(self):
        """Проверяем, что add_area выбрасывает исключение для числа"""
        rectangle = Rectangle(2, 3)
        with pytest.raises(ValueError, match="Should be a Figure"):
            rectangle.add_area(42)
    
    def test_add_area_with_properties(self, sample_rectangle, sample_rectangle2):
        """Проверяем работу add_area через свойства area"""
        expected_sum = sample_rectangle.area + sample_rectangle2.area
        
        result = sample_rectangle.add_area(sample_rectangle2)
        
        assert result == expected_sum
        assert result == 26  # 6 + 20 = 26
    
    def test_add_area_commutativity(self, sample_rectangle, sample_rectangle2):
        """Проверяем коммутативность сложения площадей"""
        result1 = sample_rectangle.add_area(sample_rectangle2)
        result2 = sample_rectangle2.add_area(sample_rectangle)
        assert result1 == result2
    
    def test_add_area_with_same_figure(self, sample_rectangle):
        """Проверяем сложение площади фигуры с самой собой"""
        result = sample_rectangle.add_area(sample_rectangle)
        assert result == 12  # 6 + 6 = 12
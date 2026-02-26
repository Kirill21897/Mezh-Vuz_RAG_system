import pytest
import os

class TestUniversityModel:
    """Тесты для модели Университета"""
    
    def test_create_university(self):
        """Тест создания университета"""
        from scripts.connection_to_database import University
        university = University(name="Test University")
        uni = University(
            name="Тестовый Университет",
            short_name="ТУ",
            city="Москва",
            rating=4.5
        )
        assert uni.name == "Тестовый Университет"
        assert uni.short_name == "ТУ"
        assert uni.city == "Москва"
        assert uni.rating == 4.5
        
    def test_university_repr(self):
        """Тест строкового представления университета"""
        from scripts.connection_to_database import University
        uni = University(short_name="МГУ",  city="Москва")
        assert "МГУ" in repr(uni)
        assert "Москва" in repr(uni)
        
    def test_university_has_programm_attr(self):
        """Проверка связи с программами"""
        from scripts.connection_to_database import University
        uni = University()
        assert hasattr(uni, "programs")

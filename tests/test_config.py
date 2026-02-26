import pytest
import os


class TestConfig:
    """Тесты для проверки конфигурации"""
    
    def test_database_url(self):
        """Проверка наличия DATABASE_URL в конфигурации"""
        from config.settings import config
        assert config.DATABASE_URL is not None
        assert len(config.DATABASE_URL) > 0
    
    def test_database_url_is_str(self):
        """Проверка что DATABASE_URL является строкой"""
        from config.settings import config
        assert isinstance(config.DATABASE_URL, str)
        
    def test_database_url_has_protocol(self):
        """Проверка наличия протокола в DATABASE_URL"""
        from config.settings import config
        protocls = ["postgresql://", "mysql://", "sqlite://"]
        assert any(protocol in config.DATABASE_URL for protocol in protocls)
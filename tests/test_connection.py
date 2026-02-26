import pytest
import sys
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock

sys.path.insert(0, str(Path(__file__).parent.parent))

class TestDatabaseConnection:
    """"Тесты подключения к базе данных"""
    
    def test_engine_created(self):
        """Тест создания движка SQLAlchemy"""
        from scripts.connection_to_database import engine
        assert engine is not None
        assert hasattr(engine, 'connect')
        
    def test_session_created(self):
        """Тест создания сессии"""
        from scripts.connection_to_database import Session
        session = Session()
        assert session is not None
        assert hasattr(session, 'query')
        session.close()
        
    def test_base_declarative(self):
        """Тест базового класса моделей"""
        from scripts.connection_to_database import Base
        assert Base is not None
        assert hasattr(Base, 'metadata')
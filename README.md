# Mezh-Vuz RAG System

Система для управления и поиска информации о межуниверситетских программах и вузах. Проект представляет собой компонент для RAG-системы (Retrieval-Augmented Generation), обеспечивающий хранение и доступ к структурированным данным об учебных заведениях и их программах.

## Структура проекта

*   `config/` — Конфигурация и настройки (чтение переменных окружения).
*   `data/` — Директория с исходными данными (Excel-файлы `programs.xlsx`, `universities.xlsx`).
*   `scripts/` — Основные скрипты:
    *   `connection_to_database.py` — Описание ORM-моделей (`University`, `Programs`) и функции для работы с БД.
*   `tests/` — Модульные тесты.

## Технологический стек

*   **Python**
*   **SQLAlchemy** — ORM для взаимодействия с базой данных.
*   **PostgreSQL** — Используемая СУБД (драйвер `psycopg2-binary`).
*   **Pandas**, **Docling** — Инструменты для обработки данных.
*   **Pytest** — Фреймворк для тестирования.

## Установка и настройка

1.  **Клонируйте репозиторий:**
    ```bash
    git clone <URL_репозитория>
    cd Mezh-Vuz_RAG_system
    ```

2.  **Создайте виртуальное окружение:**
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # Linux/macOS
    source venv/bin/activate
    ```

3.  **Установите зависимости:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Настройте переменные окружения:**
    Создайте файл `.env` в корне проекта и добавьте строку подключения к базе данных:
    ```ini
    DATABASE_URL=postgresql://user:password@host:port/database_name
    ```

## Использование

Для работы с базой данных используются модели из `scripts/connection_to_database.py`. Пример получения сессии:

```python
from scripts.connection_to_database import get_session, University

session = get_session()
universities = session.query(University).all()
print(universities)
```

## Тестирование

Запуск тестов осуществляется командой:
```bash
pytest
```

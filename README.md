# FastAPI Base — базовый шаблон для приложений на FastAPI
FastAPI — это современный фреймворк для создания API на Python с аннотациями типов.
Он хорошо подходит для сервисов, где важны скорость разработки и автоматическая документация.
![screenshot](screenshot.jpg)

## 🔧 В шаблоне реализовано:
- Базовая структура проекта
- Конфигурация через настройки (`pydantic-settings`) и `.env`
- API версии `v1` с зависимостями и слоями (`schemas`, `services`, `repositories`)
- Асинхронный доступ к БД: SQLAlchemy 2 и `aiosqlite`
- Миграции Alembic и пример эндпоинтов `health` и `users`

## 📦 Структура проекта
```
├── alembic/
│   ├── versions/
│   └── env.py
├── app/
│   ├── api/
│   │   ├── deps.py
│   │   └── v1/
│   │       ├── router.py
│   │       └── endpoints/
│   ├── core/
│   ├── db/
│   ├── models/
│   ├── repositories/
│   ├── schemas/
│   ├── services/
│   ├── utils/
│   └── main.py
├── tests/
├── alembic.ini
├── env.example
├── pyproject.toml
├── requirements.txt
├── requirements-dev.txt
└── README.md
```

## ⚙️ Установка и запуск
```bash
git clone https://gitverse.ru/Rockdukan/fastapi-base.git
cd fastapi-base
uv venv
uv sync
uv run uvicorn app.main:app --host 127.0.0.1 --port 8000
```

Если вы предпочитаете устанавливать зависимости из `requirements.txt`, можно сделать так:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -e .
uvicorn app.main:app --host 127.0.0.1 --port 8000
```

## 🧪 Тестирование
```bash
uv sync --extra dev
uv run pytest -q
```

## 🌐 Маршруты

- `GET /api/v1/health`  
  Проверка работоспособности. Возвращает JSON:

  ```json
  {"status": "ok"}
  ```

- `POST /api/v1/users`  
  Создание пользователя. Тело: email и пароль. Ответ: данные пользователя в JSON.

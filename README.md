# FastAPI Base — базовый шаблон для приложений на FastAPI
FastAPI — это современный фреймворк для создания API на Python с аннотациями типов.
Он хорошо подходит для сервисов, где важны скорость разработки и автоматическая документация.


## 🔧 В шаблоне реализовано:
- Базовая структура проекта
- Конфигурация через настройки (`pydantic-settings`) и `.env`
- API версии `v1` с эндпоинтом `health`

## 📦 Структура проекта
```
├── app/
│   ├── api/
│   │   └── v1/
│   │       ├── router.py
│   │       └── endpoints/
│   ├── core/
│   └── main.py
├── tests/
├── env.example
├── pyproject.toml
├── requirements.txt
├── run.py
└── README.md
```

## ⚙️ Установка и запуск
#### uv
```bash
git clone https://gitverse.ru/Rockdukan/fastapi-base.git
cd fastapi-base
uv venv
uv sync
uv run python run.py
```

#### venv
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python run.py
```

## 🧪 Тестирование
```bash
uv sync
uv run pytest -q
```

#### venv
```bash
pytest -q
```

## 🌐 Маршруты

- `GET /api/v1/health`  
  Проверка работоспособности. Возвращает JSON:

  ```json
  {"status": "ok"}
  ```

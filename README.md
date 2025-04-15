# 🚀 Live Task Manager

FastAPI-приложение для управления задачами с поддержкой **реального времени** через **WebSocket**.

🔗 Репозиторий: [github.com/antiquastepposus/live-task-manager](https://github.com/antiquastepposus/live-task-manager)

---

## 🛠 Используемые технологии

- **FastAPI** — backend фреймворк  
- **SQLAlchemy** — ORM  
- **Pydantic v2** — валидация данных  
- **PostgreSQL** — база данных  
- **Alembic** — миграции  
- **JWT (PyJWT)** — авторизация  
- **WebSocket** — обновление задач в реальном времени  
- **Uvicorn** — сервер для запуска  
- **dotenv** — переменные окружения  
- **asyncpg / psycopg2-binary** — драйверы БД  
- **gevent / websockets** — для WebSocket-клиентов  
- см. [📦 Зависимости](#-зависимости)

---

## ⚙️ Установка и запуск

### 1. Клонировать репозиторий

```bash
git clone https://github.com/antiquastepposus/live-task-manager.git
cd live-task-manager
```

### 2. Создать и активировать виртуальное окружение

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows
```

### 3. Установить зависимости

```bash
pip install -r requirements.txt
```

### 4. Создать `.env`

Создай `.env` файл на основе `.env.example`:

```bash
cp .env.example .env
```

---

## 🗄 Применить миграции базы данных

```bash
alembic upgrade head
```

---

## 🚀 Запуск приложения

```bash
uvicorn app.main:app --reload
```

---

## 🌐 WebSocket

### URL WebSocket-подключения:

```
ws://127.0.0.1:8000/ws/tasks
```

### 🔌 Пример клиента (Python)

```python
import asyncio
import websockets

async def main():
    uri = "ws://127.0.0.1:8000/ws/tasks"
    async with websockets.connect(uri) as websocket:
        while True:
            message = await websocket.recv()
            print("Received:", message)

asyncio.run(main())
```

📌 Если используется JWT токен:

```python
headers = {
    "Authorization": "Bearer <your_jwt_token>"
}
async with websockets.connect(uri, extra_headers=headers) as websocket:
    ...
```

---

## 🧪 API эндпоинты

- `GET /tasks/` — получить все задачи  
- `POST /tasks/` — создать задачу  
- `PUT /tasks/{id}` — обновить задачу  
- `DELETE /tasks/{id}` — удалить задачу  
- `GET /ws/tasks` — WebSocket-поток событий  

---

## 📦 Зависимости (`requirements.txt`)

```
alembic==1.15.2
annotated-types==0.7.0
anyio==4.9.0
asyncpg==0.30.0
click==8.1.8
fastapi==0.115.12
gevent==24.11.1
greenlet==3.1.1
h11==0.14.0
idna==3.10
Mako==1.3.10
MarkupSafe==3.0.2
passlib==1.7.4
psycopg2-binary==2.9.10
pydantic==2.11.3
pydantic-settings==2.8.1
pydantic_core==2.33.1
PyJWT==2.10.1
python-dotenv==1.1.0
python-multipart==0.0.20
setuptools==78.1.0
sniffio==1.3.1
SQLAlchemy==2.0.40
starlette==0.46.1
typing-inspection==0.4.0
typing_extensions==4.13.2
uvicorn==0.34.1
websocket==0.2.1
websockets==15.0.1
zope.event==5.0
zope.interface==7.2
```

---

## 📄 Пример `.env`

```env
DB_HOST=localhost
DB_PORT=5432
DB_USER=myuser
DB_PASS=mypassword
DB_NAME=mydatabase
SECRET_KEY=mysecretkey
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

## 🧾 Лицензия

Проект доступен под лицензией MIT.

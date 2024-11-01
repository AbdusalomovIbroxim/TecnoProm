# TecnoProm Backend API

TecnoProm Backend API — это серверная часть для проекта TecnoProm, разработанная на Django и предоставляющая RESTful API для управления и взаимодействия с приложением недвижимости. API поддерживает полный функционал платформы, включая управление объектами недвижимости, пользователями и заказами.

## Основные возможности
- **Управление объектами недвижимости**: Создание, обновление, удаление и просмотр информации об объектах недвижимости.
- **Аутентификация и авторизация**: Безопасная регистрация и вход пользователей с использованием JWT.
- **Фильтрация и сортировка**: Гибкая система фильтрации объектов по цене, местоположению и другим параметрам.
- **Управление заказами**: Работа с заказами клиентов и обработка платежей.
- **Поддержка реального времени**: Обновления в режиме реального времени с использованием WebSocket.
- **Документация API**: Swagger/OpenAPI для удобного ознакомления с API.

## Стек технологий
- **Python** и **Django** — основной фреймворк.
- **Django REST Framework (DRF)** — для построения RESTful API.
- **PostgreSQL** — для хранения данных.
- **JWT (JSON Web Tokens)** — для аутентификации пользователей.
- **Redis и Django Channels** — для поддержки WebSocket и уведомлений в реальном времени.

## Начало работы
### Предварительные требования
- Python 3.8+
- PostgreSQL
- Redis (для WebSocket)

### Установка
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/yourusername/tecnoprom-backend.git
   ```
2. Перейдите в папку проекта и создайте виртуальное окружение:
   ```bash
   cd tecnoprom-backend
   python -m venv venv
   source venv/bin/activate  # для Linux/macOS
   venv\Scripts\activate     # для Windows
   ```
3. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
4. Настройте переменные окружения:
   - Создайте `.env` файл на основе `.env.example`.
   - Укажите параметры базы данных, секретный ключ и настройки JWT.

5. Выполните миграции:
   ```bash
   python manage.py migrate
   ```

6. Запустите сервер разработки:
   ```bash
   python manage.py runserver
   ```

## Документация API
Подробная документация доступна по пути `/api/docs` после запуска сервера (если включен Swagger).

---


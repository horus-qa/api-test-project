# Test API Projects

Два автоматизированных учебных теста для проверки API. 

Первый тест - test_google_maps_api для ресурса [rahulshettyacademy.com](https://rahulshettyacademy.com/) -
содержит тесты для проверки CRUD-операций Google Maps API. Полный цикл тестирования: создание, чтение, обновление и удаление локаций с валидацией ответов.

Особенности реализации:
* Паттерн Page Object для API (GoogleMapsApi)
* Кастомные проверки с валидацией статус-кодов, JSON-структуры и значений
* Интеграция с Allure Framework для отчетности
* Разделение на методы API и проверки

Второй тест - star_wars_api для ресурса [swapi.dev]( https://swapi.dev/) - содержит скрипт для анализа вселенной Star Wars через SWAPI. Находит всех персонажей, которые снимались в одних фильмах с Дартом Вейдером, и сохраняет их имена в файл без дубликатов.

Особенности:
* Обработка HTTP-ошибок и пропуск недоступных данных
* Устранение дубликатов через множества (set)
* Логирование процесса выполнения
* Архитектура с разделением функций

## 📁 Структура проекта

<pre> <code>
api-test-project/
├── tests/                    # Директория с тестами
│   ├── test_google_maps.py   # Тесты Google Maps API (CRUD)
│   └── test_star_wars.py     # Скрипт анализа Star Wars API
├── utils/                    # Вспомогательные модули
│   ├── api.py               # Основные API-методы и клиенты
│   ├── http_methods.py      # Базовые HTTP-методы (GET, POST, PUT, DELETE)
│   ├── checking.py          # Утилиты для проверок и assertions
│   └── logger.py            # Логирование
├── test_results/            # Результаты тестов
├── logs/                    # Файлы логов
├── requirements.txt         # Зависимости
└── README.md </code> </pre>


## 🚀 Как запустить

1. Клонировать репозиторий
````
git clone https://github.com/horus-qa/api-test-project.git

cd api-test-project
````
2. Создать и активировать виртуальное окружение
````
python -m venv venv
````
Для Windows:
````
venv\Scripts\activate
````

Для macOS/Linux:
````
source venv/bin/activate
````

3. Установить зависимости
````
pip install -r requirements.txt
````

4. Запустить тест
````
# Все тесты
pytest tests/

# С генерацией Allure отчета
pytest --alluredir=test_results/ tests/
````

## 🧰 Используемые технологии

* Python
* Pytest
* Allure
* Requests
### Задания по пройденному материалу
---
#### 1. Веб-скрейпинг
* `Задание`: Реализовать модель веб-скрейпинга для сети торговых магазинов `Виктория`.
* `Веб-сайт`: https://www.victoria-group.ru/company/shops/.
* `Тип данных`: пространcтвенные данные (точки торговой сети).
* `Метод извлечения`: с помощью REST API (GET запрос).
* `Итоговый формат данных`: GeoJSON или CSV.
* `Рекомендуемые библиотеки`: requests, pandas, BeautifulSoup

---
#### 2. Геокодирование
* `Задание`: Реализовать функцию обратного геокодирования, для получения списка адресов по координатам.
* `Документация сревиса`: https://developer.here.com/documentation/geocoding-search-api/dev_guide/topics/endpoint-reverse-geocode-brief.html.
* `Итоговый формат`: функция на Python принимающая в виде аргументов координаты (широта, долгота) и возвращающая информацию об адресах по координатам.
* `Рекомендуемые библиотеки`: requests

---
### 3. Визуализация геоданных на Python с помощью Folium
* `Задание`: Создать карту распространения COVID-19.
* `Данные по заболеваемости`: https://github.com/CSSEGISandData/COVID-19.
* `Документация Folium`: http://python-visualization.github.io/folium/
* `Рекомендуемые библиотеки`: folium

---
### 4. Облачное хранилище DataHub
* `Задание`: Реализовать функцию поиска пространственных объектов внутри базы данных.
* `Документация DataHub API`: https://www.here.xyz/api/.
* `Методы поиска в Data Hub API`: search, bbox, spatial

---
### 5. Сервис геомаркетингового анализа на FastAPI
* `Задание`: Реализовать асинхронный функционал при выполнении запросов к API.
* `Документация FastAPI`: https://fastapi.tiangolo.com/.
* `Документация Places API`: https://developer.here.com/documentation/geocoding-search-api/dev_guide/topics/endpoint-browse-brief.html.
* `Документация Isoline API`: https://developer.here.com/documentation/isoline-routing-api/dev_guide/index.html.
* `Рекомендуемые библиотеки`: httpx

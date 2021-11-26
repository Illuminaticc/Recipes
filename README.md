# Recipes_project 
Сервис хранения рецептов
### Создайте файл .env.dev и внесите изменения в переменные
## Сборка образа и запуск контейнеров
  ```
  docker-compose up --build
  ```
## Примение миграций
  ```
  python manage.py migrate
  ```
## Загрузка фикстур
  ```
  python manage.py loaddata recipe_data.json
  ```
## Создание суперпользователя
  ```
  python manage.py createsuperuser
  ```

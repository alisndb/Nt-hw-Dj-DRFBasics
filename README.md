### Инструкция по работе:
\
**Собираем образ:** docker build . --tag=smart_home:0.1  
**Запускаем контейнер:** docker run -d -p 8080:8000 smart_home:0.1
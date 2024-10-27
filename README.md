### О чём приложение
Этот проект представляет собой простое веб-приложение на Flask, которое включает в себя регистрацию, авторизацию и защищённые страницы для авторизованных пользователей.
Приложение использует JWT-токены для аутентификации, а база данных SQLite хранит данные пользователей.
  
### Как запустить

Клонирование репозитория:    
'git clone https://github.com/Egrnorm/task_cicd-python-.git'  
Переход в загруженную папку  
cd task_cicd-python-/  
  
Сборка докер-образа:  
sudo docker build -t [название] .  
Где [название] любое удобное название для образа  
Например:  
sudo docker build -t flask_app . 
Запуск контейнера:  
sudo docker run -d -p [порт]:5000 [название] 
Где [порт] любой свободный порт на хосте, [название] название собранного образа  
Например:  
sudo docker run -d -p 1313:5000 flask_app  
По итогу контейнер будет доступен по адресу 127.0.0.1:1313



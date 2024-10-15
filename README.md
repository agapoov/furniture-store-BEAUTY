
# Мой проект - Магазин мебели

Это проект интернет-магазина мебели, разработанный с использованием Django. В данном проекте реализованы основные функции интернет-магазина, включая авторизацию, добавление товаров в корзину, оформление заказов и интеграцию с системой платежей yoomoney. Процент покрытия кода тестами: 87%

## Стек технологий(будет пополняться)

- **Python** - основной язык программирования.
- **Django** - веб-фреймворк для разработки приложения.
- **PostgreSQL** - база данных для разработки.
- **HTML/CSS/JavaScript** - для фронтенд-разметки и стилей.
- **jQuery**: Библиотека JavaScript для упрощения работы с HTML-документами и AJAX.
- **AJAX**: Для асинхронных запросов к серверу.
- **Bootstrap** - фреймворк для создания адаптивного дизайна.
- **YooKassa** - интеграция для обработки платежей.
- **Ngrok** - для создания туннеля и тестирования вебхуков локально.
- **Git** - для управления версиями.
- **Celery** - для асинхронной отправки писем.
- **Unittest** - Для тестирования кода.
## Содержание

- [Требования](#требования)
- [Установка](#установка)
- [Запуск проекта](#запуск-проекта)
- [Функционал](#функционал)
- [Новая функциональность: Вебхуки](#новая-функциональность-вебхуки)
- [Новая функциональность: Синхронная и асинхронная отправка писем](#новая-функциональность-синхронная-и-асинхронная-отправка-писем)

## Требования

Перед тем, как установить проект, убедитесь, что у вас установлены следующие зависимости:

- Python 3.x
- pip
- virtualenv

## Установка

1. Склонируйте репозиторий:

   ```bash
   git clone https://github.com/agapoov/furniture-store-BEAUTY.git
   cd store
   ```

2. Создайте виртуальное окружение:

   ```bash
   python -m venv venv
   ```

3. Активируйте виртуальное окружение:

   - Для Windows:

     ```bash
     venv\Scripts\ctivate
     ```

   - Для MacOS/Linux:

     ```bash
     source venv/bin/activate
     ```

4. Установите зависимости:

   ```bash
   pip install -r requirements.txt
   ```

5. Выполните миграции базы данных:

   ```bash
   python manage.py migrate
   ```

6. Создайте суперпользователя (по желанию):

   ```bash
   python manage.py createsuperuser
   ```

7. Настройте переменные окружения, используя `.env.example`, который содержит все необходимые данные.

## Запуск проекта

Для запуска проекта выполните следующую команду:

```bash
python manage.py runserver
```

Теперь вы можете открыть проект в браузере по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Функционал

В проекте реализованы следующие функции(будут расширяться):

- **Авторизация**: Пользователи могут регистрироваться и входить в систему.
- **Корзина**: Добавление товаров в корзину, удаление товаров.
- **Поиск**: Поиск по названиям товаров, по категориям.
- **Фильтрация**: Фильтрация товаров по различным параметрам.
- **История заказов**: Пользователи могут просматривать свои заказы и их статусы.
- **Система скидок**: Применение скидок к заказам.
- **Система подтверждения почты**: Отправка письма на почту, указанную пользователем.

## Новая функциональность: Вебхуки

В проекте также реализована интеграция с вебхуками yoomoney. При успешной оплате заказа с помощью вебхуков статус заказа обновляется в базе данных. 

Вебхуки позволяют вашему приложению получать уведомления о событиях, происходящих с платежами. Например, когда пользователь успешно оплачивает заказ, ваше приложение получает уведомление, и статус заказа автоматически обновляется на "Оплачено".

### Как это работает:

1. После успешной оплаты пользователем, Яндекс. Деньги отправляет POST запрос на ваш сервер с информацией о платеже.
2. Ваше приложение обрабатывает этот запрос, обновляет статус заказа в базе данных и отправляет ответ на запрос.

## Новая функциональность: Синхронная и асинхронная отправка писем

### Как это работает:

Синхронная отправка:
При регистрации пользователя на его email отправляется письмо с подтверждением, которое обрабатывается сразу после нажатия на кнопку отправки. Это подходит для небольших проектов или на этапе разработки.

Асинхронная отправка с Celery:
Для улучшения производительности отправка писем может быть вынесена в фоновый процесс с использованием Celery. Это снижает нагрузку на основной поток приложения и позволяет обрабатывать запросы пользователей быстрее.

## Заключение

Этот проект является отличной основой для интернет-магазина и может быть расширен новыми функциями по вашему желанию. Если у вас есть вопросы или предложения, обращайтесь.

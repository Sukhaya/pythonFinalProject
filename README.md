# Итоговый проект по автоматизации на Python+Selenium 
Курс https://stepik.org/course/120491/syllabus

В данном проекте реализована работа с интернет-магазином "https://shop.moulinex.ru/"

    Сценарий:
1. Переходим на сайт
2. Авторизация
3. Выбор категории "Миксеры"
4. Выборка фильтров
5. Переход на страницу товара
6. Добавление товара в корзину
7. Переход в корзину
8. Заполнение данных для доставки

Применены: 
  - Selenium
  - ООП
  - Page Object Model 
  - PyTest
  
 В BasePage вынесены getter'ы локаторов для сокращения кода в описании страниц, в этом же классе инициализирован driver
 Запуск теста через terminal при помощи команды "python -m pytest -s -v"
 
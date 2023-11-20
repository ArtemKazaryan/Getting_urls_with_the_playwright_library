
import time
import sqlite3
from math import floor

# Задаём базы данных
db_name = 'parsenews1.db'

# # Строки 12, 13, 14, 15 и 16 НЕ РАСКОММЕНТИРОВЫВАТЬ!!!
# # Импортируем список кортежей для работы с sqlite3 из  resources.py
# from resources import resources
# # Импортируем функцию create_tables_and_add_resources из funcs.py
# from funcs import create_tables_and_add_resources
# create_tables_and_add_resources(db_name, resources)


select = "SELECT * FROM resource WHERE resource_name='Новостной портал nur.kz';"

# Запуск парсинг-таймера
start_time = time.time()

# Связываемся с БД и производим выполнение выбранной команды
conn = sqlite3.connect(db_name)
cur = conn.cursor()
cur.execute(select)
result = cur.fetchone()
res = list(result)

# Производим передачу и распаковку данных из таблицы resource
# ДЛЯ НАГЛЯДНОСТИ переопределяем переменные
resource_id = res[0]
resource_url_args = res[2].split(', ')
depth_config = resource_url_args[1].split(', ')
depth_mode = depth_config[0].split(' ')

top_tag_args = res[3].split(', ')
bottom_tag_args = res[4].split(', ')
title_cut_args = res[5].split(', ')
date_cut_args = res[6].split(', ')

level_depth, load_pause = int(depth_mode[1]) - 1, float(depth_mode[2])
menu_url, div1_tag_class, div1_tag, a_tag_class, a_tag = resource_url_args[0], top_tag_args[0], top_tag_args[1], top_tag_args[2], top_tag_args[3]

print(f'')
print('Запуск осуществлён.')
print('Подождите...')
print(f'')

from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

# Перемещение в конец страницы с целью дозагрузки на ней списка новостей с помощью playwright
with sync_playwright() as playwright:
    # browser = playwright.chromium.launch(headless=False) # С визуализацией работы движка
    browser = playwright.chromium.launch(headless=True)  # Без визуализации работы движка
    context = browser.new_context()
    page = context.new_page()
    page.goto(menu_url)
    for i in range(level_depth):
        page.keyboard.press('End') # Перемещение в конец страницы level_depth раз
        time.sleep(load_pause) # С паузой между перемещениями load_pause секунд
    # time.sleep(1) # Для задержки (использовать необязательно)
    html = page.content()
    soup = BeautifulSoup(html, "html.parser")
    links0 = soup.find_all(div1_tag, class_=div1_tag_class)
    links = []
    for link0 in links0:
        links1 = link0.find_all(a_tag, class_=a_tag_class)
        for link1 in links1:
            links.insert(0, link1["href"])

print('Ссылки получены')
print(f'')
print(f'Список ссылок: {links}')
print(f'Количество ссылок: {len(links)}')

end_time = time.time()
print(f'ДЛИТЕЛЬНОСТЬ ПОЛУЧЕНИЯ ССЫЛОК: {round(end_time - start_time, 2)} СЕКУНД')





# from funcs import add_to_items
# from dateparser import parse
# import requests

# for link in links:
#     # Получаем ссылку как атрибут объекта response, переданную  в генераторе функции parse
#     site_link = link
#     response = requests.get(site_link)
#     if response.status_code == 200:
#         soup = BeautifulSoup(response.content, "html.parser")
#         # Получение удобочитаемых переменных
#         h1_tag_class, h1_tag = title_cut_args[0], title_cut_args[1]
#         # Проверка на пустые поля для корректной работы механизма xpath
#         if h1_tag_class != '':
#             title = soup.find(h1_tag, class_=h1_tag_class).text.strip()
#
#         # Получение удобочитаемых переменных
#         div2_tag_class, div2_tag = bottom_tag_args[0], bottom_tag_args[1]
#         # Проверка на пустые поля для корректной работы механизма xpath
#         if div2_tag_class != '':
#             content = soup.find(div2_tag, class_=div2_tag_class).text.strip()
#
#         # Получение переменной css-селектора для получения даты и времени новости
#         date_arg = date_cut_args[1]
#         date_time = soup.find(date_cut_args[1]).get('datetime')
#         from dateparser import parse
#         date = parse(date_time)
#         nd_date = int(time.mktime(date.timetuple()))
#         not_date = date.strftime('%d-%m-%Y')
#
#         # Получение времени внесения данных в БД
#         s_date = floor(time.time())
#         # Вызов функции добавления данных новости в таблицу items БД
#         add_to_items(db_name, resource_id, link, title, content, nd_date, s_date, not_date)
#
# # Остановка парсинг-таймера
# end_time = time.time()
# print(f'ОБЩАЯ ДЛИТЕЛЬНОСТЬ ПАРСИНГА: {round(end_time - start_time, 2)} СЕКУНД')










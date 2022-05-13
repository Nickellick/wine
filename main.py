import datetime
from collections import defaultdict

from http.server import HTTPServer, SimpleHTTPRequestHandler

from jinja2 import Environment, FileSystemLoader, select_autoescape

import pandas

excel_data_df = pandas.read_excel('wine3.xlsx',
                                  na_values='',
                                  keep_default_na=False)
wine_dict = excel_data_df.transpose().to_dict()

categories = defaultdict(list)

for value in wine_dict.values():
    category = value['Категория']
    wine = {}
    wine['name'] = value['Название']
    wine['variety'] = value['Сорт']
    wine['price'] = value['Цена']
    wine['image'] = value['Картинка']
    wine['category'] = category
    wine['profitable'] = value['Акция'] == 'Выгодное предложение'
    categories[category].append(wine)


env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')

rendered_page = template.render(since_years=f'{datetime.datetime.now().year - 1920}',
                                categories=categories)

with open('index.html', 'w', encoding='utf8') as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()

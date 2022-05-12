import datetime

from http.server import HTTPServer, SimpleHTTPRequestHandler

from jinja2 import Environment, FileSystemLoader, select_autoescape

import pandas

excel_data_df = pandas.read_excel('wine.xlsx')
wine_dict = excel_data_df.transpose().to_dict()
print(wine_dict)

wines = []

for value in wine_dict.values():
    wine = {}
    wine['name'] = value['Название']
    wine['variety'] = value['Сорт']
    wine['price'] = value['Цена']
    wine['image'] = value['Картинка']
    wines.append(wine)


env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')

rendered_page = template.render(since_years=f'{datetime.datetime.now().year - 1920}', wines=wines)

with open('index.html', 'w', encoding='utf8') as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()

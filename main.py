import datetime

from http.server import HTTPServer, SimpleHTTPRequestHandler

from jinja2 import Environment, FileSystemLoader, select_autoescape

import pandas

excel_data_df = pandas.read_excel('wine.xlsx')
print(excel_data_df.to_dict())

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')

rendered_page = template.render(since_years=f'{datetime.datetime.now().year - 1920}')

with open('index.html', 'w', encoding='utf8') as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()

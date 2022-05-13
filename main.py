from argparse import ArgumentParser
import datetime
from collections import defaultdict
from http.server import HTTPServer, SimpleHTTPRequestHandler
import os
from unittest.mock import DEFAULT

from dotenv import load_dotenv
from jinja2 import Environment, FileSystemLoader, select_autoescape
import pandas

def main():

    DEFAULT_FILE_PATH = 'wine.xlsx'

    ESTABLISHMENT_YEAR = 1920

    # Parsing arguments from env
    load_dotenv('.env')
    path_to_file = os.getenv(key='DVMN_WINEDATA', default=DEFAULT_FILE_PATH)
    if path_to_file is None:
        # Parsing arguments from cli
        parser = ArgumentParser(
            description='This is example of wineshop website presented by dvmn.org'
        )
        parser.add_argument(
            '--winedata',
            type=str,
            help=f'path to file with wine data. Default is {DEFAULT_FILE_PATH}. See README.MD for more info',
            default=DEFAULT_FILE_PATH
            )

        
        args = parser.parse_args()

        path_to_file = args.winedata

    excel_data_df = pandas.read_excel(
        path_to_file,
        na_values='',
        keep_default_na=False
        )
    wine_dict = excel_data_df.transpose().to_dict()

    wines = defaultdict(list)

    for value in wine_dict.values():
        category = value['Категория']
        wine = {}
        wine['name'] = value['Название']
        wine['variety'] = value['Сорт']
        wine['price'] = value['Цена']
        wine['image'] = value['Картинка']
        wine['category'] = category
        wine['profitable'] = value['Акция'] == 'Выгодное предложение'
        wines[category].append(wine)


    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')

    rendered_page = template.render(
        since_years=f'{datetime.datetime.now().year - ESTABLISHMENT_YEAR}',
        wines=wines
        )

    with open('index.html', 'w', encoding='utf8') as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()

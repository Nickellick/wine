from argparse import ArgumentParser
from collections import defaultdict
import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler

from jinja2 import Environment, FileSystemLoader, select_autoescape
import pandas

ESTABLISHMENT_YEAR = 1920


def main():

    winetable_path = 'wine.xlsx'

    parser = ArgumentParser(
        description='This is example of wineshop website presented by dvmn.org'
    )
    parser.add_argument(
        '--winetable',
        type=str,
        help=f'path to file with wine data. Default is {winetable_path}. See README.MD for more info',
        default=winetable_path
        )

    
    args = parser.parse_args()

    path_to_file = args.winetable

    excel_data_df = pandas.read_excel(
        path_to_file,
        na_values='',
        keep_default_na=False
        ).transpose().to_dict()

    categories = defaultdict(list)

    for wine in excel_data_df.values():
        category = wine['Категория']
        categories[category].append(wine)


    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')

    rendered_page = template.render(
        since_years=datetime.datetime.now().year - ESTABLISHMENT_YEAR,
        categories=categories
        )

    with open('index.html', 'w', encoding='utf8') as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()

import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler
from collections import defaultdict
import os
from jinja2 import Environment, FileSystemLoader, select_autoescape
from pandas import read_excel
from dotenv import load_dotenv

def get_year_notation(year):
    last_char, pre_last_char = list(year)[-1], list(year)[-2]
    year_notation = 'лет'
    is_tens = pre_last_char == '1'
    if last_char == '1' and not is_tens:
        year_notation = 'год'
    if last_char in ['2', '3', '4'] and not is_tens:
        year_notation = 'года'
    return year_notation


def main():
    load_dotenv()
    foundation_year = int(os.getenv('FOUNDATION_YEAR'))
    now = datetime.datetime.now()
    company_age = str(now.year - foundation_year)
    year_notation = get_year_notation(company_age)
    categorised_drinks = read_excel(
        io=os.getenv('PATH_TO_XLSX_DB'),
        sheet_name=os.getenv('SHEET'),
        keep_default_na=False
    )
    drinks = categorised_drinks.to_dict(orient='record')
    drinks_by_categories = defaultdict(list)
    for drink in drinks:
        drink_category = drink['Категория']
        drinks_by_categories[drink_category].append(drink)
        drink.pop('Категория')

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')
    rendered_page = template.render(
        company_age=company_age,
        year_notation=year_notation,
        drinks_by_categories=drinks_by_categories
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()

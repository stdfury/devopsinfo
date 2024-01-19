import requests
from datetime import datetime, timedelta
from bs4 import BeautifulSoup

currency_to_rub = {
    "AZN": 35.68,
    "BYR": 23.91,
    "EUR": 59.90,
    "GEL": 21.74,
    "KGS": 0.76,
    "KZT": 0.13,
    "RUR": 1,
    "UAH": 1.64,
    "USD": 60.66,
    "UZS": 0.0055,
}


def process_salary(salary):
    if not salary:
        return 'Не указана'

    currency = salary['currency']
    if currency in currency_to_rub:
        rate = currency_to_rub[currency]
    else:
        rate = 1

    salary_from = salary['from'] * rate if salary['from'] else 0
    salary_to = salary['to'] * rate if salary['to'] else 0

    if salary_from and salary_to:
        return f"{(salary_from + salary_to) / 2} руб."
    return f"{salary_from} руб." if salary_from else f"{salary_to} руб."


def clean_string(raw_string):
    soup = BeautifulSoup(raw_string, "html.parser")
    clean_text = soup.get_text().strip()
    return clean_text[:600] + '...' if len(clean_text) > 250 else clean_text


def second_request(vacancy_id):
    url = f'https://api.hh.ru/vacancies/{vacancy_id}'
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def get_vacancies():
    keywords = ['devops', 'development operations']
    date_from = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')

    url = 'https://api.hh.ru/vacancies'

    params = {
        'text': 'NAME:(' + ' OR '.join(keywords) + ') AND (IT)',
        'date_from': date_from,
        'date_to': date_from,
        'per_page': 10
    }

    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()

    vacancies = []
    for item in data['items']:
        detailed_info = second_request(item['id'])

        vacancy = {
            'name': item['name'],
            'desc': clean_string(detailed_info['description']),
            'skills': ', '.join([skill['name'] for skill in detailed_info.get('key_skills', [])]),
            'company': item['employer']['name'],
            'salary': process_salary(item['salary']),
            'region': item['area']['name'],
            'date': item['published_at'].replace("T", " ")[:-5]
        }
        vacancies.append(vacancy)

    return vacancies

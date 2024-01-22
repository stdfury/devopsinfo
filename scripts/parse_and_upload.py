import csv
import datetime
import re
import graphs
from devopsinfo_api import upload_item

keywords = ['devops', 'development operations']

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


def clean_line(string):
    return ' '.join(re.sub(r'<.*?>', '', string).split())


class Salary:
    def __init__(self, data):
        self.sal_cur = data['salary_currency']
        self.sal_from = data['salary_from']
        self.sal_to = data['salary_to']

    def get_avg_salary(self):
        return currency_to_rub[self.sal_cur] * int((float(self.sal_to) + float(self.sal_from)) / 2)


class Vacancy:
    def __init__(self, data):
        self.name = data['name']
        self.sal = Salary(data)
        self.publ_at = data['published_at']
        self.area_name = data['area_name']


class DataSet:
    def __init__(self, input_connector):
        self.__inp = input_connector
        self.years = set()
        self.vacs = self.read_csv(input_connector.f_name)
        self.vacs_by_area = self.get_vacs_by_area()
        self.vacs_by_year = self.get_vacs_by_year()

    @classmethod
    def read_csv(cls, f_name):
        with open(f_name, 'r', encoding='utf-8-sig') as file:
            res = []
            reader = list(x for x in csv.reader(file) if '' not in x)
            keys = reader.pop(0)
            for vac in reader:
                vac_data = {}
                for i, elem in enumerate(vac):
                    vac_data[keys[i]] = clean_line(elem)
                res.append(Vacancy(vac_data))
            return res

    def get_vacs_by_year(self):
        res = {}
        for vac in sorted(self.vacs, key=lambda x: x.publ_at, reverse=False):
            year = datetime.datetime.strptime(vac.publ_at, '%Y-%m-%dT%H:%M:%S%z').year
            self.years.add(year)
            if year in res.keys():
                res[year].append(vac)
            else:
                res[year] = [vac]
        return res

    def select_vacancies(self):
        result = []
        for i in self.vacs:
            flag = False
            for keyword in keywords:
                if keyword.lower() in i.name.lower():
                    flag = True
            if flag:
                result.append(i)

        self.vacs = result
        self.vacs_by_year = self.get_vacs_by_year()

    def get_total_vacs_by_year(self):
        res = {k: len(v) for k, v in self.vacs_by_year.items()}
        return res if len(res) > 0 else {k: 0 for k in sorted(self.years)}

    def get_sals_by_year(self):
        res = {k: int(sum(vac.sal.get_avg_salary() for vac in v) / len(v)) for k, v in
               self.vacs_by_year.items()}
        return res if len(res) > 0 else {k: 0 for k in sorted(self.years)}

    def get_vacs_by_area(self):
        result = {}
        for vac in self.vacs:
            area = vac.area_name
            if area not in result.keys():
                result[area] = [vac]
            else:
                result[area].append(vac)
        return {k: v for k, v in result.items() if len(v) / len(self.vacs) >= 0.01}

    def get_rate_by_area(self, trunc):
        return {k: round(len(v) / len(self.vacs), 4) for k, v in
                sorted(self.vacs_by_area.items(), key=lambda item: len(item[1]), reverse=True)[:trunc]}

    def get_sals_by_area(self, trunc):
        sals = {k: int(sum(vac.sal.get_avg_salary() for vac in v) / len(v)) for k, v in
                self.vacs_by_area.items()}
        return {k: v for k, v in sorted(sals.items(), key=lambda item: item[1], reverse=True)[:trunc]}


class InputConnector:
    def __init__(self):
        self.f_name = input('Введите название файла: ')
        self.prof_name = "popa"

    @staticmethod
    def print_data(text, data):
        print(f'{text}: {data}\n')


def main():
    inp_con = InputConnector()
    dta_set = DataSet(inp_con)
    sals_by_year = dta_set.get_sals_by_year()
    total_vacs_by_year = dta_set.get_total_vacs_by_year()
    rate_by_area = dta_set.get_rate_by_area(10)
    sals_by_area = dta_set.get_sals_by_area(5)
    dta_set.select_vacancies()
    dta_set.vacs_by_area = dta_set.get_vacs_by_area()
    prof_sals_by_year = dta_set.get_sals_by_year()
    prof_total_vacs_by_year = dta_set.get_total_vacs_by_year()
    prof_sals_by_area = dta_set.get_sals_by_area(5)
    prof_rate_by_area = dta_set.get_rate_by_area(10)

    print("\nСтраница Востребованность\n")

    InputConnector.print_data(
        "Динамика уровня зарплат по годам",
        sals_by_year
    )
    for k, v in sals_by_year.items():
        data = {"year": k, "salary": v}
        upload_item(data, url_prefix='demand/average-salary/')
    graphs.default(sals_by_year, "demand_1")

    InputConnector.print_data(
        "Динамика количества вакансий по годам",
        total_vacs_by_year
    )
    for k, v in total_vacs_by_year.items():
        data = {"year": k, "vacancy_amount": v}
        upload_item(data, url_prefix='demand/average-amount/')
    graphs.default(total_vacs_by_year, "demand_2")

    InputConnector.print_data(
        "Динамика уровня зарплат по годам для выбранной профессии",
        prof_sals_by_year
    )
    for k, v in prof_sals_by_year.items():
        data = {"year": k, "salary": v}
        upload_item(data, url_prefix='demand/devops-salary/')
    graphs.default(prof_sals_by_year, "demand_3")

    InputConnector.print_data(
        "Динамика количества вакансий по годам для выбранной профессии",
        prof_total_vacs_by_year
    )
    for k, v in prof_total_vacs_by_year.items():
        data = {"year": k, "vacancy_amount": v}
        upload_item(data, url_prefix='demand/devops-amount/')
    graphs.default(prof_total_vacs_by_year, "demand_4")


    print("\nСтраница География\n")

    InputConnector.print_data(
        "Уровень зарплат по городам (в порядке убывания)",
        sals_by_area
    )
    for k, v in sals_by_area.items():
        data = {"city": k, "salary": v}
        upload_item(data, url_prefix='geography/salary/')
    graphs.default(sals_by_area, "geography_1")

    InputConnector.print_data(
        "Доля вакансий по городам (в порядке убывания)",
        rate_by_area
    )
    for k, v in rate_by_area.items():
        data = {"city": k, "rate": v}
        upload_item(data, url_prefix='geography/rating/')
    graphs.pie(rate_by_area, "geography_2")

    InputConnector.print_data(
        "Уровень зарплат по городам для выбранной профессии (в порядке убывания)",
        prof_sals_by_area
    )
    for k, v in prof_sals_by_area.items():
        data = {"city": k, "salary": v}
        upload_item(data, url_prefix='geography/devops-salary/')
    graphs.default(prof_sals_by_area, "geography_3")

    InputConnector.print_data(
        "Доля вакансий по городам для выбранной профессии (в порядке убывания)",
        prof_rate_by_area
    )
    for k, v in prof_rate_by_area.items():
        data = {"city": k, "rate": v}
        upload_item(data, url_prefix='geography/devops-rating/')
    graphs.pie(prof_rate_by_area, "geography_4")



if __name__ == '__main__':
    main()


import matplotlib.pyplot as plt
import re

def default(data_str, filename):
    data_dict = data_str

    years = list(data_dict.keys())
    vacancy_amount = list(data_dict.values())

    plt.figure(figsize=(8, 4), facecolor='skyblue')
    plt.bar(years, vacancy_amount)
    plt.xticks(years, color='#f8f8f2')
    plt.yticks(color='#f8f8f2')
    plt.gca().spines['bottom'].set_color('#f8f8f2')
    plt.gca().spines['left'].set_color('#f8f8f2')
    plt.gca().spines['top'].set_color('#f8f8f2')
    plt.gca().spines['right'].set_color('#f8f8f2')
    plt.grid(axis='y', color='#f8f8f2')

    file_path = f'./{filename}.png'
    plt.savefig(file_path, transparent=True, bbox_inches='tight')

    plt.close()


def pie(data_str, filename):

    vacancy_data_dict = data_str

    if list(vacancy_data_dict.values())[0] > 1:
        total = 100
    else: total = 1

    total_share = sum(vacancy_data_dict.values())
    other_share = total - total_share

    vacancy_data_dict["Другие"] = other_share

    cities = list(vacancy_data_dict.keys())
    shares = list(vacancy_data_dict.values())

    plt.figure(figsize=(8, 8), facecolor='skyblue')
    patches, texts, autotexts = plt.pie(shares, labels=cities, autopct='%1.1f%%', startangle=140, colors=plt.cm.tab20.colors)

    for text in texts:
        text.set_color('#f8f8f2')


    file_path = f'{filename}.png'
    plt.savefig(file_path, transparent=True, bbox_inches='tight', facecolor='none')

    plt.close()
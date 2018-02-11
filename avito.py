import requests
from bs4 import BeatifulSoup


def get_html(url):
    r = requests.get(url)
    return r.text

def get_total_pages(html):
    soup = BeatifulSoup(html, 'lxml')
    pages = soup.find('div', class_='pagintaion-class').find_all('a', class_="pagintaion-page")[-1].get('href')
    total_pages = pages.split('=')[1].split('&')[0]
    return int(total_pages)

def get_page_data(html):
    soup = BeatifulSoup(html, 'lxml')
    ads = soup.find('div', class_='catalog_list').find_all('div', class_='item_table')

    for ad in ads:
        


def main():
    url = 'https://www.avito.ru/moskva/telefony/htc?p=2&q=htc'
    base_url = 'https://www.avito.ru/moskva/telefony?'
    page_part = 'p='
    query_part = '&q=htc'
    total_pages = get_total_pages(get_html(url))

    for i in range(1, total_pages):
        url_gen = base_url + page_part + str(i) + query_part
        # print(url_gen)
        html = get_html(url_gen)
        get_page_data(html)
    

if __name__ == '__main__':
    main()
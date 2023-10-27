import time
import requests
from bs4 import BeautifulSoup

def get_product_info(query, attempt=0):
    if attempt >= 3:
        print("Błąd , podaj inną nazwę")
        return "Brak nazwy", "Brak oceny", "Brak ceny"
    ans = query.replace(" ", "+")
    url = f'https://www.amazon.pl/s?k={ans}'
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        item = soup.select('div.a-section.a-spacing-base')[0]
        rating_element = item.select('span.a-icon-alt')
        if rating_element:
            rating = rating_element[0].text
        else:
            rating = "Brak oceny"
        name_element = item.select('h2.a-size-mini.a-spacing-none.a-color-base.s-line-clamp-4')
        if name_element:
            name = name_element[0].text
        else:
            name = "Brak nazwy"
        price_element = item.select('span.a-price span.a-offscreen')
        if price_element:
            price = price_element[0].get_text()
        else:
            price = "Brak ceny"
        return name, rating, price
    except:
        print("Błąd. Ponowna próba wyszukania produktu")
        time.sleep(5)
        return get_product_info(query, attempt + 1)

def main():
    query = input("Jaki produkt chcesz wyszukać? :")
    name, rating, price = get_product_info(query)
    print('Nazwa produktu:', name)
    print('Cena produktu:', price)
    print('Ocena produktu:', rating)

    input("Wciśnij enter aby zakończyć...")

main()

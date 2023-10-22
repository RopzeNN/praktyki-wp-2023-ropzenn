import time
import requests
from bs4 import BeautifulSoup


def informacje_o_produkcie(query):
    ans = query.replace(" ", "+")
    url = f'https://www.amazon.pl/s?k={ans}'
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        przedmiot = soup.select('div.a-section.a-spacing-base')[0]
        rating_element = przedmiot.select('span.a-icon-alt')
      
        if rating_element:
            rating = rating_element[0].text
        else:
            rating = "Brak oceny"
            nazwa_produktu = przedmiot.select('h2.a-size-mini.a-spacing-none.a-color-base.s-line-clamp-4')
          
        if nazwa_produktu:
            nazwa = nazwa_produktu[0].text
        else:
            nazwa = "Brak nazwy"
        price_element = przedmiot.select('span.a-price span.a-offscreen')
      
        if price_element:
            price = price_element[0].get_text()
        else:
            price = "Brak ceny"
        return nazwa, rating, price
      
    except:
        print("Nie udało się znaleźć produktu")
        time.sleep(5)
        return informacje_o_produkcie(query)


def main():
    query = input("Podaj nazwę produktu: ")
    nazwa, rating, ocena = informacje_o_produkcie(query)
    print('Nazwa produktu:', name)
    print('Cena produktu:', price)
    print('Ocena produktu:', rating)

    input("Press Enter to continue...")


main()

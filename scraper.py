import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Scraper:
    results = []

    def StartScraper():
        user_agent = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
                              (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}

        all_products = []
        possible_sizes = ['34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44']

        size = '35'
        product = 'Tênis Converse Amarelo'
        if size not in possible_sizes:
            print('Esse tamanho não é possível de encontrar. \nVerifique ortografia ou tente tamanho entre 34 ao 44')
            return StartScraper()
        else:
            pass

        def Dafiti():
            dafiti = f'https://www.dafiti.com.br/tamanho-{size}/?sort=price&q={product}&wtqs=1'
            conteudo = requests.get(dafiti, headers=user_agent)
            soup = BeautifulSoup(conteudo.content, 'html.parser')
            products = soup.find_all('div', {'data-store': '1'})
            for info in products:
                image = info.find('img', class_="product-image")['data-original']
                name = info.find('img', class_="product-image")['alt']
                link = info.find(class_="product-box-link is-lazyloaded image product-image-rotate")['href']
                price = info.find(class_="product-box-price-from").text.strip().replace(" ", "")
                if len(price) < 8:
                    price_list = list(price)
                    price_list.insert(2, '0')
                    price = ''.join(price_list)
                else:
                    pass

                dafiti_products = {
                    'Image': image,
                    'Name': name,
                    'Price': price,
                    'Link': link,
                }

                all_products.append(dafiti_products)

        Dafiti()

        def Kanui():
            kanui = f'https://www.kanui.com.br/all-products/tamanho-{size}/?sort=price&q={product}&wtqs=1'
            conteudo = requests.get(kanui, headers=user_agent)
            soup = BeautifulSoup(conteudo.content, 'html.parser')
            products = soup.find_all('div', {'data-store': '1'})

            for info in products:
                image = info.find('img', class_="product-image")['data-original']
                name = info.find('img', class_="product-image")['alt']
                link = info.find(class_="product-box-link is-lazyloaded image product-image-rotate")['href']
                price = info.find(class_="product-box-price-from").text.strip().replace(" ", "")
                if len(price) < 8:
                    price_list = list(price)
                    price_list.insert(2, '0')
                    price = ''.join(price_list)
                else:
                    pass

                kanui_products = {
                    'Image': image,
                    'Name': name,
                    'Price': price,
                    'Link': link,
                }
                all_products.append(kanui_products)

        Kanui()

        def Shop2Gether():

            size_list = ['34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44']
            filter_list = ['19', '20', '21', '22', '23', '06', '07', '08', '09', '10', '11']

            real_size = size_list.index(size)
            shop2gether = f'https://www.shop2gether.com.br/catalogsearch/result/index/?cat=0&dir=asc&order=price&q={product}&sapato_tamanho_filtro=45{filter_list[real_size]}'
            conteudo = requests.get(shop2gether, headers=user_agent)
            soup = BeautifulSoup(conteudo.content, 'html.parser')
            products = soup.find_all('li', {"class": "item"})

            for info in products:
                image = info.find(class_="lazy")['data-src']
                name = info.find(class_="lazy")['title']
                link = info.find(class_="product-image")['href']
                try:
                    price = info.find('span', class_="price", id=False).text.strip()
                    if len(price) < 8:
                        price_list = list(price)
                        price_list.insert(2, '0')
                        price = ''.join(price_list)
                    else:
                        pass
                except:
                    price = info.find(class_="special-price").contents[3].text.strip()
                    if len(price) < 8:
                        price_list = list(price)
                        price_list.insert(2, '0')
                        price = ''.join(price_list)
                    else:
                        pass

                shop2gether_products = {
                    'Image': image,
                    'Name': name,
                    'Price': price,
                    'Link': link,
                }
                all_products.append(shop2gether_products)

        Shop2Gether()

        def Oqvestir():
            size_list = ['34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44']
            filter_list = ['907', '905', '965', '967', '969', '971', '973', '975', '977', '979', '981']

            real_size = size_list.index(size)
            oqvestir = f'https://www.oqvestir.com.br/catalogsearch/result/index/?dir=asc&limit=90&order=price&q={product}&sapato_tamanho={filter_list[real_size]}'
            conteudo = requests.get(oqvestir, headers=user_agent)
            soup = BeautifulSoup(conteudo.content, 'html.parser')

            products = soup.find_all('li', {'class': 'item'})

            for info in products:
                try:
                    image = info.find('img', alt=True)['data-srcset']
                    name = info.find(class_="product-image")['title']
                    link = info.find(class_="product-image")['href']
                    try:
                        price = info.find(class_="special-price").text.strip()
                        if len(price) < 8:
                            price_list = list(price)
                            price_list.insert(2, '0')
                            price = ''.join(price_list)
                    except:
                        pass

                    try:
                        price = info.find(class_="price", id=False).text.strip()
                        if len(price) < 8:
                            price_list = list(price)
                            price_list.insert(2, '0')
                            price = ''.join(price_list)
                    except:
                        pass

                    oqvestir_products = {
                        'Image': image,
                        'Name': name,
                        'Price': price,
                        'Link': link,
                    }
                    all_products.append(oqvestir_products)

                except:
                    pass

        Oqvestir()

        def Zattini():
            zattini = f'https://www.zattini.com.br/busca?nsCat=Natural&q={product}&tamanho={size}'
            conteudo = requests.get(zattini, headers=user_agent)
            soup = BeautifulSoup(conteudo.content, 'html.parser')
            link_list = soup.find_all('a', {'parent-sku': True})
            all_links = []
            for link in link_list:
                all_links.append('https:' + link['href'])

            for links in all_links:
                conteudo = requests.get(links, headers=user_agent)
                soup = BeautifulSoup(conteudo.content, 'html.parser')
                image = soup.find('img', class_="zoom")['src']
                link = soup.find('link', {'href': True})['href']
                name = soup.find('h1', {'data-productname': True}).text.strip()
                price = soup.find(class_="default-price").text.strip().replace('A partir de', '').replace(" ", "")
                if len(price) < 8:
                    price_list = list(price)
                    price_list.insert(2, '0')
                    price = ''.join(price_list)

                zattini_products = {
                    'Image': image,
                    'Name': name,
                    'Price': price,
                    'Link': link,
                }
                all_products.append(zattini_products)

        Zattini()

        def StudioZ():
            options = Options()
            options.add_argument("--headless")
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
            start_url = f'https://www.stz.com.br/#searchSort=1&search-term={product}'
            driver.get(start_url)
            page_source = driver.page_source
            driver.quit()
            soup = BeautifulSoup(page_source, 'html.parser')
            products = soup.find_all(class_="apoio-sh", style=False)
            words = "Encontramos produtos"

            if words not in soup.text:
                for info in products:
                    image = info.find('img')['src']
                    name = info.find('h2', itemprop="name").text.strip()
                    link = 'https:' + info.find('a', class_="p-1")['href']
                    price = info.find(class_="price-sale").text.strip().replace(" ", "")
                    if len(price) < 8:
                        price_list = list(price)
                        price_list.insert(2, '0')
                        price = ''.join(price_list)
                    else:
                        pass

                    studioz_products = {
                        'Image': image,
                        'Name': name,
                        'Price': price,
                        'Link': link,
                    }

                    all_products.append(studioz_products)
            else:
                pass

        StudioZ()

        def Netshoes():
            netshoes = f'https://www.netshoes.com.br/busca?nsCat=Natural&q={product}&searchTermCapitalized={product}&sort=lowest-first&tamanho={size}'
            conteudo = requests.get(netshoes, headers=user_agent)
            soup = BeautifulSoup(conteudo.content, 'html.parser')
            link_list = soup.find_all('a', {'parent-sku': True})
            all_links = []
            for link in link_list:
                all_links.append('https:' + link['href'])

            for links in all_links:
                conteudo = requests.get(links, headers=user_agent)
                soup = BeautifulSoup(conteudo.content, 'html.parser')
                image = soup.find('img', class_="zoom")['src']
                link = soup.find('link', {'href': True})['href']
                name = soup.find('h1', {'data-productname': True}).text.strip()
                price = soup.find(class_="default-price").text.replace(' ', '').replace('Apartirde', '')
                if len(price) < 8:
                    price_list = list(price)
                    price_list.insert(2, '0')
                    price = ''.join(price_list)
                else:
                    pass

                netshoes_products = {
                    'Image': image,
                    'Name': name,
                    'Price': price,
                    'Link': link,
                }
                all_products.append(netshoes_products)

        Netshoes()

        def Centauro():
            options = Options()
            options.add_argument("--headless")
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
            start_url = f'https://www.centauro.com.br/busca?q={product}&common_filter%5BTamanho%5D={size}'
            driver.get(start_url)
            page_source = driver.page_source
            driver.quit()
            soup = BeautifulSoup(page_source, 'html.parser')
            products = soup.find_all('div', class_="_sv7ou2 product-card")

            for info in products:
                image = 'https://www.centauro.com.br' + info.find('img', class_="_j96s06")['src']
                name = info.find('img', class_="_j96s06")['alt']
                link = 'https:' + info.find('a', class_="_13xlah4")['href']
                price = info.find('span', class_="_9pmwio").text.strip().replace(" ", "")
                if len(price) < 8:
                    price_list = list(price)
                    price_list.insert(2, '0')
                    price = ''.join(price_list)

                else:
                    pass

                centauro_products = {
                    'Image': image,
                    'Name': name,
                    'Price': price,
                    'Link': link,
                }

                all_products.append(centauro_products)

        Centauro()

        def OrganizeData():
            df = pd.DataFrame(all_products)

            if not df.empty:
                results = df.sort_values(by='Price', ascending=True)
                results.to_csv()

            else:
                print(f'Nenhum resultado para {product}.\nTente verificar a ortografia ou usar termos mais genéricos!')
                return Scraper

        OrganizeData()


if __name__ == '__main__':
    scraper = Scraper()
    scraper.run()

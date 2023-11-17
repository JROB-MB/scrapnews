# import requests
# from bs4 import BeautifulSoup

# url = ''

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
# }


# response = requests.get(url, headers=headers)

# if response.status_code == 200:
#     html_content = response.content
#     soup = BeautifulSoup(html_content, 'html.parser')

#     # Encontrar todos los elementos 'article'
#     articles = soup.find_all('article')

#     for article in articles:
#         # Imprimir el texto del artículo o realizar otras operaciones aquí
#         print(article.get_text())
# else:
#     print('La solicitud GET no fue exitosa')
import requests
from bs4 import BeautifulSoup

url = ''

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')

    articles = soup.find_all('article')

    # Crear un archivo de texto para guardar el contenido
    with open('contenido_extraido.txt', 'w', encoding='utf-8') as file:
        for article in articles:
            # Escribir el texto del artículo en el archivo
            file.write(article.get_text() + '\n')
    
    print('Contenido extraído y guardado en contenido_extraido.txt')
else:
    print('La solicitud GET no fue exitosa')

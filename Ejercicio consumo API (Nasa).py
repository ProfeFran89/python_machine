import requests
import json
from string import Template

def build_web_page(lista_imagenes):
    html_template = Template('''<html>
                            <head>
                            </head>
                            <body>
                            <ul>
                            <li>$imagenes</li>
                            </ul>
                            </body>
                            </head>
                            </html>''')

    imagenes_url = ''

    for url_ in lista_imagenes:
        imagenes_url+= url_+'\n'
    
    html = html_template.substitute(imagenes = imagenes_url)

    with open('nasa.html', 'w') as f:
        f.write(html)

url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/latest_photos?api_key=ZL1DfZQzdr7LrhwSkiSYDFu7dMP8zoEr4J2guueL"

response = json.loads(requests.get(url).text)
data = response.get('latest_photos')[:25]

lista_src = []
for elemento in data:
    for k,v in elemento.items():
        if k == 'img_src':
            lista_src.append(f'<img src="{v}"/>')

build_web_page(lista_src)
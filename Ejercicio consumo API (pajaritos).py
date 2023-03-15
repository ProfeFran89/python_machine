import requests
import json
from string import Template

def build_web_page(lista_nombres, lista_names, lista_imagenes):
    html_template = Template('''<html>
                            <head><h1> SITIO WEB DE AVES
                            </h1></head>
                            <body>
                            <ul>
                            <li>$informacion</li>
                            </ul>
                            </body>
                            </head>
                            </html>''')

    informacion_ = ''
    for nombre, name, imagen in zip(lista_nombres, lista_names, lista_imagenes):
        informacion_ += ("</h4>Spanish: "+nombre+" English: "+name+"</h4><img src="+imagen+"><br/>")
    
    html = html_template.substitute(informacion = informacion_)
        
    #Creación del sitio web
    with open('pajaritos.html', 'w') as f:
        f.write(html)
    return ''

#Consumir API
url = 'https://aves.ninjas.cl/api/birds'
response = json.loads(requests.get(url).text)
imagenes_ = []
nombres_ = []
names_ = []

#Creación de lista con imágenes
for item in response[:25]:
    for k, v in item.items():
        if k == "images":
            imagenes_.append(v['main'])

#Creación de lista con nombres
for item in response[:25]:
    for k, v in item.items():
        if k == "name":
            nombres_.append(v['spanish'])

#Creación de lista con names
for item in response[:25]:
    for k, v in item.items():
        if k == "name":
            names_.append(v['english'])

build_web_page(nombres_,names_,imagenes_)
import requests

# Links to csv files
url_contador = 'https://datos.cdmx.gob.mx/dataset/07d5d501-66dc-4e3e-9d92-bfa163d21434/resource/8548607a-b0c0-4210-962e-1240f715b680/download/ciclista_nuevo.csv'
url_incidentes = ''

# Get data from the website
get_contador = requests.get(f'{url_contador}')
print(get_contador)

# Read content
content_contador = get_contador.content

# Create csv files
with open('contador-ciclistas.csv', 'wb') as file:
    file.write(content_contador)

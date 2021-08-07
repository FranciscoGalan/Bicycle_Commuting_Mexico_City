#!/usr/bin/env python
# coding: utf-8

# In[32]:


import requests
import pandas as pd


# In[33]:


# Links to csv files
url_contador = 'https://datos.cdmx.gob.mx/dataset/07d5d501-66dc-4e3e-9d92-bfa163d21434/resource/8548607a-b0c0-4210-962e-1240f715b680/download/ciclista_nuevo.csv'
url_incidentes = ''


# In[34]:


# Get data from the website
get_contador = requests.get(f'{url_contador}')
print(get_contador)


# In[35]:


# Read content
content_contador = get_contador.content


# In[36]:


# Create csv files
with open('contador-ciclistas.csv', 'wb') as file:
    file.write(content_contador)


# In[38]:


contador = pd.read_csv('contador-ciclistas.csv')
contador


# Bicycle Commuting Analysis | Mexico City

Analyzed government data from 2015 to 2020 to determine which hour, day, month, and location is the safest to travel by bicycle in Mexico City.    



## Insights

### Hour



### Day



### Month



### Location

![](https://github.com/FranciscoGalan/Bicycle_Commuting_Mexico_City/blob/main/Media/Mapa_incidentes_viales.jpg)

Explore the whole map [here](https://public.tableau.com/shared/PYW5PG24K?:display_count=y&:origin=viz_share_link). 



### Additional information

All the previous charts were created with PowerBI and Tableau. Minor details were added with Paint. 

These insights are also compiled in a PowerPoint presentation:

- English version. 
- [Spanish version](https://github.com/FranciscoGalan/Bicycle_Commuting_MexicoCity/blob/main/Media/Presentation%20(Spanish).pdf).



## Data

The original data was taken from three datasets of Mexico City's government [website](https://datos.cdmx.gob.mx/):

| Dataset                         | Location                                                     | Date of download |
| ------------------------------- | ------------------------------------------------------------ | ---------------- |
| Bicycle counter                 | https://datos.cdmx.gob.mx/dataset/contador-ciclistas         | 11-Dec-2020      |
| Road accidents                  | https://datos.cdmx.gob.mx/dataset/incidentes-viales-c5       | 11-Dec-2020      |
| Estudio de Conteo ciclista 2018 | https://datos.cdmx.gob.mx/dataset/estudio-de-conteo-ciclista-2018 | 11-Dec-2020      |

However, in the **[notebook main.ipynb](https://nbviewer.jupyter.org/github/FranciscoGalan/Bicycle_Commuting_MexicoCity/blob/main/main.ipynb)**, I explored the datasets and transformed them to a version which I could then use to create visualizations. You can fin the transformed datasets here:

| Dataset                                 | Location                                                     |
| --------------------------------------- | ------------------------------------------------------------ |
| Adapted Bicycle counter                 | https://github.com/FranciscoGalan/Bicycle_Commuting_MexicoCity/blob/main/Data/contador_final.csv |
| Adapted Road accidents                  | https://github.com/FranciscoGalan/Bicycle_Commuting_MexicoCity/blob/main/Data/incidentes_final.csv |
| Adapted Estudio de Conteo Ciclista 2018 | https://github.com/FranciscoGalan/Bicycle_Commuting_MexicoCity/blob/main/Data/estudio_final.csv |
# Bicycle Commuting Analysis | Mexico City

Analyzed government data from 2015 to 2020 to determine which hour, day, month, and location is the safest to travel by bicycle in Mexico City.    



## Data

The original data was taken from three datasets of Mexico City's government [website](https://datos.cdmx.gob.mx/):

| Dataset                         | Location                                                     | Date of download |
| ------------------------------- | ------------------------------------------------------------ | ---------------- |
| Bicycle counter                 | https://datos.cdmx.gob.mx/dataset/contador-ciclistas         | 11-Dec-2020      |
| Road accidents                  | https://datos.cdmx.gob.mx/dataset/incidentes-viales-c5       | 11-Dec-2020      |
| Estudio de Conteo ciclista 2018 | https://datos.cdmx.gob.mx/dataset/estudio-de-conteo-ciclista-2018 | 11-Dec-2020      |

However, in the **[Notebook main.ipynb](https://nbviewer.jupyter.org/github/FranciscoGalan/Bicycle_Commuting_Mexico_City/blob/main/main.ipynb)**, I explored the datasets and transformed them to a version which I could then use to create visualizations. You can fin the transformed datasets here:

| Dataset                                 | Location                                                     |
| --------------------------------------- | ------------------------------------------------------------ |
| Adapted Bicycle counter                 | https://github.com/FranciscoGalan/Bicycle_Commuting_MexicoCity/blob/main/Data/contador_final.csv |
| Adapted Road accidents                  | https://github.com/FranciscoGalan/Bicycle_Commuting_MexicoCity/blob/main/Data/incidentes_final.csv |
| Adapted Estudio de Conteo Ciclista 2018 | https://github.com/FranciscoGalan/Bicycle_Commuting_MexicoCity/blob/main/Data/estudio_final.csv |



## Insights

### Number of cyclists

Each day there are more cyclists in Mexico City, as measured by the counters in three main avenues:

![](https://github.com/FranciscoGalan/Bicycle_Commuting_Mexico_City/blob/main/Media/Contadores.png)

### Hour

Most accidents occur when the sun goes down:

![](https://github.com/FranciscoGalan/Bicycle_Commuting_Mexico_City/blob/main/Media/Accidentes%20por%20hora.jpg)

Could it be that  there are more cyclists in the evening? It is unlikely, since most cyclists report that they commute to work, so one would except a similar rate of accidents in the morning. Perhaps the accidents are caused by the lack of visibility. 

### Day

Monday and Tuesday are the safest days to cycle:

![](https://github.com/FranciscoGalan/Bicycle_Commuting_Mexico_City/blob/main/Media/Accidentes%20por%20d%C3%ADa.jpg)

This is true even considering the amount of cyclists per day (at least for Tuesdays):

![](https://github.com/FranciscoGalan/Bicycle_Commuting_Mexico_City/blob/main/Media/Ciclistas%20por%20d%C3%ADa.jpg)

### Month

The safest period of the year is the summer:

![](https://github.com/FranciscoGalan/Bicycle_Commuting_Mexico_City/blob/main/Media/Accidentes%20por%20mes.jpg)

Could it be that more people are on vacation or feel less stressed?

### Location

Accidents occur throughout Mexico City. However, many of them concentrate on the main avenues, although it is hard to tell is this is because more people pass through them. 

We also see that many accidents occur at intersections:

![](https://github.com/FranciscoGalan/Bicycle_Commuting_Mexico_City/blob/main/Media/Mapa_incidentes_viales.jpg)

Explore the whole map [here](https://public.tableau.com/shared/PYW5PG24K?:display_count=y&:origin=viz_share_link). 



### Additional information

All the previous charts were created with PowerBI and Tableau. 

These insights are also compiled in a PowerPoint presentation:

- [English version](https://github.com/FranciscoGalan/Bicycle_Commuting_Mexico_City/blob/main/Media/Presentation%20(English).pdf). 
- [Spanish version](https://github.com/FranciscoGalan/Bicycle_Commuting_MexicoCity/blob/main/Media/Presentation%20(Spanish).pdf).




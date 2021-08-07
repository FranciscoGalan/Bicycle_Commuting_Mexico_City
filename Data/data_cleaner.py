import pandas as pd
import numpy as np
import re

contador = pd.read_csv('contador-ciclistas.csv')
incidentes = pd.read_csv('incidentes-viales-c5.csv')


# ## 1. Bicycle counter

#Drop id column
contador.drop('Id', axis=1, inplace=True)

contador.columns = ['Día de la semana', 'Día', 'Mes', 'Año', 'Reforma', 'Revolución', 'Patriotismo']

# Transform months to categories to order them.
meses = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']
contador['Mes'] = pd.Categorical(contador['Mes'], meses)

# Order values in descending order.
contador = contador.sort_values(['Año', 'Mes', 'Día'])

# Change months back to object type
contador['Mes'] = contador['Mes'].astype('object')

# Label-encode months
dict_meses = {}
number = 0
for mes in meses: 
    number += 1
    dict_meses[mes] = number
    
contador['Mes'] = contador['Mes'].map(dict_meses)

# Create new column with complete date
contador.insert(4, 'Fecha', pd.to_datetime(contador.Año*10000+contador.Mes*100+contador.Día, format='%Y%m%d'))

# Reset indexes
contador = contador.reset_index(drop=True)

# Change months back to string format
dict_meses_inverso = {}
for mes, numero in dict_meses.items():
    dict_meses_inverso[numero] = mes
    
contador['Mes'] = contador['Mes'].map(dict_meses_inverso)

# Replace special characters
contador['Día de la semana'] = contador['Día de la semana'].str.replace('á', 'a').str.replace('é', 'e')


# ### Missing values

# Fill missing values up to the installation of the counters.
contador.loc[0:940, ['Revolución', 'Patriotismo']] = contador.loc[0:940, ['Revolución', 'Patriotismo']].fillna(0)

# Calculate mean of each day of each month and year. 
means = pd.DataFrame(contador.groupby([ 'Año', 'Mes', 'Día de la semana'])['Reforma' ,'Revolución', 'Patriotismo'].mean()).sort_index().reset_index()
means

# Define list of months and counters
months = ['enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre',
 'diciembre']
counters = ['Reforma', 'Revolución', 'Patriotismo']

# Fill missing values with the mean of the past month's corresponding day.
for counter in counters:
    for i in contador.index.tolist():
        if pd.isnull(contador.loc[i, counter]):
            # Get current date
            day = contador['Día de la semana'][i]
            month = contador['Mes'][i]
            year = contador['Año'][i]

            # Get mean of last available month.
            mean_last_available_month = np.NaN
            index_adjuster = 0
            while pd.isnull(mean_last_available_month):
                # Get past month and its year
                index_adjuster -= 1
                last_available_month = months[months.index(month)+index_adjuster]
                year_last_available_month = year

                if last_available_month == 'diciembre':
                    year_last_available_month -= 1

                ### Avoid outlier values from July 2017
                if last_available_month == 'julio':
                    index_adjuster -= 1
                    last_available_month = months[months.index(month)+index_adjuster]

                # Get mean of past month
                mean_last_available_month = means.loc[(means.Año == year_last_available_month) & (means.Mes == last_available_month) & (means['Día de la semana'] == day), counter].iloc[0]         

            # Assign value to cell 
            contador.loc[i, counter] = mean_last_available_month

            # Print value assigned to cell
            print(f'- Value: {mean_last_available_month} | {counter} | {i} | Year: {year_last_available_month} | Av. Month: {last_available_month} | Month: {month} | Day: {day}')

# ### Save dataset

# Create column with total cyclists of a given day
contador['total'] = contador['Patriotismo'] + contador['Revolución'] + contador['Reforma']
contador['total'] = contador['total'].astype('int64')

# Change column type to integer.
for counter in counters:
    contador[counter] = contador[counter].astype('int64')

contador_final = contador.copy()

contador_final.to_csv('Data/contador_final.csv', index=False)


# # 2. Road accidents

# ### Data exploration

incidentes = incidentes[['dia_semana', 'fecha_creacion', 'hora_creacion', 'mes', 'delegacion_inicio', 'latitud', 'longitud', 'geopoint']]

incidentes = incidentes[incidentes['hora_creacion'].str.match(r'\d\d:\d\d:\d\d') == True]

# Now let's proceed to transform the time columns.

# ### Data cleaning

# Clean day column.
incidentes['dia_semana'] = incidentes['dia_semana'].str.lower()

# Combine date and time columns
fecha_hora = pd.Series(incidentes['fecha_creacion'] + ' ' + incidentes['hora_creacion'])

# Insert new column
incidentes.insert(1, 'fecha_hora', fecha_hora)

# Change new column to datetime format
incidentes['fecha_hora'] = pd.to_datetime(incidentes['fecha_hora'], format='%d/%m/%Y %H:%M:%S')

# Change type of time columns
incidentes['fecha_creacion'] = pd.to_datetime(incidentes['fecha_creacion'], format='%d/%m/%Y')
incidentes['hora_creacion'] = pd.to_datetime(incidentes['hora_creacion'], format='%H:%M:%S').dt.time

# Drop extra columns
incidentes.drop(['fecha_creacion', 'mes'], axis=1, inplace=True)

# Create new columns with year, month, and hour. 
incidentes.insert(2, 'hora', incidentes['fecha_hora'].dt.hour)
incidentes.insert(2, 'mes', incidentes['fecha_hora'].dt.month)
incidentes.insert(2, 'año', incidentes['fecha_hora'].dt.year)

# Remove special characters
incidentes['dia_semana'] = incidentes['dia_semana'].str.replace('á', 'a').str.replace('é', 'e')

# Transform months back to text
incidentes['mes'] = incidentes['mes'].map(dict_meses_inverso)

# ### Save dataset

incidentes_final = incidentes.copy()

incidentes_final.to_csv('Data/incidentes_final.csv', index=False)
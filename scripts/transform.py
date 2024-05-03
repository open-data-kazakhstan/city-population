import pandas as pd
import numpy as np

# Loading the data
df = pd.read_excel("../archive/source.xlsx", sheet_name='01')

# Choosing relevant columns and rows
df.dropna(inplace=True)
df = df.iloc[:, :4]
# Renaming columns
df.columns = ['Region', 'Total', 'Males', 'Females']

name_map = {
    "Қазақстан Республикасы ": "The Republic of Kazakhstan",
    "Абай": "Abai Region",
    "Ақмола": "Akmola Region",
    "Ақтөбе": "Aktobe Region",
    "Алматы": "Almaty Region",
    "Атырау": "Atyrau Region",
    "Батыс Қазақстан": "West Kazakhstan Region",
    "Жамбыл": "Jambyl Region",
    "Жетісу": "Jetisu Region",
    "Қарағанды": "Karaganda Region",
    "Қостанай": "Kostanay Region",
    "Қызылорда": "Kyzylorda Region",
    "Маңғыстау": "Mangystau Region",
    "Павлодар": "Pavlodar Region",
    "Солтүстік Қазақстан": "North Kazakhstan Region",
    "Түркістан облысы": "Turkistan Region",
    "Ұлытау": "Ulytau Region",
    "Шығыс Қазақстан": "East Kazakhstan Region",
    "Астана қаласы": "Astana city",
    "Алматы қаласы": "Almaty city",
    "Шымкент қаласы": "Shymkent city"
}

df['Region'] = df['Region'].map(name_map)

# Changing first row to the end of dataframe
df = pd.concat([df.iloc[1:], df.iloc[:1]], ignore_index=True)


# Changing data types of three columns to integer
cols_to_convert = ['Total', 'Males', 'Females']
df[cols_to_convert] = df[cols_to_convert].apply(pd.to_numeric, errors='coerce', downcast='integer')
# Changing data type of the first column to string
df['Region'] = df['Region'].astype(str)

# Saving the dataframe to a csv file
df.to_csv('../data/city_population.csv', index=False)
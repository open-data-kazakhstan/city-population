import pandas as pd
import numpy as np

# Loading the data
df = pd.read_excel('../archive/source.xlsx', sheet_name='01')

# Choosing relevant columns and rows
df.dropna(inplace=True)
df = df.iloc[:, :4]
df = df.iloc[1:]
# Renaming columns
df.columns = ['Region', 'Total', 'Males', 'Females']

city_names = [
    "Abai",
    "Akmola",
    "Aktobe",
    "Almaty",
    "Atyrau",
    "Batys Kazakhstan",
    "Zhambyl",
    "Zhetisu",
    "Karagandy",
    "Kostanai",
    "Kyzylorda",
    "Mangistau",
    "Pavlodar",
    "Soltustik Kazakhstan",
    "Turkistan",
    "Ulytau",
    "Shygys Kazakhstan",
    "Astana city",
    "Almaty city",
    "Shymkent city"
]

# Changing Kazakh names to English names
df['Region'] = city_names

# Changing data types of three columns to integer
cols_to_convert = ['Total', 'Males', 'Females']
df[cols_to_convert] = df[cols_to_convert].apply(pd.to_numeric, errors='coerce', downcast='integer')
# Changing data type of the first column to string
df['Region'] = df['Region'].astype(str)

# Saving the dataframe to a csv file
df.to_csv('../data/city_population.csv', index=False)
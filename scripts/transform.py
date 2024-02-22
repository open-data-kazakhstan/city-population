import pandas as pd
import numpy as np

# Loading the data
df = pd.read_excel('../archive/source.xlsx', sheet_name='03')

# Cleaning the data
df = df.drop([0, 1, 2, 3, 4, 5])
df.dropna(inplace=True)
df = df.iloc[:, [0, 4, 5, 6]]
df.columns = ['City', 'Total','Males','Females']
df = df[df.City.str.contains('қаласы')]
df = df[df.Total > 40000]
# Sorting and indexing
df.sort_values(by='Total', ascending=False, inplace=True)
df.index = np.arange(1, len(df) + 1)
# Manual trnaslation of city names based on the sorted dataframe
english_city_names = [
    'Almaty',
    'Astana',
    'Shymkent',
    'Aktobe',
    'Karaganda',
    'Taraz',
    'Oskemen',
    'Pavlodar',
    'Atyrau',
    'Semey',
    'Kyzylorda',
    'Kostanay',
    'Aktau',
    'Oral',
    'Petropavl',
    'Turkistan',
    'Kokshetau',
    'Temirtau',
    'Taldykorgan',
    'Ekibastuz',
    'Rudny',
    'Zhezkazgan',
    'Kentau',
    'Zhanaozen',
    'Balkhash',
    'Satpayev',
    'Qonayev',
    'Arys',
    'Aksu',
    'Stepnogorsk',
    'Ridder'
]
df.City = english_city_names
# Changing the data types
df.City = df.City.astype('string')
df.Total = df.Total.astype('int')
df.Males = df.Males.astype('int')
df.Females = df.Females.astype('int')

# Saving the dataframe to a csv file
df.to_csv('../data/city_population.csv', index=False)
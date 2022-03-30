import pandas as pd

# TASK 01

data_frame = pd.read_csv('PAD_03_PD.csv', sep=';')
country = data_frame['Country'].value_counts()

print(country)

# TASK 02

data_frame['owned_goods'] = data_frame[[
    'owns_car', 'owns_TV', 'owns_house', 'owns_Phone'
]].sum(axis=1)
print(data_frame)

# TASK 03

gender_by_owned_goods = data_frame.groupby(['gender'])['owned_goods']
gender_by_owned_goods_round = round(gender_by_owned_goods.mean(), 2)
print(gender_by_owned_goods_round)

# TASK 04

grouped_by_country = data_frame.groupby(['Country'])
by_country = list(grouped_by_country.groups.keys())
by_country_owned_goods = list(round(grouped_by_country.mean()['owned_goods'], 2))
by_country_minimum_age = list(grouped_by_country['Age'].min())

new_df = pd.DataFrame(
    {
        "country": by_country,
        "owned_goods_mean": by_country_owned_goods,
        "minimum_age": by_country_minimum_age
    }
)

print(new_df)

import pandas as pd 

panda = pd.read_csv('PAD_03_PD.csv', sep=';')
genders = panda.groupby(['gender'])
print(genders.all())


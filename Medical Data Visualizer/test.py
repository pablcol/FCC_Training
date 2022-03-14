import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('medical_examination.csv')

'''weight = df['weight']
heightsq = (df['height'] * df['height'])
bmi = weight / heightsq

df['overweight'] = np.where(bmi * 10000 > 25, 1, 0)
print(df)'''

'''df['cholesterol'] = np.where(df['cholesterol'] == 1, 0, 1)
print(df['cholesterol'])
df['gluc'] = np.where(df['gluc'] == 1, 0, 1)
print(df['gluc'])
'''

variables = sorted(
    ['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

df_cat = pd.melt(df, id_vars=['cardio'], value_vars=variables)

df_cat = df_cat.value_counts().reset_index(name='total')

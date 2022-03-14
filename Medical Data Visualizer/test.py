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

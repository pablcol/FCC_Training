
import pandas as pd

df = pd.read_csv('adult.data.csv')

# race_count = df['race'].value_counts()
# print(race_count)

# average_age_men = (df.groupby('sex')['age'].mean())['Male']
# print(avg_age_men)

# percentage_bachelors = round(((df['education'].value_counts().Bachelors / df['education'].count()) * 100), 1)
# print(percentage_bachelors)

higher_education = (df['education'].value_counts().Bachelors +
                    df['education'].value_counts().Masters +
                    df['education'].value_counts().Doctorate)
print(higher_education)

lower_education = 0
print(lower_education)

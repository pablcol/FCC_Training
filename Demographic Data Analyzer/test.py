import pandas as pd

df = pd.read_csv('adult.data.csv')

# race_count = df['race'].value_counts()
# print(race_count)

# average_age_men = (df.groupby('sex')['age'].mean())['Male']
# print(avg_age_men)

# percentage_bachelors = round(((df['education'].value_counts().Bachelors / df['education'].count()) * 100), 1)
# print(percentage_bachelors)

# higher_education = df.loc[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
# print(higher_education.count)

# lower_education = df.loc[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
# print(lower_education)

# higher_education_rich = round(higher_education.loc[higher_education['salary'] == ">50K"].size
#                               / higher_education.size * 100, 1,)
# print(higher_education_rich)

# lower_education_rich = round(lower_education.loc[lower_education['salary'] == ">50K"].size
#                              / lower_education.size * 100, 1,)
# print(lower_education_rich)

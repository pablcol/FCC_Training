import pandas as pd

df = pd.read_csv('adult.data.csv')

# race_count = df['race'].value_counts()
# print(race_count)

# average_age_men = (df.groupby('sex')['age'].mean())['Male']
# print(avg_age_men)

# percentage_bachelors = round(((df['education'].value_counts().Bachelors /
#                                df['education'].count()) * 100), 1)
# print(percentage_bachelors)

# higher_education = df.loc[df['education'].isin(['Bachelors', 'Masters',
#                                                 'Doctorate'])]
# print(higher_education)
# lower_education = df.loc[~df['education'].isin(['Bachelors', 'Masters',
#                                                 'Doctorate'])]
# print(lower_education)

# higher_education_rich = round(
#     higher_education.loc[higher_education['salary'] == ">50K"].size
#     / higher_education.size * 100, 1, )
# print(higher_education_rich)

# lower_education_rich = round(
#     lower_education.loc[lower_education['salary'] == ">50K"].size
#    / lower_education.size * 100, 1, )
# print(lower_education_rich)

# min_work_hours = df['hours-per-week'].min()
# print(min_work_hours)

# num_min_workers = df.loc[df['hours-per-week'] == min_work_hours]
# rich_percentage = round(
#     num_min_workers.loc[num_min_workers['salary'] == ">50K"].size
#     / num_min_workers.size * 100, 1, )
# print(rich_percentage)

'''highest_country = (
    df[['salary', 'native-country']]
    .groupby('native-country')
    .apply(lambda g: g.loc[g["salary"] == ">50K"].size / g.size * 100)
)

highest_earning_country = highest_country.idxmax()


highest_earning_country_percentage = round(highest_country.max(), 1)
print(highest_earning_country_percentage)
'''

'''top_IN_occupation = (
    df.loc[(df['native-country'] == 'India') & (df['salary'] == '>50K')][
        'occupation'].value_counts().idxmax())
print(top_IN_occupation)
'''

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime


def parse_date(x):
    return datetime.strptime(x, "%Y-%m-%d")


df = pd.read_csv(
    'fcc-forum-pageviews.csv', index_col=['date'],
    parse_dates=['date'],
    date_parser=parse_date,
    )

df = df.loc[
    (df['value'] >= df['value'].quantile(0.025)) &
    (df['value'] <= df['value'].quantile(0.975))
]
print(df)


def draw_bar_plot():
    fig, ax = plt.subplots(figsize=(16, 6))
    ax = sns.lineplot(data=df, x='date', y='value')
    ax.set(
        xlabel='Date', ylabel='Page Views'
    )
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    fig.savefig('1.png')
    return fig


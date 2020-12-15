import pandas as pd
from Base.common import rename_header
import seaborn as sns
from matplotlib import pyplot as plt
import numpy as np

if __name__ == '__main__':
    # Load Data #
    sns.set_context("paper")
    sns.set_palette("Set2")
    df = pd.read_csv("../Data/MainData.csv")
    temp_headers = rename_header(df)
    temp_exp_data = []
    temp_time_data = []

    for row in df[['professional_experience', 'most_spent_time']].dropna().iterrows():
        for item1 in row[1]['most_spent_time'].split(";"):
            for item2 in item1.split(","):
                temp_exp_data.append(row[1]['professional_experience'])
                if item2 in temp_headers['On which software development activities, do you spend most of the time? '].keys():
                    item2 = temp_headers['On which software development activities, do you spend most of the time? '][item2]
                temp_time_data.append(item2)

    new_df = pd.DataFrame({
        "professional_experience": temp_exp_data,
        "most_spent_time": temp_time_data
    })
    contingency_table = pd.crosstab(new_df['professional_experience'], new_df['most_spent_time'])
    junior_count = np.array(contingency_table.loc[['less than 2', '2 to 5']].values.tolist()).sum(axis=0)
    senior_count = np.array(contingency_table.loc[['5 to 10', 'more than 10']].values.tolist()).sum(axis=0)
    temp_data = [(title, junior, senior) for title, junior, senior in
                 zip(contingency_table.columns.tolist(), junior_count, senior_count)]
    temp_data.sort(key=lambda item: item[1] + item[2], reverse=False)
    junior_count = [item[1] for item in temp_data]
    senior_count = [item[2] for item in temp_data]
    plt.figure(figsize=(9, 5))

    width = 0.35
    y_axis_labels = []
    for item in [item[0] for item in temp_data]:
        if item in temp_headers['On which software development activities, do you spend most of the time? '].keys():
            item = temp_headers['On which software development activities, do you spend most of the time? '][item]
        y_axis_labels.append(item.strip())


    x = np.arange(len([item[0] for item in temp_data]))
    plt.yticks(ticks=x, labels=y_axis_labels, fontsize=13)
    plt.xticks(fontsize=13)
    p1 = plt.barh(x - width / 2, junior_count, width, label='Junior Developers')
    p2 = plt.barh(x + width / 2, senior_count, width, label='Senior Developers')
    plt.ylabel("Most Spent time")
    plt.xlabel("Number of Respondents")
    plt.ylabel("")
    plt.legend()
    plt.savefig("../Figures/Activity_and_Seniority.eps", format='eps', dpi=5000, bbox_inches='tight')
    plt.show()

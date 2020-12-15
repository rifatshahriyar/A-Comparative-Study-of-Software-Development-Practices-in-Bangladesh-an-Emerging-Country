import pandas as pd
from Base.common import rename_header
from FigureGenerators.reqgather import FigureController as RequirementFigureController
from matplotlib import pyplot as plt
import seaborn as sns
import random
import numpy as np
import re

if __name__ == '__main__':
    # Load Data #
    df = pd.read_csv("../Data/MainData.csv")
    temp_headers = rename_header(df)
    temp_req_data = []
    temp_tech_data = []
    for row in df[['requirements_gathering', 'technology_experience']].dropna().iterrows():
        for item2 in re.split(";|,", row[1]['requirements_gathering']):
            for key, value in temp_headers["Which of the followings do you use for requirements gathering?"].items():
                if isinstance(value, list) and item2.strip() in value:
                    item2 = key
                    break
            for item3 in re.split(";", row[1]['technology_experience']):
                for key, value in temp_headers["Which of the following technologies do you have experience working in?"].items():
                    if item3.strip() == key:
                        item3 = value
                        break
                temp_req_data.append(item2.replace(" ", "\n"))
                temp_tech_data.append(item3)

    new_df = pd.DataFrame({
        "requirements_gathering": [item.strip().lower().capitalize() for item in temp_req_data],
        "technology_experience": [item for item in temp_tech_data]
    })
    contingency_table = pd.crosstab(new_df['requirements_gathering'], new_df['technology_experience'])
    x_axis_data = []
    y_axis_data = []
    s_axis_data = []
    #random.seed(77, 2)
    sns.set_context("paper")
    sns.set_palette("Set2", 3)
    column_data = contingency_table.columns.tolist()
    row_data = contingency_table.index.tolist()
    #random.shuffle(column_data)
    #random.shuffle(row_data)
    for column in column_data:
        for row in row_data:
            if contingency_table.loc[row, column] > 0:
                x_axis_data.append(row)
                y_axis_data.append(column)
                s_axis_data.append(contingency_table.loc[row, column] * 20)
    plt.figure(figsize=(9, 5))
    plt.xticks(rotation=90, fontsize=13)
    plt.yticks(fontsize=13)
    plt.xlabel("Requirement gathering process", fontsize=13)
    plt.ylabel("Technology", fontsize=13)
    plt.scatter(x=x_axis_data, y=y_axis_data, s=s_axis_data, alpha=0.7)
    plt.savefig("../Figures/Requirement_Technology_Cross_Analysis.eps", format='eps', dpi=5000, bbox_inches='tight')

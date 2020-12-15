import pandas as pd
from FisherExact import fisher_exact

from Base.common import rename_header
import seaborn as sns
from matplotlib import pyplot as plt
import numpy as np
import scipy.stats as ss
import re


def get_contingency_table(table, row_name, column_name):
    a = table.loc[row_name][column_name]
    b = table.loc[row_name].drop(columns=[column_name]).sum().sum()
    c = table.drop(index=[row_name])[column_name].sum().sum()
    d = table.drop(index=[row_name]).drop(columns=[column_name]).sum().sum()
    return np.array([[a, b], [c, d]])


def merge_column(table, column1, column2):
    table = table.copy(deep=True)
    table[column1 + "_" + column2] = table[column1] + table[column2]
    return table.drop(columns=[column1, column2])


def merge_row(table, index1, index2):
    table = table.copy(deep=True)
    new_row = table.loc[[index1, index2]].sum()
    new_row.name = index1 + "_" + index2
    table = table.append(new_row)
    return table.drop(index=[index1, index2])


if __name__ == '__main__':
    # Load Data #
    sns.set_context("paper")
    sns.set_palette("Set2")
    df = pd.read_csv("../Data/MainData.csv")
    temp_headers = rename_header(df)
    temp_tech_data = []
    temp_framework_data = []

    for row in df[['technology_experience', 'framework']].dropna().iterrows():
        for item1 in re.split(';|, ', row[1]['technology_experience']):
            for key, value in temp_headers[
                "Which of the following technologies do you have experience working in?"].items():
                if isinstance(value, list) and item1 in value:
                    item1 = key
                    break
            for item2 in re.split(';|, ', row[1]['framework'].strip()):
                for key, value in temp_headers["Which frameworks are you using?"].items():
                    if isinstance(value, list) and item2 in value:
                        item2 = key
                        break
                temp_tech_data.append(item1)
                temp_framework_data.append(item2)

    new_df = pd.DataFrame({
        "tech": temp_tech_data,
        "framework": temp_framework_data
    })
    contingency_table = pd.crosstab(new_df['tech'], new_df["framework"])

    print(ss.chi2_contingency(
        get_contingency_table(merge_column(contingency_table, 'Django', 'Spring'), 'Web', 'Django_Spring')))

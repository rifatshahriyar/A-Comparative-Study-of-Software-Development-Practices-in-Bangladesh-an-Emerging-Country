import pandas as pd
from FisherExact import fisher_exact

from Base.common import rename_header
import seaborn as sns
from matplotlib import pyplot as plt
import numpy as np
import scipy.stats as ss
import re
from CodeSample.SampleGenerator import get_formatted_dataframe


def get_contingency_table(table, row_name, column_name):
    a = table.loc[row_name][column_name]
    b = table.loc[row_name].drop(columns=[column_name]).sum().sum()
    c = table.drop(index=[row_name])[column_name].sum().sum()
    d = table.drop(index=[row_name]).drop(columns=[column_name]).sum().sum()
    return np.array([[a, b], [c, d]])


if __name__ == '__main__':
    # Load Data #
    sns.set_context("paper")
    sns.set_palette("Set2")
    closed_data = pd.read_csv("../Data/MainData.csv")
    temp_headers = rename_header(closed_data)
    open_ended_data,codes = get_formatted_dataframe("How_do_you_ensure_security_of_your_products__1.csv")#pd.read_csv("../Data/Coded_Data/How_do_you_ensure_security_of_your_products__1.csv")
    target_columns = open_ended_data.columns.tolist()
    target_columns.remove('Answer')
    target_columns.append('framework')
    data_dict = {item: [] for item in target_columns}
    df = pd.merge(closed_data, open_ended_data, left_on='security', right_on='Answer')[target_columns]
    for row in df.dropna().iterrows():
        for item2 in re.split(';|, ', row[1]['framework'].strip()):
            for key, value in temp_headers["Which frameworks are you using?"].items():
                if isinstance(value, list) and item2 in value:
                    item2 = key
                    break
            data_dict['framework'].append(item2)
            temp_list = row[1].index.tolist()
            temp_list.remove("framework")
            for column in temp_list:
                data_dict[column].append(int(row[1][column]))

    new_df = pd.DataFrame(data_dict)
    contingency_table = pd.crosstab(new_df['framework'], new_df['Dependent on framework'])
    print(ss.chi2_contingency(contingency_table))


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
    return np.array([[a,b],[c,d]])
if __name__ == '__main__':
    # Load Data #
    sns.set_context("paper")
    sns.set_palette("Set2")
    df = pd.read_csv("../Data/MainData.csv")
    temp_headers = rename_header(df)
    temp_test_data = []
    temp_experience_data = []

    for row in df[['testing', 'professional_experience']].dropna().iterrows():
        for item1 in row[1]['testing'].split(";"):
            for item2 in item1.split(","):
                for key, value in temp_headers["What types of software testing practices do you use?"].items():
                    if isinstance(value, list) and item2.strip() in value:
                        item2 = key
                        flag = True
                        break
                for item4 in re.split(';', row[1]['professional_experience'].strip()):

                    temp_test_data.append(item2)
                    temp_experience_data.append(item4)

    new_df = pd.DataFrame({
        "test": temp_test_data,
        "experience": temp_experience_data
    })
    number_dict = {'less than 2':0, '2 to 5':1, '5 to 10':2, 'more than 10':3}
    new_df['experience_num'] = new_df['experience'].map(lambda x: number_dict[x])
    new_df.sort_values(by='experience_num',ascending=True,inplace=True,ignore_index=True)
    contingency_table = pd.crosstab(new_df['test'], new_df["experience_num"]).T
    selected_test = new_df[new_df['test'].isin(['Unit testing', 'Integration Testing', 'Functional testing'])][
        'test'].values.tolist()
    other_tests = new_df[~new_df['test'].isin(['Unit testing', 'Integration Testing', 'Functional testing'])][
        'test'].values.tolist()

    print(ss.mannwhitneyu(selected_test, other_tests))

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
    temp_tech_data = []
    temp_language_data = []

    for row in df[['technology_experience', 'programming_language']].dropna().iterrows():
        for item1 in row[1]['technology_experience'].split(";"):
            for item2 in item1.strip().split(","):
                for item4 in re.split(';|, ', row[1]['programming_language'].strip()):
                    for key, value in temp_headers["Which programming languages are you using?"].items():
                        if isinstance(value, list) and item4 in value:
                            item4 = key
                            break
                    temp_tech_data.append(item2)
                    temp_language_data.append(item4)

    new_df = pd.DataFrame({
        "tech": temp_tech_data,
        "language": temp_language_data
    })
    contingency_table = pd.crosstab(new_df['tech'], new_df["language"])
    web_and_mobile = contingency_table.loc[['Mobile','Web']].sum()
    web_and_mobile.name = "Web_Mobile"
    contingency_table = contingency_table.append(web_and_mobile)
    print(ss.chi2_contingency(get_contingency_table(contingency_table,'Web','JavaScript')))
    # print(fisher_exact(contingency_table,workspace=4e100))
    # print(ss.c)
    # contingency_table.loc['Mobile'].drop(index=['Swift']).sum().sum()
    # contingency_table.drop(index=['Mobile'])['Swift'].sum().sum()
    # chi2, p, dof, ex = ss.chi2_contingency(contingency_table[contingency_table >= 5])
    # print(chi2, p, dof, ex)

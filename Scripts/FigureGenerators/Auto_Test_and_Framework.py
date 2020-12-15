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
    temp_framework_data = []

    for row in df[['automated_testing', 'framework']].dropna().iterrows():

        item1 = row[1]['automated_testing']
        # for item1 in row[1]['automated_testing'].split(";"):
        #         if item1 in temp_headers["What is the level of automated testing in your projects?"]:
        #             item1 = temp_headers["What is the primary operating system you are developing on?"][item1]
        for item4 in re.split(';|, ', row[1]['framework'].strip()):
            for key, value in temp_headers["Which frameworks are you using?"].items():
                if isinstance(value, list) and item4 in value:
                    item4 = key
                    break
            temp_test_data.append(item1)
            temp_framework_data.append(item4)

    new_df = pd.DataFrame({
        "test": temp_test_data,
        "framework": temp_framework_data
    })
    contingency_table = pd.crosstab(new_df['test'], new_df["framework"])
    percentage_table = (contingency_table / contingency_table.sum()) * 100
    ax = percentage_table.T.plot.bar(stacked=True,figsize=(6, 4))
    ax.legend(loc='upper right', bbox_to_anchor=(0.46, 1.17),
              ncol=3, fancybox=True, shadow=True)
    ax.set_xlabel("Framework")
    ax.set_ylabel("Percentage (%)")
    ax.get_figure().savefig("../Figures/Framework_and_Test_Level.eps", format='eps', dpi=5000, bbox_inches='tight')

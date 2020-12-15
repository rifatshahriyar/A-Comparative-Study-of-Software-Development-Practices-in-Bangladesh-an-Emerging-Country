import pandas as pd
from Base.common import rename_header
import seaborn as sns
from StatisticalTests.Column_Converter import *
from matplotlib import pyplot as plt


def get_stats(dataframe, column1, column2, percentage=False, dump=False, only_max=False):
    table = pd.crosstab(dataframe[column1], dataframe[column2])

    table = round((table.T / table.sum(axis=1)).T * 100, 2) if percentage else table
    index_condition = True
    if only_max:
        table = pd.DataFrame([(row, column, table.loc[row, column]) for row, column in
                              zip(table.index.tolist(), table.idxmax(axis=1).tolist())],
                             columns=[column1, column2, "Count_Percentage"])
        index_condition = False

    if dump:
        table.to_csv("temp.csv", index=index_condition)
    return table


if __name__ == '__main__':
    # Load Data #
    sns.set_context("paper")
    sns.set_palette("muted")
    df = pd.read_csv("../Data/MainData.csv")
    temp_headers = rename_header(df)
    data = get_stats(convert_role(df, temp_headers), "current_role",
                     "gender", percentage=True, dump=True, only_max=False)
    bar_width =1.0
    ax = data.plot.bar(width=bar_width, figsize=(12, 6))
    ax.legend(loc='upper right', bbox_to_anchor=(0.85, 1.16),
              ncol=len(data.columns) // 2, fancybox=True, shadow=True, fontsize=10)
    for p in ax.patches:
        if p.get_height() > 0:
            ax.annotate(str(p.get_height()) + "%", (p.get_x() + 0.03, p.get_height()*0.7), rotation=90,fontsize=13)
    plt.xticks(fontsize=16, rotation=0)
    plt.yticks(fontsize=16)
    ax.set_xlabel("Gender", fontsize=16)
    ax.set_ylabel("Percentage (%)", fontsize=16)
    ax.get_figure().savefig("../Figures/Gender_and_Role.eps", format='eps', dpi=5000, bbox_inches='tight')


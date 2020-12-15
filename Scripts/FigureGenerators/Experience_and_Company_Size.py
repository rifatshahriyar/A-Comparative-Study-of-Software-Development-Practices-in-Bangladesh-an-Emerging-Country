

import pandas as pd
from Base.common import rename_header
import seaborn as sns
from matplotlib import pyplot as plt
import numpy as np

from StatisticalTests.Column_Converter import convert_size
from StatisticalTests.Role_VS_All_STATS import get_stats

if __name__ == "__main__":
    sns.set_context("paper")
    sns.set_palette("Set2")
    df = pd.read_csv("../Data/MainData.csv")
    temp_headers = rename_header(df)

    data = get_stats(convert_size(df, temp_headers), "professional_experience",
                     "size", percentage=True, dump=True, only_max=False)
    data = data.T
    data = data.reindex(['less than 2', '2 to 5', '5 to 10', 'more than 10'], axis=1)
    data = data.reindex(['Very Small', 'Small', 'Medium', 'Big', 'Large'], axis=0)
    ax = data.plot.bar(stacked=True,figsize=(8, 6))
    ax.set_xlabel("Company Size")
    ax.set_ylabel("Employee Count")
    ax.legend(title= "Professional Experience")
    ax.get_figure().savefig("../Figures/Employee_Company_Size.pdf", format='pdf', dpi=5000, bbox_inches='tight')
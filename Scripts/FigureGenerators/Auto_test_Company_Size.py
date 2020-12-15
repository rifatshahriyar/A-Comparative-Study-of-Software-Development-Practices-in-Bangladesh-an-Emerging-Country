

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

    data = get_stats(convert_size(df, temp_headers), "automated_testing",
                     "size", percentage=True, dump=True, only_max=False)
    data = data.reindex(['Very Small', 'Small', 'Medium', 'Big', 'Large'], axis=1)
    ax = data.plot.bar(stacked=True,figsize=(8, 6))
    ax.set_xlabel("Automatic Test Level")
    ax.set_ylabel("Respondents Percentage (%)")
    ax.legend(title= "Professional Experience")
    ax.legend(loc='upper right', bbox_to_anchor=(0.55, 1.12),
              ncol=4, fancybox=True, shadow=True)
    plt.show()
    ax.get_figure().savefig("../Figures/Auto_Test_Company_Size.pdf", format='pdf', dpi=5000, bbox_inches='tight')
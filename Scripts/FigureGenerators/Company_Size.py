import pandas as pd
from Base.common import rename_header
import seaborn as sns
from matplotlib import pyplot as plt
import numpy as np

from StatisticalTests.Column_Converter import convert_size

if __name__ == '__main__':
    # Load Data #
    sns.set_context("paper")
    sns.set_palette("Set2")
    df = pd.read_csv("../Data/MainData.csv")
    temp_headers = rename_header(df)
    df = convert_size(df, temp_headers)
    total_count = df['size'].value_counts().sum()
    def set_count(x):
        return str(int(x*total_count*0.01)) + " (" + str(round(x, 2)) + "%)"
    ax = df['size'].value_counts().plot.pie(autopct=set_count, shadow=True,pctdistance=0.8,figsize=(6,6))
    ax.set_ylabel("")
    centre_circle = plt.Circle((0, 0), 0.6, color='black', fc='white', linewidth=0.8)
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)

    # Set aspect ratio to be equal so that pie is drawn as a circle.
    plt.axis('equal')
    ax.get_figure().savefig("../Figures/Company_Size.pdf", format='pdf', dpi=5000, bbox_inches='tight')

import pandas as pd
from Base.common import rename_header
import seaborn as sns
from matplotlib import pyplot as plt
import numpy as np
import scipy.stats as ss

def cramers_corrected_stat(confusion_matrix):
    """ calculate Cramers V statistic for categorial-categorial association.
        uses correction from Bergsma and Wicher,
        Journal of the Korean Statistical Society 42 (2013): 323-328
    """
    chi2, p, dof, ex = ss.chi2_contingency(confusion_matrix)
    n = confusion_matrix.sum().sum()
    phi2 = chi2/n
    r,k = confusion_matrix.shape
    phi2corr = max(0, phi2 - ((k-1)*(r-1))/(n-1))
    rcorr = r - ((r-1)**2)/(n-1)
    kcorr = k - ((k-1)**2)/(n-1)
    return np.sqrt(phi2corr / min( (kcorr-1), (rcorr-1)))


if __name__ == '__main__':
    # Load Data #
    sns.set_context("paper")
    sns.set_palette("Set2")
    df = pd.read_csv("../Data/MainData.csv")
    temp_headers = rename_header(df)
    temp_methodology_data = []
    temp_time_data = []

    for row in df[['methodology', 'most_spent_time']].dropna().iterrows():
        for item1 in row[1]['most_spent_time'].split(";"):
            for item2 in item1.split(","):
                for item4 in row[1]['methodology'].split(";"):

                        if item4 in temp_headers['Which of the following software development methodologies do you follow?'].keys():
                            item4 = temp_headers['Which of the following software development methodologies do you follow?'][item4]
                        elif item4 in temp_headers[
                            'Which of the following software development methodologies do you follow?']['Others']:
                            item4 = 'Others'
                        if item2 in temp_headers['On which software development activities, do you spend most of the time? '].keys():
                            item2 = temp_headers['On which software development activities, do you spend most of the time? '][item2]
                        temp_time_data.append(item2)
                        temp_methodology_data.append(item4)
    new_df = pd.DataFrame({
        "methodology": temp_methodology_data,
        "time": temp_time_data
    })
    contingency_table = pd.crosstab(new_df['methodology'],new_df["time"])
    contingency_table.to_csv("temp.csv")
    print(cramers_corrected_stat(contingency_table))
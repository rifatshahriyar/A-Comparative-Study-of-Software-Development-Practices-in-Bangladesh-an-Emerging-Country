import pandas as pd
from FisherExact import fisher_exact

from Base.common import rename_header
import seaborn as sns
from matplotlib import pyplot as plt
import numpy as np
import scipy.stats as ss



if __name__ == '__main__':
    # Load Data #
    sns.set_context("paper")
    sns.set_palette("Set2")
    df = pd.read_csv("../Data/MainData.csv")
    temp_headers = rename_header(df)
    temp_experience_data = []
    temp_os_data = []

    for row in df[['professional_experience', 'operating_system']].dropna().iterrows():
        for item1 in row[1]['professional_experience'].split(";"):
            for item2 in item1.split(","):
                for item4 in row[1]['operating_system'].split(";"):
                    # for item4 in item3.split(","):
                        if item4 in temp_headers["What is the primary operating system you are developing on?"]:
                            item4 = temp_headers["What is the primary operating system you are developing on?"][item4]
                        temp_experience_data.append(item2)
                        temp_os_data.append(item4)

    new_df = pd.DataFrame({
        "experience": temp_experience_data,
        "os": temp_os_data
    })
    print(new_df['os'].unique())
    ordinal_dict = {'less than 2':1, '2 to 5':2, '5 to 10':3, 'more than 10':4}
    new_df['ordinal_experience'] = new_df['experience'].map(lambda x: ordinal_dict[x])
    print(ss.mannwhitneyu(new_df[new_df['os']=='Linux']['ordinal_experience'].values.tolist(),new_df[new_df['os']!='Linux']['ordinal_experience'].values.tolist()))
    # Null hypo same, alternate hypo bot same
    # if p> 0.05 then null hypo is true

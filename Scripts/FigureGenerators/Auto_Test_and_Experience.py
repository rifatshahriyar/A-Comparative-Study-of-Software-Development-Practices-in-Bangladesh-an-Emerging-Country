import pandas as pd
from FisherExact import fisher_exact

from Base.common import rename_header
import seaborn as sns
from matplotlib import pyplot as plt
import numpy as np
import scipy.stats as ss
import re
import random
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

    for row in df[['automated_testing', 'professional_experience']].dropna().iterrows():

        item1 = row[1]['automated_testing']
        for item2 in re.split(';', row[1]['professional_experience'].strip()):
            temp_test_data.append(item1)
            temp_experience_data.append(item2)


    new_df = pd.DataFrame({
        "test": temp_test_data,
        "experience": temp_experience_data
    })
    contingency_table = pd.crosstab(new_df['test'], new_df["experience"])

    random.seed(77, 2)
    sns.set_context("paper")
    sns.set_palette("Set2", 3)
    column_data = contingency_table.columns.tolist()
    row_data = contingency_table.index.tolist()
    number_dict = {
        'less than 2':1, '2 to 5': 2, '5 to 10': 3, 'more than 10':4
    }
    x_axis_data = []
    y_axis_data = []
    s_axis_data = []
    for column in column_data:
        for row in row_data:
            if contingency_table.loc[row, column] > 0:
                x_axis_data.append(str(row))
                y_axis_data.append(number_dict[column])
                s_axis_data.append(contingency_table.loc[row, column] * 500)
    plt.figure(figsize=(9, 5))
    plt.yticks(ticks=[1.0,1.5,2.0,2.5,3.0,3.5,4.0],labels=['less than 2',None,'2 to 5',None,'5 to 10',None,'more than 10'], fontsize=13)
    plt.xlabel("Automatic Testing levels", fontsize=13)
    plt.ylabel("Experience", fontsize=13)
    plt.scatter(x=x_axis_data, y=y_axis_data, s=s_axis_data, alpha=0.7,data=s_axis_data)
    for data in zip(x_axis_data,y_axis_data,s_axis_data):
        plt.annotate(int(data[2] / 500), (data[0], data[1]))
    plt.savefig("../Figures/Auto_Test_and_Experience.eps", format='eps', dpi=5000, bbox_inches='tight')
import pandas as pd
from Base.common import rename_header
import seaborn as sns
from scipy import stats as ss
from StatisticalTests.Column_Converter import *



if __name__ == '__main__':
    # Load Data #
    sns.set_context("paper")
    sns.set_palette("Set2")
    df = pd.read_csv("../Data/MainData.csv")
    temp_headers = rename_header(df)
    df = df[['gender', 'professional_experience']].dropna().reset_index()
    experience_data = {'less than 2':1, '2 to 5':2, '5 to 10':3, 'more than 10':4}
    df['professional_experience'] = df['professional_experience'].map(lambda x: experience_data[x])
    print(ss.mannwhitneyu(df[df['gender'] == 'Male']['professional_experience'].values.tolist(), df[df['gender'] == 'Female']['professional_experience'].values.tolist()))

# Created by Partha at 1/14/20
from Base.common import rename_header, get_question_from_header
import pandas as pd

USE_ZIP = False

def convert_column(column_name, question, dataframe):
    file_name = question + "_raw_dataset.txt"
    file = open(file_name, "w")
    for item in dataframe.iterrows():
        if USE_ZIP:
            specifier = "\n==--endcodeableunit--==\n"
        else:
            specifier = "\n\n"
        if isinstance(item[1][column_name], str):
            file.write(item[1][column_name] + specifier)
        else:
            file.write("Did not responded. "+specifier)

    file.close()


if __name__ == '__main__':
    OPEN_ENDED_QUESTION_SET = ['manager_expectation', 'RD_involvement', "scalability", "performance", "security",
                               "employee_expectation", "candidate_expectation",
                               "university_expectation", "government_expectation", "training"]
    # Load Data #
    df = pd.read_csv("../Data/MainData.csv")
    rename_header(df)
    for item in OPEN_ENDED_QUESTION_SET:
        question = get_question_from_header(item)
        convert_column(item, question, df)

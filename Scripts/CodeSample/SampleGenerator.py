# Created by Partha at 1/31/20
from Base.common import rename_header, get_question_from_header
import pandas as pd
import re


def sanitize_string(text_array):
    return [item.replace("\"", "") for item in text_array]


def get_formatted_dataframe(question_file_name):
    data_file = open("../Data/Coded_Data/" + question_file_name)
    unique_codes = None
    for line in data_file:
        tokenized_row = re.findall("\".*?\"", line)
        if unique_codes is None:
            unique_codes = set(sanitize_string(tokenized_row[3:-1]))
        else:
            unique_codes.update(sanitize_string(tokenized_row[3:-1]))

    column_data = []
    header_data = ["Answer"]
    for item in unique_codes:
        header_data.append(item)
    data_file.seek(0)
    for line in data_file:
        tokenized_row = re.findall("\".*?\"", line)
        row_data = [tokenized_row[1].replace("\"", "")]
        for item in unique_codes:
            if item in sanitize_string(tokenized_row[3:-1]):
                row_data.append(True)
            else:
                row_data.append(False)
        column_data.append(tuple(row_data))
    dataframe = pd.DataFrame(column_data, columns=header_data)
    return dataframe, sorted(unique_codes)


def get_sample(column_name):
    # This method will take input the type of the question from Data/Coded_Data/Headers.json
    # This method will print Coded category, percentage of that category in  data and all the responses under this category input 's' if you want to stop and enter to continue
    question_file_name = get_question_from_header(column_name).rstrip()[:-1].rstrip().replace(" ", "_") + "__1.csv"
    dataframe, unique_codes = get_formatted_dataframe(question_file_name)
    for item in unique_codes:
        print('\033[31m', item, '\033[0m', sep='')
        matching_rows = dataframe[getattr(dataframe, item) == True]['Answer'].index.to_list()
        print('\033[31m', "Percentage " + str(round((len(matching_rows) / len(dataframe)) * 100, 2)) + "%", '\033[0m',
              sep='')
        for element in matching_rows:
            print(element + 1, dataframe.loc[element]['Answer'])
            temp_input = input()
            if temp_input == 's':
                break


if __name__ == "__main__":
    # get_sample("training")
    get_sample("manager_expectation")

import pandas as pd
import re
from CodeSample.SampleGenerator import get_formatted_dataframe
import math
import sys

def convert_age(dataframe, header, column_name='age'):
    def helper(x, dictionary):
        for key, value in dictionary.items():
            if value[0] <= x <= value[1]:
                return key
        return x

    convert_dictionary = dict()
    age_bucket = 5
    age_data = dataframe[column_name].dropna().astype(int)
    for start, end in zip(range(age_data.min(), age_data.max(), age_bucket),
                          range(age_data.min() + age_bucket, age_data.max() + age_bucket, age_bucket)):
        convert_dictionary[str(start) + " to " + str(end)] = (start, end)
    dataframe[column_name] = dataframe[column_name].map(lambda x: helper(x, convert_dictionary))
    return dataframe


def convert_dev_method(dataframe, header, column_name='methodology'):
    data_dict = {item: [] for item in dataframe.columns.tolist()}
    for row in dataframe.iterrows():
        if isinstance(row[1][column_name], str) or not math.isnan(row[1][column_name]):
            for item1 in re.split(';', row[1][column_name].strip()):
                for key, value in get_header_item(header, column_name).items():
                    if isinstance(value, list) and item1 in value:
                        item1 = key
                        break
                data_dict[column_name].append(item1)
                temp_list = row[1].index.tolist()
                temp_list.remove(column_name)
                for column in temp_list:
                    data_dict[column].append(row[1][column])
    return pd.DataFrame(data_dict)


def get_header_item(headers, column_name):
    temp = {value['header']: key for key, value in headers.items()}
    return headers[temp[column_name]]


def convert_size(dataframe, header, column_name='size'):
    data_dict = {item: [] for item in dataframe.columns.tolist()}
    size_dict = {
        "Very Small": range(0, 20 + 1),
        "Small": range(21, 50 + 1),
        "Medium": range(51, 150 + 1),
        "Big": range(150, 500 + 1),
        "Large": range(501, sys.maxsize)
    }
    for row in dataframe.iterrows():
        if isinstance(row[1][column_name], str) or not math.isnan(row[1][column_name]):
            item1 = row[1][column_name]
            for key, value in size_dict.items():
                if item1 in value:
                    item1 = key
                    break
            data_dict[column_name].append(item1)
            temp_list = row[1].index.tolist()
            temp_list.remove(column_name)
            for column in temp_list:
                data_dict[column].append(row[1][column])
    return pd.DataFrame(data_dict)


def convert_role(dataframe, header, column_name='current_role'):
    data_dict = {item: [] for item in dataframe.columns.tolist()}
    for row in dataframe.iterrows():
        if isinstance(row[1][column_name], str) or not math.isnan(row[1][column_name]):
            for item1 in re.split(';', row[1][column_name]):
                for key, value in get_header_item(header, column_name).items():
                    if isinstance(value, list) and item1 in value:
                        item1 = key
                        break
                data_dict[column_name].append(item1)
                temp_list = row[1].index.tolist()
                temp_list.remove(column_name)
                for column in temp_list:
                    data_dict[column].append(row[1][column])
    return pd.DataFrame(data_dict)


def convert_req_gather(dataframe, header, column_name='requirements_gathering'):
    data_dict = {item: [] for item in dataframe.columns.tolist()}
    for row in dataframe.iterrows():
        if isinstance(row[1][column_name], str) or not math.isnan(row[1][column_name]):
            for item1 in re.split(';|,', row[1][column_name].strip()):
                for key, value in get_header_item(header, column_name).items():
                    if isinstance(value, list) and item1.strip() in value:
                        item1 = key
                        break
                data_dict[column_name].append(item1)
                temp_list = row[1].index.tolist()
                temp_list.remove(column_name)
                for column in temp_list:
                    data_dict[column].append(row[1][column])
    return pd.DataFrame(data_dict)


def convert_dev_activity(dataframe, header, column_name='most_spent_time'):
    data_dict = {item: [] for item in dataframe.columns.tolist()}
    for row in dataframe.iterrows():
        if isinstance(row[1][column_name], str) or not math.isnan(row[1][column_name]):
            for item1 in re.split(';|,', row[1][column_name].strip()):
                for key, value in get_header_item(header, column_name).items():
                    if isinstance(value, list) and item1.strip() in value:
                        item1 = key
                        break
                data_dict[column_name].append(item1)
                temp_list = row[1].index.tolist()
                temp_list.remove(column_name)
                for column in temp_list:
                    data_dict[column].append(row[1][column])
    return pd.DataFrame(data_dict)


def convert_os(dataframe, header, column_name='operating_system'):
    data_dict = {item: [] for item in dataframe.columns.tolist()}
    for row in dataframe.iterrows():
        if isinstance(row[1][column_name], str) or not math.isnan(row[1][column_name]):
            for item1 in re.split(';|,', row[1][column_name].strip()):
                for key, value in get_header_item(header, column_name).items():
                    if isinstance(value, list) and item1.strip() in value:
                        item1 = key
                        break
                if len(item1) > 0:
                    data_dict[column_name].append(item1)
                    temp_list = row[1].index.tolist()
                    temp_list.remove(column_name)
                    for column in temp_list:
                        data_dict[column].append(row[1][column])
    return pd.DataFrame(data_dict)


def convert_language(dataframe, header, column_name='programming_language'):
    data_dict = {item: [] for item in dataframe.columns.tolist()}
    for row in dataframe.iterrows():
        if isinstance(row[1][column_name], str) or not math.isnan(row[1][column_name]):
            for item1 in re.split(';|,', row[1][column_name].strip()):
                for key, value in get_header_item(header, column_name).items():
                    if isinstance(value, list) and item1.strip() in value:
                        item1 = key
                        break
                if len(item1) > 0:
                    data_dict[column_name].append(item1)
                    temp_list = row[1].index.tolist()
                    temp_list.remove(column_name)
                    for column in temp_list:
                        data_dict[column].append(row[1][column])
    return pd.DataFrame(data_dict)


def convert_framework(dataframe, header, column_name='framework'):
    data_dict = {item: [] for item in dataframe.columns.tolist()}
    for row in dataframe.iterrows():
        if isinstance(row[1][column_name], str) or not math.isnan(row[1][column_name]):
            for item1 in re.split(';|,', row[1][column_name].strip()):
                for key, value in get_header_item(header, column_name).items():
                    if isinstance(value, list) and item1.strip() in value:
                        item1 = key
                        break
                data_dict[column_name].append(item1)
                temp_list = row[1].index.tolist()
                temp_list.remove(column_name)
                for column in temp_list:
                    data_dict[column].append(row[1][column])
    return pd.DataFrame(data_dict)


def convert_ide(dataframe, header, column_name='ide'):
    data_dict = {item: [] for item in dataframe.columns.tolist()}
    for row in dataframe.iterrows():
        if isinstance(row[1][column_name], str) or not math.isnan(row[1][column_name]):
            for item1 in re.split(';|,', row[1][column_name].strip()):
                for key, value in get_header_item(header, column_name).items():
                    if isinstance(value, list) and item1.strip() in value:
                        item1 = key
                        break
                data_dict[column_name].append(item1)
                temp_list = row[1].index.tolist()
                temp_list.remove(column_name)
                for column in temp_list:
                    data_dict[column].append(row[1][column])
    return pd.DataFrame(data_dict)


def convert_test_type(dataframe, header, column_name='testing'):
    data_dict = {item: [] for item in dataframe.columns.tolist()}
    for row in dataframe.iterrows():
        if isinstance(row[1][column_name], str) or not math.isnan(row[1][column_name]):
            for item1 in re.split(';|,', row[1][column_name].strip()):
                for key, value in get_header_item(header, column_name).items():
                    if isinstance(value, list) and item1.strip() in value:
                        item1 = key
                        break
                data_dict[column_name].append(item1)
                temp_list = row[1].index.tolist()
                temp_list.remove(column_name)
                for column in temp_list:
                    data_dict[column].append(row[1][column])
    return pd.DataFrame(data_dict)


def convert_test_qa(dataframe, header, column_name='QA'):
    data_dict = {item: [] for item in dataframe.columns.tolist()}
    for row in dataframe.iterrows():
        if isinstance(row[1][column_name], str) or not math.isnan(row[1][column_name]):
            for item1 in re.split(';', row[1][column_name].strip()):
                for key, value in get_header_item(header, column_name).items():
                    if isinstance(value, list) and item1 in value:
                        item1 = key
                        break
                if len(item1) > 0:
                    data_dict[column_name].append(item1)
                    temp_list = row[1].index.tolist()
                    temp_list.remove(column_name)
                    for column in temp_list:
                        data_dict[column].append(row[1][column])
    return pd.DataFrame(data_dict)


def convert_cd(dataframe, header, column_name='CD'):
    data_dict = {item: [] for item in dataframe.columns.tolist()}
    for row in dataframe.iterrows():
        if isinstance(row[1][column_name], str) or not math.isnan(row[1][column_name]):
            for item1 in re.split(';|,', row[1][column_name].strip()):
                for key, value in get_header_item(header, column_name).items():
                    if isinstance(value, list) and item1.strip() in value:
                        item1 = key
                        break
                if len(item1) >  0:
                    data_dict[column_name].append(item1)
                    temp_list = row[1].index.tolist()
                    temp_list.remove(column_name)
                    for column in temp_list:
                        data_dict[column].append(row[1][column])
    return pd.DataFrame(data_dict)


def convert_vc(dataframe, header, column_name='version_control'):
    data_dict = {item: [] for item in dataframe.columns.tolist()}
    for row in dataframe.iterrows():
        if isinstance(row[1][column_name], str) or not math.isnan(row[1][column_name]):
            for item1 in re.split(';|,', row[1][column_name].strip()):
                for key, value in get_header_item(header, column_name).items():
                    if isinstance(value, list) and item1.strip() in value:
                        item1 = key
                        break
                data_dict[column_name].append(item1)
                temp_list = row[1].index.tolist()
                temp_list.remove(column_name)
                for column in temp_list:
                    data_dict[column].append(row[1][column])
    return pd.DataFrame(data_dict)


def convert_tech_experience(dataframe, header, column_name='technology_experience'):
    data_dict = {item: [] for item in dataframe.columns.tolist()}
    for row in dataframe.iterrows():
        if isinstance(row[1][column_name], str) or not math.isnan(row[1][column_name]):
            for item1 in re.split(';', row[1][column_name].strip()):
                for key, value in get_header_item(header, column_name).items():
                    if item1 == key:
                        item1 = value
                        break
                data_dict[column_name].append(item1)
                temp_list = row[1].index.tolist()
                temp_list.remove(column_name)
                for column in temp_list:
                    data_dict[column].append(row[1][column])
    return pd.DataFrame(data_dict)


def convert_open_ended(dataframe, header, file_name, column_name='security'):
    open_ended_data, codes = get_formatted_dataframe(file_name)
    previous_columns = dataframe.columns.tolist()
    target_columns = open_ended_data.columns.tolist()
    target_columns.remove('Answer')
    dataframe = pd.merge(dataframe, open_ended_data, left_on=column_name, right_on='Answer')
    dataframe = dataframe.drop(columns=['Answer', column_name])
    # dataframe = dataframe.rename(columns={item: item + "_" + column_name for item in target_columns})
    data_dict = {item: [] for item in previous_columns}
    previous_columns.remove(column_name)
    for row in dataframe.iterrows():
        for column in target_columns:
            if row[1][column]:
                data_dict[column_name].append(column)
                for previous_column_item in previous_columns:
                    data_dict[previous_column_item].append(row[1][previous_column_item])
    return pd.DataFrame(data_dict)

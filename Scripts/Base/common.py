# Created by Partha at 8/17/19
import json


def rename_header(dataframe):
    temp_headers = json.load(open("../Data/Headers.json", "r"))
    headers = {key: value['header'] for key, value in temp_headers.items()}
    dataframe.rename(columns=headers, inplace=True)

    return temp_headers


def get_question_from_header(header_name):
    temp_headers = json.load(open("../Data/Headers.json", "r"))
    reverse_map = dict()
    for item in temp_headers.items():
        reverse_map[item[1]['header']] = item[0]

    return reverse_map.get(header_name)

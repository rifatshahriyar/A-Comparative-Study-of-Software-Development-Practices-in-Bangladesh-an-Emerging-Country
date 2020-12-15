import pandas as pd
from Base.common import rename_header
import seaborn as sns
import numpy as np
from StatisticalTests.Column_Converter import *


def get_stats(dataframe, column1, column2, percentage=False, dump=False, only_max=False):
    table = pd.crosstab(dataframe[column1], dataframe[column2])

    table = round((table.T / table.sum(axis=1)).T * 100, 2) if percentage else table
    index_condition = True
    if only_max:
        table = pd.DataFrame([(row, column, table.loc[row, column]) for row, column in
                              zip(table.index.tolist(), table.idxmax(axis=1).tolist())],
                             columns=[column1, column2, "Count_Percentage"])
        index_condition = False

    if dump:
        table.to_csv("temp.csv", index=index_condition)
    return table


def text_report_pretty_print(data, column2, column1='current_role', bold=False, italic=False,format2=False):
    text = ""
    for item in data.iterrows():
        text += str(item[0] + 1) + ") " + str(item[1][column1]) + ": "
        if bold:
            text += "\\textbf{"
        if italic:
            text += "\\textit{"
        if format2:
            text += str(item[1][column2]) + " (" + str(int(item[1]['Count_Percentage']) if item[1]['Count_Percentage'] == int(item[1]['Count_Percentage']) else item[1]['Count_Percentage']) + "\\%) "
        else:
            text += str(item[1][column2]) + ", " + str(item[1]['Count_Percentage']) + "\\% "
        if bold:
            text += "} "
        if italic:
            text += "} "
    text = text.replace("&", "\&")
    print(text)

def short_word(text):
    text = text.strip()
    if len(text.split(" ")) >= 2:
        return ''.join([item[0] for item in text.lower().split(" ")]).upper()
    else:
        return text
def get_top_n(data, n=2,short=False):
    short_word_dictionary = dict()
    column_title = ['top1 (\\%)', 'top2 (\\%)', 'top3 (\\%)']
    temp = pd.DataFrame(data.columns.values[np.argsort(-data.values, axis=1)[:, :n]], index=data.index,
                        columns=column_title[:n])
    for item in temp.iterrows():
        for row_item in item[1].index.tolist():
            if short:
                short_word_dictionary[temp.loc[item[0], row_item]] = short_word(temp.loc[item[0], row_item])
            cell_text = ""
            cell_percentage = ""
            if short:
                cell_text = short_word(temp.loc[item[0], row_item]) if len(temp.loc[item[0], row_item]) > 0 else cell_text
            else:
                cell_text = temp.loc[item[0], row_item] if len(temp.loc[item[0], row_item]) > 0 else cell_text
            cell_percentage = " (" + str(data.loc[item[0], item[1][row_item]]) + ") " if len(cell_text) > 0 else cell_percentage

            temp.at[item[0], row_item] = cell_text + cell_percentage if data.loc[item[0], item[1][row_item]]>0 else ""

    return temp, short_word_dictionary


def table_report_pretty_print(data, short_word=False, all=False):
    if not all:
        data, sh_dictionary = get_top_n(data, 2,short=short_word)
        print(sh_dictionary)
    print(len(data.columns.tolist()))
    text = " & "

    for item in data.columns.tolist():
        text += item + " & "
    text = text[:-2] + "\\\\\n"
    for row in data.iterrows():
        text += row[0] + " & "
        for row_item in row[1].index.tolist():
            text += str(row[1][row_item]) + " & "
        text = text[:-2] + "\\\\\n"
    print(text)


if __name__ == '__main__':
    # Load Data #
    sns.set_context("paper")
    sns.set_palette("Set2")
    df = pd.read_csv("../Data/MainData.csv")
    temp_headers = rename_header(df)
    #print((convert_role(df, temp_headers)['current_role'].value_counts()/convert_role(df, temp_headers)['current_role'].count())*100)
    data = get_stats(convert_role(df, temp_headers), "current_role",
                     "professional_experience", percentage=True, dump=True, only_max=True)
    text_report_pretty_print(data, "professional_experience",bold=False,italic=False,format2=True)

    # data = get_stats(convert_role(convert_dev_method(df, temp_headers), temp_headers), "current_role",
    #                  "methodology", percentage=True, dump=True, only_max=True)
    # text_report_pretty_print(data, "methodology", bold=False, italic=False, format2=True)

    # data = get_stats(convert_role(convert_req_gather(df, temp_headers), temp_headers), "current_role",
    #                  "requirements_gathering", percentage=True, dump=True, only_max=True)
    # text_report_pretty_print(data, "requirements_gathering", bold=False, italic=False, format2=True)

    # data = get_stats(convert_role(convert_dev_activity(df, temp_headers), temp_headers), "current_role",
    #                  "most_spent_time", percentage=True, dump=True, only_max=True)
    # text_report_pretty_print(data, "most_spent_time", bold=False, italic=False, format2=True)

    # data = get_stats(convert_role(convert_tech_experience(df, temp_headers), temp_headers), "current_role",
    #                  "technology_experience", percentage=True, dump=True, only_max=True)
    # text_report_pretty_print(data, "technology_experience", bold=False, italic=False, format2=True)

    # data = get_stats(convert_role(convert_os(df, temp_headers), temp_headers), "current_role",
    #                  "operating_system", percentage=True, dump=True, only_max=True)
    # text_report_pretty_print(data, "operating_system", bold=False, italic=False, format2=True)

    # data = get_stats(convert_role(convert_language(df, temp_headers), temp_headers), "current_role",
    #                  "programming_language", percentage=True, dump=True, only_max=True)
    # text_report_pretty_print(data, "programming_language", bold=False, italic=False, format2=True)

    # data = get_stats(convert_role(convert_framework(df, temp_headers), temp_headers), "current_role",
    #                  "framework", percentage=True, dump=True, only_max=True)
    # text_report_pretty_print(data, "framework", bold=False, italic=False, format2=True)

    # data = get_stats(convert_role(convert_test_type(df, temp_headers), temp_headers), "current_role",
    #                  "testing", percentage=True, dump=True, only_max=True)
    # text_report_pretty_print(data, "testing", bold=False, italic=False, format2=True)

    # data = get_stats(convert_role(df, temp_headers), "current_role",
    #                  "automated_testing", percentage=True, dump=True, only_max=True)
    # text_report_pretty_print(data, "automated_testing", bold=False, italic=False, format2=True)

    # data = get_stats(convert_role(convert_test_qa(df, temp_headers), temp_headers), "current_role",
    #                  "QA", percentage=True, dump=True, only_max=True)
    # text_report_pretty_print(data, "QA", bold=False, italic=False, format2=True)
    #
    # data = get_stats(convert_role(convert_cd(df, temp_headers), temp_headers), "current_role",
    #                  "CD", percentage=True, dump=True, only_max=True)
    # text_report_pretty_print(data, "CD", bold=False, italic=False, format2=True)


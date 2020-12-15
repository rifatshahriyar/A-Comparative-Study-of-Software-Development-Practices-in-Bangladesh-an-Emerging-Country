import pandas as pd
from Base.common import rename_header
import seaborn as sns
import numpy as np
from StatisticalTests.Column_Converter import *
from StatisticalTests.Role_VS_All_STATS import get_stats, text_report_pretty_print, table_report_pretty_print

if __name__ == "__main__":
    sns.set_context("paper")
    sns.set_palette("Set2")
    df = pd.read_csv("../Data/MainData.csv")
    temp_headers = rename_header(df)

    data = get_stats(convert_size(df, temp_headers), "professional_experience",
                     "size", percentage=True, dump=True, only_max=True)
    text_report_pretty_print(data, column2="size", column1='professional_experience', bold=True, italic=True)


    data = get_stats(convert_size(convert_dev_method(df, temp_headers), temp_headers), "methodology",
                     "size", percentage=True, dump=True, only_max=True)
    text_report_pretty_print(data, column2="size", column1='methodology', bold=True, italic=True)

    data = get_stats(convert_size(convert_req_gather(df, temp_headers), temp_headers), "requirements_gathering",
                     "size", percentage=True, dump=True, only_max=True)
    text_report_pretty_print(data, column2="size", column1='requirements_gathering', bold=True, italic=True)

    data = get_stats(convert_size(convert_dev_activity(df, temp_headers), temp_headers), "most_spent_time",
                     "size", percentage=True, dump=True, only_max=True)
    text_report_pretty_print(data, column2="size", column1='most_spent_time', bold=True, italic=True)

    data = get_stats(convert_size(convert_tech_experience(df, temp_headers), temp_headers), "technology_experience",
                     "size", percentage=True, dump=True, only_max=True)
    text_report_pretty_print(data, column2="size", column1='technology_experience', bold=True, italic=True)

    data = get_stats(convert_size(convert_os(df, temp_headers), temp_headers), "operating_system",
                     "size", percentage=True, dump=True, only_max=True)
    text_report_pretty_print(data, column2="size", column1='operating_system', bold=True, italic=True)

    data = get_stats(convert_size(convert_language(df, temp_headers), temp_headers), "programming_language",
                     "size", percentage=True, dump=True, only_max=True)
    text_report_pretty_print(data, column2="size", column1='programming_language', bold=True, italic=True)

    data = get_stats(convert_size(convert_framework(df, temp_headers), temp_headers), "framework",
                     "size", percentage=True, dump=True, only_max=True)
    text_report_pretty_print(data, column2="size", column1='framework', bold=True, italic=True)

    data = get_stats(convert_size(convert_test_type(df, temp_headers), temp_headers), "testing",
                     "size", percentage=True, dump=True, only_max=True)
    text_report_pretty_print(data, column2="size", column1='testing', bold=True, italic=True)

    data = get_stats(convert_size(df, temp_headers), "automated_testing",
                     "size", percentage=True, dump=True, only_max=True)
    text_report_pretty_print(data, column2="size", column1='automated_testing', bold=True, italic=True)

    data = get_stats(convert_size(convert_test_qa(df, temp_headers), temp_headers), "QA",
                     "size", percentage=True, dump=True, only_max=True)
    text_report_pretty_print(data, column2="size", column1='QA', bold=True, italic=True)

    data = get_stats(convert_size(convert_cd(df, temp_headers), temp_headers), "CD",
                     "size", percentage=True, dump=True, only_max=True)
    text_report_pretty_print(data, column2="size", column1='CD', bold=True, italic=True)
    data = get_stats(convert_size(convert_open_ended(df, temp_headers, file_name="How_do_you_ensure_security_of_your_products__1.csv", column_name='security'), temp_headers), "security",
                     "size", percentage=True, dump=True, only_max=True)
    text_report_pretty_print(data, column2="size", column1='security', bold=True, italic=True)

    data = get_stats(convert_size(
        convert_open_ended(df, temp_headers, file_name="How_do_you_ensure_scalability_of_your_products__1.csv",
                           column_name='scalability'), temp_headers), "scalability",
        "size", percentage=True, dump=True, only_max=True)
    text_report_pretty_print(data, column2="size", column1='scalability', bold=True, italic=True)

    data = get_stats(convert_size(
        convert_open_ended(df, temp_headers, file_name="How_do_you_maintain_performance_of_your_products__1.csv",
                           column_name='performance'), temp_headers), "performance",
        "size", percentage=True, dump=True, only_max=True)
    text_report_pretty_print(data, column2="size", column1='performance', bold=True, italic=True)

# Created by Partha at 2/1/20
import numpy as np
from matplotlib import pyplot as plt

from Base.common import get_question_from_header
from CodeSample.SampleGenerator import get_formatted_dataframe
from FigureGenerators.ManagerExpectationFigure import ManagerExpectationFigureController
from FigureGenerators.PerformanceFigure import PerformanceFigureController
from FigureGenerators.ScalabilityFigure import ScalabilityFigureController
import pandas as pd
if __name__ == "__main__":
    column_name = "performance"
    question_file_name = get_question_from_header(column_name).rstrip()[:-1].rstrip().replace(" ", "_") + "__1.csv"
    dataframe, unique_codes = get_formatted_dataframe(question_file_name)
    perf_controller = PerformanceFigureController(dataframe)
    #perf_controller.process_data(unique_codes=unique_codes, exclude_data=['Did not responded', 'Nothing'])

    column_name = "scalability"
    question_file_name = get_question_from_header(column_name).rstrip()[:-1].rstrip().replace(" ", "_") + "__1.csv"
    dataframe, unique_codes = get_formatted_dataframe(question_file_name)
    sc_controller = ScalabilityFigureController(dataframe)
    #sc_controller.process_data(unique_codes=unique_codes, exclude_data=['Did not responded', 'Nothing'])
    merge = {
        "Efficient design and implementation": "Efficient designing",
        "Using cloud services": "Upgraded infrastructure",
        "Following design patterns": "Efficient designing",
        "Load testing": "Testing",
        "Emphasizing on architecture": "Efficient designing",
        'Did not responded': 'Did not responded',
        'Nothing': 'Nothing'
    }
    new_column_count = 0
    new_column_name = []
    temp = list(map(lambda x: x.lower(), merge.keys()))
    for column_name in sc_controller.dataframe.columns.tolist():
        if column_name.lower().strip() not in list(map(lambda x: x.lower(), merge.keys())) and column_name != 'Answer':
            new_column_count += 1
            new_column_name.append(column_name)
            perf_controller.dataframe[column_name] = False
        else:
            pass
    temp_dataframe = pd.DataFrame(data=[[False] * len(perf_controller.dataframe.columns.tolist())]*len(sc_controller.dataframe),columns=perf_controller.dataframe.columns.tolist())
    temp_dataframe = pd.concat([perf_controller.dataframe,temp_dataframe])
    for row in sc_controller.dataframe.iterrows():
        temp_dataframe.iat[row[0] + len(perf_controller.dataframe), 0] = row[1]['Answer']
        for column_name in sc_controller.dataframe.columns.tolist():
            if column_name != 'Answer':
                if column_name.lower() not in list(map(lambda x: x.lower(), merge.keys())):
                    target_id = perf_controller.dataframe.columns.tolist().index(column_name)
                else:
                    target_id = list(map(lambda x: x.lower(), perf_controller.dataframe.columns.tolist())).index(merge[column_name.capitalize()].lower())
                temp_dataframe.iat[row[0] + len(perf_controller.dataframe), target_id] = row[1][column_name]

    perf_controller.set_dataframe(temp_dataframe.reset_index(drop=True))
    perf_controller.directory_name = "PerformanceScalability.eps"
    unique_codes = temp_dataframe.columns.tolist()
    unique_codes.remove('Did not responded')
    unique_codes.remove('Nothing')
    unique_codes.remove('Answer')
    perf_controller.process_data(unique_codes=unique_codes, exclude_data=['Did not responded', 'Nothing'])
    group = {
        "Peer Review": ["User Feedback", "Code review"],
        "Software Design": ["Efficient designing", "Using better codes/practices"],
        "Framework/Platform/Tools": ["Upgraded infrastructure", "Performance monitoring tools", "Caching techonology",
                                     "Load balancing", "Using sdk/framework", "Container technology"],
        "Software Testing": ["Testing"],
        "Database Design": ["Database optimization"]
    }
    temp = {key: 0 for key in group.keys()}
    for key, value in perf_controller.plot_data.items():
        flag = True
        for group_key, group_value in group.items():
            if key.lower() in list(map(lambda x: x.lower(), group_value)):
                temp[group_key] += value
                flag = False
                break
        if flag:
            print(key)

    print(perf_controller.plot_data.items())
    print({k: v for k, v in sorted(temp.items(), key=lambda item: item[1], reverse=True)})

    perf_controller.draw_figure(save=True)

import pandas as pd
import numpy as np
from Base.common import rename_header
from Base.FigureController import Controller
import math


class FigureController(Controller):
    xlabel = ""
    ylabel = "Percentage of Respondents (%)"
    directory_name = "Respondents_frameworks.eps"
    question = "Which frameworks are you using?"
    quest_header = "framework"

    def process_data(self, **kwargs):
        data = list()
        for item in self.dataframe[self.quest_header]:
            if isinstance(item, float) and math.isnan(item):
                data.append('Not Disclosed')
            else:
                for i in item.split(';'):
                    data.extend(i.split(', '))

        for key, value in kwargs.get(self.question).items():
            if isinstance(value, list):
                data = [key if d in value else d for d in data if d]

        unique_values = np.unique(np.array(data))
        print(unique_values)
        plot_data = dict()

        for item in unique_values:
            plot_data[item] = 0

        if 'Not Disclosed' in plot_data.keys():
            plot_data.pop('Not Disclosed')
            plot_data['Not Disclosed'] = 0

        for item in data:
            if isinstance(item, float) and math.isnan(item):
                plot_data['Not Disclosed'] += 1
            else:
                plot_data[item] += 1

        self.plot_data = plot_data


if __name__ == '__main__':
    # Load Data #
    df = pd.read_csv("../Data/MainData.csv")
    temp_headers = rename_header(df)
    controller = FigureController(df)
    controller.process_data(**temp_headers)
    controller.draw_figure_bar_vertically(save=True, exclude_fields=["Not Disclosed"])

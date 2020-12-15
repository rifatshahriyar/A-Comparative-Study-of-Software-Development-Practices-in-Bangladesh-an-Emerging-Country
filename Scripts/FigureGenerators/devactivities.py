import pandas as pd
import numpy as np
from Base.common import rename_header
from Base.FigureController import Controller
import math


class FigureController(Controller):
    xlabel = "Percentage of Respondents (%)"
    ylabel = ""
    directory_name = "Respondents_Activities.eps"
    question = "On which software development activities, do you spend most of the time? "
    quest_header = 'most_spent_time'

    def process_data(self, **kwargs):
        data = list()
        for item in self.dataframe[self.quest_header]:
            if isinstance(item, float) and math.isnan(item):
                data.append('Not Disclosed')
            else:
                data.extend(item.split(';'))

        for key, value in kwargs.get(self.question).items():
            data = [value if d == key else d for d in data]

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
    controller.draw_figure_bar_horizontally(save=True, exclude_fields=["Not Disclosed"])

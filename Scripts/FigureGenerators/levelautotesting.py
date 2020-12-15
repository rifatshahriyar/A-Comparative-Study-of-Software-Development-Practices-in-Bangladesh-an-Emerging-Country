import pandas as pd
import json
import numpy as np
from Base.common import rename_header
from Base.FigureController import Controller
from matplotlib import pyplot as plt
import math


class FigureController(Controller):
    xlabel = "Respondents (%)"
    ylabel = "Level"
    directory_name = "Respondents_autotest_level.eps"
    question = "What is the level of automated testing in your projects?"
    quest_header = "automated_testing"

    def process_data(self, **kwargs):
        unique_values = sorted(self.dataframe[self.quest_header].unique().tolist())
        unique_values = [item if math.isnan(item) else int(item) for item in unique_values]
        print(unique_values)
        plot_data = dict()

        for item in unique_values:
            if math.isnan(item):
                plot_data['Not Disclosed'] = 0
            else:
                plot_data[item] = 0

        if 'Not Disclosed' in plot_data.keys():
            plot_data.pop('Not Disclosed')
            plot_data['Not Disclosed'] = 0

        for item in self.dataframe[self.quest_header]:
            if isinstance(item,float) and math.isnan(item):
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

import pandas as pd
import json
import numpy as np
from Base.common import rename_header
from Base.FigureController import Controller
from matplotlib import pyplot as plt
import math


class RoleFigureController(Controller):
    xlabel = "Role"
    ylabel = "Frequency (%)"
    directory_name = "Respondents_Role.eps"
    question = "What is your current role?"
    quest_header = "current_role"

    def process_data(self, **kwargs):
        data = list()
        for item in self.dataframe[self.quest_header]:
            if isinstance(item, float) and math.isnan(item):
                data.append('Not Disclosed')
            else:
                data.extend(item.split(';'))

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
            if isinstance(item,float) and math.isnan(item):
                plot_data['Not Disclosed'] += 1
            else:
                plot_data[item] += 1

        self.plot_data = plot_data

    def draw_figure(self, save=False, legend=False, **kwargs):
        objects = self.plot_data.keys()
        role = np.arange(len(objects))
        role_frequency = self.plot_data.values()
        role_frequency = [af * 100 / self.num_of_respondents for af in role_frequency]

        plt.bar(role, role_frequency, align='center', alpha=0.02)
        plt.xticks(role, objects)
        plt.xticks(rotation=90)

        super(RoleFigureController, self).draw_figure(save=save)


if __name__ == '__main__':
    # Load Data #
    df = pd.read_csv("../Data/MainData.csv")
    temp_headers = rename_header(df)
    controller = RoleFigureController(df)
    controller.process_data(**temp_headers)
    controller.draw_figure(save=True)

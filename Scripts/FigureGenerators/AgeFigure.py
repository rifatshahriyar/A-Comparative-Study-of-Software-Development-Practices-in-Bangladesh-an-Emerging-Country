# Created by Partha at 8/16/19
import pandas as pd
import json
import numpy as np
from Base.common import rename_header
from Base.FigureController import Controller
from matplotlib import pyplot as plt
import math


class AgeFigureController(Controller):
    xlabel = "Age"
    ylabel = "Frequency (%)"
    directory_name = "Respondents_Age.eps"

    def process_data(self, **kwargs):
        unique_values = sorted(self.dataframe['age'].unique().tolist())
        unique_values = [item if math.isnan(item) else int(item) for item in unique_values]
        plot_data = dict()

        for item in unique_values:
            if math.isnan(item):
                plot_data['Not Disclosed'] = 0
            else:
                plot_data[str(item)] = 0

        if 'Not Disclosed' in plot_data.keys():
            plot_data.pop('Not Disclosed')
            plot_data['Not Disclosed'] = 0

        for item in self.dataframe['age'].tolist():
            if math.isnan(item):
                plot_data['Not Disclosed'] += 1
            else:
                plot_data[str(int(item))] += 1

        self.plot_data = plot_data

    def draw_figure(self, save=False, legend=False, **kwargs):
        objects = self.plot_data.keys()
        age = np.arange(len(objects))
        age_frequency = self.plot_data.values()
        age_frequency = [af * 100 / self.num_of_respondents for af in age_frequency]

        plt.bar(age, age_frequency, align='center', alpha=0.5)
        plt.xticks(age, objects)
        plt.xticks(rotation=90)

        super(AgeFigureController, self).draw_figure(save=save)


if __name__ == '__main__':
    # Load Data #
    df = pd.read_csv("../Data/MainData.csv")
    rename_header(df)
    controller = AgeFigureController(df)
    controller.process_data()
    controller.draw_figure(save=True)

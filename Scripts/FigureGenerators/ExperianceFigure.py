# Created by Partha at 8/16/19
import pandas as pd
import json
import numpy as np
from Base.common import rename_header
from Base.FigureController import Controller
from matplotlib import pyplot as plt, ticker
import math


class AgeFigureController(Controller):
    xlabel = "Professional Experience"
    ylabel = "Frequency (%)"
    directory_name = "Respondents_Experience.eps"

    def process_data(self, **kwargs):
        unique_values = self.dataframe['professional_experience'].unique().tolist()
        unique_values = ['Not Disclosed' if isinstance(item, float) and math.isnan(item) else item for item in unique_values]
        #unique_values = sorted(temp)
        plot_data = dict()

        for item in unique_values:
            if isinstance(item,float) and math.isnan(item):
                plot_data['Not Disclosed'] = 0
            else:
                plot_data[item] = 0

        if 'Not Disclosed' in plot_data.keys():
            plot_data.pop('Not Disclosed')
            plot_data['Not Disclosed'] = 0

        for item in self.dataframe['professional_experience'].tolist():
            if isinstance(item,float) and math.isnan(item):
                plot_data['Not Disclosed'] += 1
            else:
                plot_data[item] += 1

        self.plot_data = plot_data

    def draw_figure(self, save=False, **kwargs):
        objects = self.plot_data.keys()
        age = np.arange(len(objects))
        age_frequency = self.plot_data.values()
        age_frequency = [af * 100 / self.num_of_respondents for af in age_frequency]

        plt.bar(age, age_frequency, width=0.5, align='center', alpha=0.5)
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

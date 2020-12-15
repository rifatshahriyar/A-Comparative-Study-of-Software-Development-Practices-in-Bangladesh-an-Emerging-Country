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
    ylabel = "Frequency"
    directory_name = "Respondents_Age_Sex.eps"

    def process_data(self, **kwargs):
        unique_values = sorted(self.dataframe['age'].unique().tolist())
        unique_values = [item if math.isnan(item) else int(item) for item in unique_values]
        plot_data_male = dict()
        plot_data_female = dict()

        for item in unique_values:
            if math.isnan(item):
                plot_data_male['Not Disclosed'] = 0
                plot_data_female['Not Disclosed'] = 0
            else:
                plot_data_male[str(item)] = 0
                plot_data_female[str(item)] = 0

        if 'Not Disclosed' in plot_data_male.keys():
            plot_data_male.pop('Not Disclosed')
            plot_data_male['Not Disclosed'] = 0
        if 'Not Disclosed' in plot_data_female.keys():
            plot_data_female.pop('Not Disclosed')
            plot_data_female['Not Disclosed'] = 0

        for item in self.dataframe[['age', 'gender']].iterrows():
            if math.isnan(item[1]['age']):
                if item[1]['gender'] == 'Male':
                    plot_data_male['Not Disclosed'] += 1
                else:
                    plot_data_female['Not Disclosed'] += 1
            else:
                if item[1]['gender'] == 'Male':
                    plot_data_male[str(int(item[1]['age']))] += 1
                else:
                    plot_data_female[str(int(item[1]['age']))] += 1

        self.plot_data_male = plot_data_male
        self.plot_data_female = plot_data_female

    def draw_figure(self, save=False,legend=False, **kwargs):
        width = 0.85
        objects = self.plot_data_male.keys()
        y_pos = np.arange(len(objects)) * 2
        male_age = self.plot_data_male.values()
        plt.bar(y_pos, male_age, width=width, align='center', alpha=0.5, label='Male')

        female_age = self.plot_data_female.values()
        plt.bar(y_pos + width, female_age, width=width, align='center', alpha=0.5, label='Female')

        y_pos = y_pos + width / 2

        plt.xticks(y_pos, objects)
        plt.xticks(rotation=90)

        super(AgeFigureController, self).draw_figure(save=save)


if __name__ == '__main__':
    # Load Data #
    df = pd.read_csv("../Data/MainData.csv")
    rename_header(df)
    controller = AgeFigureController(df)
    controller.process_data()
    controller.draw_figure(save=True, legend=True)

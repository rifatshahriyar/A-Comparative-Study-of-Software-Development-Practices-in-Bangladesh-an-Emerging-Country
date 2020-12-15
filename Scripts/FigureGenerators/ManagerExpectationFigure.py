# Created by Partha at 1/31/20

import numpy as np
from matplotlib import pyplot as plt

from Base.FigureController import Controller
from Base.common import get_question_from_header
from CodeSample.SampleGenerator import get_formatted_dataframe
import pandas as pd

class ManagerExpectationFigureController(Controller):
    ylabel = ""
    xlabel = "Percentage of Respondents(%)"
    directory_name = "Managers_Expectation.eps"
    figure_height = 10
    figure_width = 5
    x_tick_size = 20
    y_tick_size = 20
    axis_title_size = 20

    @staticmethod
    def conditional_replace(text, min_word_length=3):
        words = text.split(" ")
        replacers = []
        for word in words:
            if len(word) <= min_word_length:
                replacers.append(" ")
            else:
                replacers.append("\n")
        temp = ""
        for word, replacer in zip(words, replacers):
            temp += word + replacer
        return temp

    def process_data(self, **kwargs):
        unique_values = kwargs['unique_codes']
        plot_data = dict()
        if 'exclude_data' in kwargs:
            unique_values = [x for x in unique_values if x not in kwargs['exclude_data']]
            temp = pd.Series(data=[False]*len(self.dataframe))
            for item in kwargs['exclude_data']:
                temp = temp | self.dataframe[item]
            total = len(self.dataframe) - temp.sum()
        else:
            total = len(self.dataframe)
        for item in unique_values:
            plot_data[str(item)] = round(
                len(self.dataframe[getattr(self.dataframe, item) == True]) / total * 100, 2)

        for key in list(plot_data.keys()):
            temp = plot_data[key]
            plot_data.pop(key)
            plot_data[key.strip().lower().capitalize()] = temp
        plot_data = {k: v for k, v in sorted(plot_data.items(), key=lambda item: item[1], reverse=False)}
        self.plot_data = plot_data

    def draw_figure(self, save=False, legend=False, **kwargs):

        objects = self.plot_data.keys()
        data_object = np.arange(len(objects))
        frequency = self.plot_data.values()
        plt.barh(data_object, frequency, align='center', alpha=0.5, height=kwargs.get('height', 0.35))
        plt.yticks(data_object, objects)
        # plt.yticks(rotation=90)
        super(ManagerExpectationFigureController, self).draw_figure(save=save)


if __name__ == "__main__":
    column_name = "manager_expectation"
    question_file_name = get_question_from_header(column_name).rstrip()[:-1].rstrip().replace(" ", "_") + "__1.csv"
    dataframe, unique_codes = get_formatted_dataframe(question_file_name)
    controller = ManagerExpectationFigureController(dataframe)
    controller.process_data(unique_codes=unique_codes, exclude_data=['Did not responded', 'Nothing'])
    controller.draw_figure(save=True, height=0.3)

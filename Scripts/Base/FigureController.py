# Created by Partha at 8/17/19
from matplotlib import pyplot as plt
from matplotlib import rcParams
import seaborn as sns
import numpy as np


class Controller(object):
    xlabel = None
    ylabel = None
    x_tick_size = 30
    y_tick_size = 30
    title = None
    directory_name = None
    axis_title_size = 30
    title_size = 20
    prop_size = 25
    extension = 'eps'
    palette = "Set2"
    figure_height = 20
    figure_width = 10
    num_of_respondents = 136
    plot_data = None

    # palettes = ["deep", "muted", "pastel", "bright", "dark", "colorblind"]

    def __init__(self, dataframe):
        self.dataframe = dataframe
        self.root = "../Figures/"
        rcParams.update({'figure.autolayout': True})
        sns.set_palette(self.palette)
        sns.set_context("paper")
        plt.figure(figsize=(self.figure_height, self.figure_width))
        plt.xticks(fontsize=self.x_tick_size)
        plt.yticks(fontsize=self.y_tick_size)

    def set_dataframe(self, new_dataframe):
        self.dataframe = new_dataframe

    def process_data(self, **kwargs):
        pass

    @staticmethod
    def formatted_response_percentages(options_list, frequency_list):
        response_percentage = ''
        for i in range(1, len(options_list) + 1):
            response_percentage += '{}) {} {}\\%, '.format(i, options_list[i - 1], round(frequency_list[i - 1], 2))

        response_percentage = response_percentage[:-2] if response_percentage else response_percentage

        return response_percentage

    def draw_figure(self, save=False, legend=False,**kwargs):
        if self.xlabel is None:
            print("Attention !!! xlabel not set")
            return
        else:
            plt.xlabel(self.xlabel, fontsize=self.axis_title_size)
        if self.ylabel is None:
            print("Attention !!! ylabel not set")
            return
        else:
            plt.ylabel(self.ylabel, fontsize=self.axis_title_size)

        plt.autoscale(True)
        if legend:
            plt.legend(loc='upper left', prop={'size': self.prop_size})

        if self.title is not None:
            plt.title(self.title, fontsize=self.title_size)
        if save:
            if self.directory_name is None:
                print("Attention !!! directory name not set")
            else:
                plt.savefig(self.root + self.directory_name, format=self.extension, dpi=5000)
        else:
            plt.show()

    def draw_figure_bar_horizontally(self, save=False, legend=False, **kwargs):
        alpha = kwargs.get('alpha', 0.5)
        height = kwargs.get('height', 0.35)
        align = kwargs.get('align', 'center')
        if 'exclude_fields' in kwargs:
            for data in kwargs['exclude_fields']:
                del self.plot_data[data]

        self.plot_data = {k: v for k, v in sorted(self.plot_data.items(), key=lambda item: item[1])}
        objects = self.plot_data.keys()
        data_objects = np.arange(len(objects))
        frequency = self.plot_data.values()
        frequency = [rf * 100 / self.num_of_respondents for rf in frequency]

        print(self.formatted_response_percentages(list(objects), frequency))

        plt.barh(data_objects, frequency, align=align, alpha=alpha, height=height)
        plt.yticks(data_objects, objects)

        self.draw_figure(save=save)

    def draw_figure_bar_vertically(self, save=False, legend=False, **kwargs):
        alpha = kwargs.get('alpha', 0.5)
        align = kwargs.get('align', 'center')
        width = kwargs.get('width', 0.35)
        if 'exclude_fields' in kwargs:
            for field in kwargs['exclude_fields']:
                del self.plot_data[field]

        self.plot_data = {k: v for k, v in sorted(self.plot_data.items(), key=lambda item: item[1])}
        objects = self.plot_data.keys()
        data_objects = np.arange(len(objects))
        frequency = self.plot_data.values()
        frequency = [af * 100 / self.num_of_respondents for af in frequency]

        print(self.formatted_response_percentages(list(objects), frequency))

        plt.bar(data_objects, frequency, align=align, alpha=alpha, width=width)
        plt.xticks(data_objects, objects)
        plt.xticks(rotation=90)

        self.draw_figure(save=save)

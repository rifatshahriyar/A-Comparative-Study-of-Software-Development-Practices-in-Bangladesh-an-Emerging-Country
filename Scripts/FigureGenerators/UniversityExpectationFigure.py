# Created by Partha at 2/1/20
import numpy as np
from matplotlib import pyplot as plt

from Base.common import get_question_from_header
from CodeSample.SampleGenerator import get_formatted_dataframe
from FigureGenerators.ManagerExpectationFigure import ManagerExpectationFigureController


class CandidateExpectationFigureController(ManagerExpectationFigureController):
    ylabel = ""
    xlabel = "Percentage of Respondents(%)"
    directory_name = "UniversityExpectation.eps"
    figure_height = 10
    figure_width = 5
    x_tick_size = 20
    y_tick_size = 20
    axis_title_size = 20


if __name__ == "__main__":
    column_name = "university_expectation"
    question_file_name = get_question_from_header(column_name).rstrip()[:-1].rstrip().replace(" ", "_") + "__1.csv"
    dataframe, unique_codes = get_formatted_dataframe(question_file_name)
    controller = CandidateExpectationFigureController(dataframe)
    controller.process_data(unique_codes=unique_codes, exclude_data=['Did not responded','Nothing'])
    controller.draw_figure(save=True, height=0.2)

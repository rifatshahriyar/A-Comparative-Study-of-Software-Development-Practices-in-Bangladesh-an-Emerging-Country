# Created by Partha at 1/31/20

import numpy as np
from matplotlib import pyplot as plt

from Base.common import get_question_from_header
from CodeSample.SampleGenerator import get_formatted_dataframe
from FigureGenerators.ManagerExpectationFigure import ManagerExpectationFigureController


class RDInvolvementFigureController(ManagerExpectationFigureController):
    xlabel = "R&D Involvement"
    ylabel = "Frequency"
    directory_name = "RD_Involvement.eps"


if __name__ == "__main__":
    column_name = "RD_involvement"
    question_file_name = get_question_from_header(column_name).rstrip()[:-1].rstrip().replace(" ", "_") + "__1.csv"
    dataframe, unique_codes = get_formatted_dataframe(question_file_name)
    controller = RDInvolvementFigureController(dataframe)
    controller.process_data(unique_codes=unique_codes, handle_not_responded=False)
    controller.draw_figure(save=True)

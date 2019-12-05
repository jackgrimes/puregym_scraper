import datetime
import os

import pandas as pd
from pandas.plotting import register_matplotlib_converters

from configs import PATHS
from utils.plot_utils import plot_time_per_visit, plot_time_per_week, plot_durations_histogram
from utils.scrape_utils import get_paths

register_matplotlib_converters()

if __name__ == "__main__":

    DATA_PATH = get_paths(PATHS)

    durations = pd.read_csv(
        os.path.join(os.path.join(DATA_PATH, "data_durations"), "durations.csv")
    )
    durations["date"] = pd.to_datetime(durations["date"], format="%Y-%m-%d")

    time_str = datetime.datetime.now().strftime("%Y_%m_%d__%H_%M_%S")

    plot_time_per_visit(durations, DATA_PATH, time_str)

    plot_time_per_week(durations, DATA_PATH, time_str)

    plot_durations_histogram(durations, DATA_PATH, time_str)


import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np


def draw_plot():
    # Import data
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # First line of best fit (1880 - latest year)
    res = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    x_pred = np.arange(1880, 2051)
    y_pred = res.slope * x_pred + res.intercept
    ax.plot(x_pred, y_pred, color="red")

    # Second line of best fit (2000 - latest year)
    df_recent = df[df["Year"] >= 2000]
    res_recent = linregress(
        df_recent["Year"],
        df_recent["CSIRO Adjusted Sea Level"]
    )

    x_recent = np.arange(2000, 2051)
    y_recent = res_recent.slope * x_recent + res_recent.intercept
    ax.plot(x_recent, y_recent, color="green")

    # Labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")

    # Do not modify the next two lines
    fig.savefig("sea_level_plot.png")
    return plt.gca()

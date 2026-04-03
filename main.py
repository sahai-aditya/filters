import matplotlib.pyplot as plt
import numpy, math

from DataGenerator import *


def display_graph(data, time, properties):
    """
    data is a list of dictionaries where each dictionary has legend, color and y values corresponding to time.
    properties is a dictionary containing properties like title and x, y labels.
    """
    for graph_dict in data:
        plt.plot(
            time,
            graph_dict["data"],
            label=graph_dict["label"],
            color=graph_dict["color"],
            linestyle=graph_dict["line-type"]
        )

    plt.title(properties["title"])
    plt.xlabel(properties["x-label"])
    plt.ylabel(properties["y-label"])
    plt.legend()
    plt.show()

noisy_sin = get_noisy_sin(2, 1)

# ------------------------------------------------------------------------------
# MOVING PASS FILTER
moving_pass = []
moving_pass_filtered = []

for y in noisy_sin[0]:
    i = len(moving_pass_filtered)
    if i < 10:
        moving_pass.append(y)

        if i == 0:
            moving_pass_filtered.append(y)
            continue
        
        yf = (i * moving_pass_filtered[-1] + y) / (i + 1)
        moving_pass_filtered.append(yf)
        continue

    yf = moving_pass_filtered[-1] + (y - moving_pass[0]) / 10
    moving_pass_filtered.append(yf)

    del moving_pass[0]
    moving_pass.append(y)


# ------------------------------------------------------------------------------ 
# LOW PASS FILTER
alpha = 0.61
low_pass_filtered = []

for y in noisy_sin[0]:
    if not low_pass_filtered:
        low_pass_filtered.append(y)
        continue

    yf = alpha * low_pass_filtered[-1] + (1 - alpha) * y
    low_pass_filtered.append(yf)

# ------------------------------------------------------------------------------ 


# ------------------------------------------------------------------------------ 

display_graph(
    data = [
        {
            "data": noisy_sin[0],
            "label": "raw-sin",
            "color": "blue",
            "line-type": "--"
        },
        {
            "data": low_pass_filtered,
            "label": "lpf",
            "color": "red",
            "line-type": "-"
        },
    ],
    time = noisy_sin[1],
    properties = {
        "title": f"First Order Low Pass Filter (alpha = {alpha})",
        "x-label": "Time (ms)",
        "y-label": "Sine"
    }
)
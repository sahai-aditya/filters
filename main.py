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
display_graph(
    data = [
        {
            "data": noisy_sin[0],
            "label": "raw-sin",
            "color": "blue",
            "line-type": "--"
        },
    ],
    time = noisy_sin[1],
    properties = {
        "title": "Noisy Sine Graph",
        "x-label": "Time (ms)",
        "y-label": "Sine"
    }
)
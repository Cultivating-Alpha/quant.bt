import numpy as np
from numba import njit


@njit(cache=True)
def print_bar(iteration, total, prev_percentage, length=40, fill="█"):
    percentage = iteration * 100 / total
    if percentage - prev_percentage >= 10:
        progress = iteration / float(total)
        filled_length = int(length * progress)
        bar = fill * filled_length + "-" * (length - filled_length)
        print(np.round(percentage), f"% | {bar} |")
        return percentage
    return prev_percentage

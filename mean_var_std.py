import numpy as np


def calculate(list):
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")

    # convertin liust -> numpy array
    np_arr = np.array(list)
    np_arr.resize(3, 3)

    calculations = {
        "mean": np.mean,
        "variance": np.var,
        "standard deviation": np.std,
        "max": np.max,
        "min": np.min,
        "sum": np.sum,
    }

    for key, func in calculations.items():
        calculations[key] = [
            func(np_arr, axis=0).tolist(),
            func(np_arr, axis=1).tolist(),
            func(np_arr),
        ]

    return calculations


calculate([0, 1, 2, 3, 4, 5, 6, 7, 8]).items()

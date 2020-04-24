import numpy as np
import pandas as pd
from random import shuffle


def load_data(file_path):
    df = pd.read_json(file_path)
    # df = shuffle(df)
    X = df["comment"]
    y = []
    for t in df["rating"]:
        if t < 5:
            y.append("bad")
        else:
            y.append("good")
    return np.array(X), np.array(y)
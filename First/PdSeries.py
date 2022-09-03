import pandas as pd
import random


def RandDataFrame():
    x = [[random.randint(0, 20) for _ in range(5)] for _ in range(5)]
    x1 = pd.DataFrame(x)
    print(x1)
    return x


if __name__ == "__main__":
    RandDataFrame()
    print("Hello!")

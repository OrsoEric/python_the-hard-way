import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def make_data():
    y_sin = math.cos( range( -math.pi, math.pi, 100 ))
    print(y_sin)

def test_show():
    ts = pd.Series(np.random.randn(1000), index=pd.date_range("1/1/2000", periods=1000))
    ts = ts.cumsum()
    ts.plot()
    plt.show()


def test_fig():
    #create an object i can set
    my_figure, my_axis = plt.subplot(figsize=(16,9),grid=True) 





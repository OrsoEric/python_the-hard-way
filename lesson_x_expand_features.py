## Kernel Trick

#----------------------------------------------------
# import
#----------------------------------------------------

import matplotlib.pyplot as plt
import seaborn as sns

import logging

#----------------------------------------------------
# 
#----------------------------------------------------

##  Data Synthesis
#
import numpy as np
def build_data(x_show = False):
    OFFSET = 0.5
    PERIOD = 3.0
    SLOPE = -3.0
    AMPLITUDE = 2.0
    WHITE_NOISE = 0.1
    TRUMPET = 0.1
    #time
    t = np.linspace(0, 10, 1000)
    
    y = OFFSET +((0.5+ TRUMPET* np.random.random(t.shape[0])) *SLOPE)*t +AMPLITUDE *np.sin( (t /PERIOD) *2.0 *np.pi) +np.random.random(t.shape[0])*WHITE_NOISE

    if (x_show == True):
        my_fig = plt.figure("Synth", figsize=(16,6))
        my_fig = sns.scatterplot(x=t, y=y) 

    X = t.reshape(-1,1)

    return X, y

#----------------------------------------------------
# 
#----------------------------------------------------

def xxx():
    return


#----------------------------------------------------
# regressor
#----------------------------------------------------

from sklearn.utils import shuffle
from sklearn.model_selection import cross_val_predict
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
def exe_regressor_kernel( X, y, i_n_degree=2 ):
    #shuffle imputs
    Xs, ys = shuffle( X, y )
    #Build a new square feature
    my_kernel = PolynomialFeatures(degree=i_n_degree).fit(Xs)
    Xk = my_kernel.transform(Xs)

    y_pred = cross_val_predict( LinearRegression(), Xk, ys )

    return Xs, ys, y_pred

#----------------------------------------------------
# show
#----------------------------------------------------

def show( figure, x, y, y_pred, source_color="Black" ):
    x_plot = x[:,0]
    figure = sns.scatterplot(x = x_plot, y=y, marker="+", color=source_color) 
    figure = sns.scatterplot(x = x_plot, y=y_pred, marker=".", color=source_color) 

#----------------------------------------------------
# 
#----------------------------------------------------

def xxx():
    return

#----------------------------------------------------
# Main
#----------------------------------------------------

def main():

    X, y = build_data()

    Xs, ys, y_pred = exe_regressor_kernel( X, y, 6 )
    
    my_fig = plt.figure("Synth", figsize=(16,6))
    show( my_fig, Xs, ys, y_pred )

    plt.show()

    return


## if the file is being read WITH the intent of being executed
if __name__ == '__main__':
    logging.basicConfig(
        #level of debug to show
        level=logging.INFO,
        #header of the debug message
        format='[%(asctime)s] %(levelname)s: %(message)s',
    )
    main()
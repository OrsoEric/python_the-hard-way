import matplotlib.pyplot as plt
import seaborn as sns

import logging

##
#
import numpy as np
def build_data(x_show = False):
    OFFSET = 0.5
    PERIOD = 3.0
    SLOPE = -1.0
    AMPLITUDE = 2.0
    WHITE_NOISE = 1.1
    TRUMPET = 1.1
    #time
    t = np.linspace(0, 10, 1000)
    
    y = OFFSET +((0.5+ TRUMPET* np.random.random(t.shape[0])) *SLOPE)*t +AMPLITUDE *np.sin( (t /PERIOD) *2.0 *np.pi) +np.random.random(t.shape[0])*WHITE_NOISE

    if (x_show == True):
        my_fig = plt.figure("Synth", figsize=(16,6))
        my_fig = sns.scatterplot(x=t, y=y) 

    return t, y


from sklearn.model_selection import train_test_split
##
def extract_matrix( x,y ):
    X = x
    X = X.reshape(-1,1)
    #divide in training and validation
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size = 0.8 )
    logging.info(f"training: {X_train.shape} {y_train.shape}")
    logging.info(f"validation: {X_test.shape} {y_test.shape}")

    return X_train, X_test, y_train, y_test

#----------------------------------------------------
# regressor
#----------------------------------------------------

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
def exe_regressor( X_train, X_test, y_train, y_test ):
    my_regressor = LinearRegression()
    my_regressor.fit( X_train, y_train )
    y_pred_train = my_regressor.predict(X_train)
    y_pred_test = my_regressor.predict(X_test)


    logging.info(f"E2 Metric: {mean_squared_error(y_test, y_pred_test)}")
    logging.info(f"R2 Metric: {r2_score(y_test, y_pred_test)}")

    return y_pred_train, y_pred_test

#----------------------------------------------------
# TREE
#----------------------------------------------------
#   awesome

from sklearn.tree import DecisionTreeRegressor
##
def exe_regressor_tree( X_train, X_test, y_train, y_test ):
    my_regressor = DecisionTreeRegressor()
    my_regressor.fit( X_train, y_train )
    y_pred_train = my_regressor.predict(X_train)
    y_pred_test = my_regressor.predict(X_test)

    return y_pred_train, y_pred_test, my_regressor

#----------------------------------------------------
# TREE
#----------------------------------------------------
#   awesome

#uses 10Ks of classifiers to express confidence and vote
from sklearn.ensemble import RandomForestRegressor
##
def exe_regressor_tree2( X_train, X_test, y_train, y_test ):
    my_regressor = RandomForestRegressor()
    my_regressor.fit( X_train, y_train )
    y_pred_train = my_regressor.predict(X_train)
    y_pred_test = my_regressor.predict(X_test)

    return y_pred_train, y_pred_test, my_regressor

#----------------------------------------------------
# ???
#----------------------------------------------------

from sklearn.model_selection import cross_val_predict
from sklearn.utils import shuffle
def compute_cross_prediction( my_regressor, x, y ):
    x_shuff, y_shuff = shuffle( x, y )
    y_pred = cross_val_predict( my_regressor, x_shuff.reshape(-1,1), y_shuff )

    return x_shuff, y_shuff, y_pred

#----------------------------------------------------
# show
#----------------------------------------------------

def show( figure, x, y, y_pred, source_color="Black" ):
    #x_plot = x[:,0]
    x_plot = x
    figure = sns.scatterplot(x = x_plot, y=y, marker="+", color=source_color) 
    figure = sns.scatterplot(x = x_plot, y=y_pred, marker=".", color=source_color) 

def main():
    #synthetize data
    t, y = build_data(False)

    X_train, X_test, y_train, y_test = extract_matrix(t, y )
    
    #y_pred_train, y_pred_test, my_regressor = exe_regressor( X_train, X_test, y_train, y_test )
    #y_pred_train, y_pred_test, my_regressor = exe_regressor_tree( X_train, X_test, y_train, y_test )
    y_pred_train, y_pred_test, my_regressor = exe_regressor_tree2( X_train, X_test, y_train, y_test )

    xs, ys, ysp = compute_cross_prediction(my_regressor, t, y )

    #logging.info(f"{y_pred_train} {y_pred_test}")

    my_fig = plt.figure("Synth", figsize=(16,6))

    #show( my_fig, X_train, y_train, y_pred_train, "Blue")
    #show( my_fig, X_test, y_test, y_pred_test, "Violet")

    show( my_fig, xs, ys, ysp, "Violet")
    


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
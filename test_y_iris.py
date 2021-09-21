## Dummy dataset iris flower classification

#----------------------------------------------------
# IMPORT
#----------------------------------------------------

from pandas import DataFrame
from pandas import read_csv
import time
import logging as logging
import os

import matplotlib.pyplot as plt
import seaborn as sns

#----------------------------------------------------
# MAIN
#----------------------------------------------------

from sklearn import datasets
from sklearn.pipeline import make_pipeline

def my_loader( x_show = False ):
    my_set = datasets.load_iris()
    #logging.info(f">>>{my_set.keys()}<<<")
    X = my_set["data"]
    y = my_set["target"]
    logging.info(f" Features: {X} Class: {y}")

    #construct dataframe
    my_dataframe = DataFrame( my_set["data"], columns=my_set.feature_names)
    my_dataframe["class"] = [my_set.target_names[n] for n in my_set.target]
    logging.info(f" DataFrame: {my_dataframe}")
    
    logging.info(f"index {my_dataframe.columns}")

    if x_show == True:
        my_fig_train_a = plt.figure("DATA01", figsize=(10,6))
        my_fig_train_a = sns.scatterplot(data=my_dataframe, x=my_dataframe.columns[0], y=my_dataframe.columns[1], hue="class")
        my_fig_train_b = plt.figure("DATA23", figsize=(10,6))
        my_fig_train_b = sns.scatterplot(data=my_dataframe, x=my_dataframe.columns[2], y=my_dataframe.columns[3], hue="class")

    return my_dataframe

#----------------------------------------------------
# PCA
#----------------------------------------------------

"""
from sklearn.decomposition import PCA
from sklearn.preprocessing import MinMaxScaler
#
def compute_pca( source_matrix, num_components = 2, x_show = False  ):
    
    my_pca =PCA(n_components=num_components).fit_transform(source_matrix)
    my_pca = MinMaxScaler().fit_transform(my_pca)

    logging.info(f"{my_pca}")
    if x_show == True:
        #my_fig_train_a = plt.figure("PCA", figsize=(10,6))
        #my_fig_train_a = sns.scatterplot(data=my_pca, x=my_dataframe.columns[0], y=my_dataframe.columns[1], hue="class")
        pass

    return my_pca
"""

#----------------------------------------------------
# PCA
#----------------------------------------------------

from sklearn.model_selection import train_test_split
##
def extract_matrix( source_dataframe ):
    logging.info(f"Dataframe: {source_dataframe}")
    X = source_dataframe.iloc[:,:-1]
    y = source_dataframe["class"]
    #divide in training and validation
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size = 0.8 )
    logging.info(f"training: {X_train.shape} {y_train.shape}")
    logging.info(f"validation: {X_test.shape} {y_test.shape}")

    return X_train, X_test, y_train, y_test

#----------------------------------------------------
# 
#----------------------------------------------------

from sklearn.linear_model import LogisticRegression
##
def exe_classifier( X_train, X_test, y_train, y_test ):
    my_classifier = LogisticRegression( max_iter=10e3 )
    my_classifier.fit( X_train, y_train )
    y_predict_train = my_classifier.predict( X_train )

    y_predict_test = my_classifier.predict( X_test )

    return y_predict_train, y_predict_test

#----------------------------------------------------
# 
#----------------------------------------------------

from sklearn.pipeline import make_pipeline
from sklearn.ensemble import RandomForestClassifier
##
def classifier_forest():

    my_pipeline = make_pipeline()


    return


#----------------------------------------------------
# show confusion matrix as heatmap
#----------------------------------------------------

from sklearn.metrics import confusion_matrix
##
def show_confusion( y_train, y_pred_train, y_test, y_pred_test ):
    my_confusion_matrix_train = confusion_matrix(y_train, y_pred_train)
    my_fig_train = plt.figure("TRAIN", figsize=(10,6))
    my_fig_train = sns.heatmap(my_confusion_matrix_train, annot=True, fmt="d")
    my_fig_train.set_xlabel("Prediction")
    my_fig_train.set_ylabel("Ground Truth")

    my_confusion_matrix_test = confusion_matrix(y_test, y_pred_test)
    my_fig_test = plt.figure("VALIDATION", figsize=(10,6))
    my_fig_test = sns.heatmap(my_confusion_matrix_test, annot=True, fmt="d")
    my_fig_train.set_xlabel("Prediction")
    my_fig_train.set_ylabel("Ground Truth")

#----------------------------------------------------
# MAIN
#----------------------------------------------------

def main():

    #load the data
    my_dataframe = my_loader(False)
    plt.show()

    #apply PCA
    #compute_pca( my_dataframe, x_show=True)

    #separate training and validation
    X_train, X_test, y_train, y_test = extract_matrix(my_dataframe)

    y_pred_train, y_pred_test = exe_classifier( X_train, X_test, y_train, y_test )

    show_confusion( y_train, y_pred_train, y_test, y_pred_test )
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
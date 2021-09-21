##  classification
#   use a file with one row and one class
#   IRIS dataset is a typical example

    #----------------------------------------------------
    # IMPORT
    #----------------------------------------------------



import matplotlib.pyplot as plt
import seaborn as sns

import os

import logging

    #----------------------------------------------------
    # CSV
    #----------------------------------------------------

from pandas import read_csv
## open the CSV file
#
def open_csv( x_draw = False ):
    CONFIDENTIAL_DATA_FOLDER = 'data_files'
    #five clusters 
    CONFIDENTIAL_DATA_FILE = 'dummy1.csv'
    
    file_name = os.path.join(os.getcwd(), CONFIDENTIAL_DATA_FOLDER, CONFIDENTIAL_DATA_FILE)
    my_csv = read_csv(file_name, sep=',')

    if (x_draw == True):
        logging.info(f"open csv: {my_csv}")
        my_fig = plt.figure("CSV", figsize=(10,6))
        my_fig = sns.lineplot(x = my_csv["VALUE"], y=my_csv["CLASS"], hue=my_csv["CLASS"])
        plt.show()
    return my_csv

    #----------------------------------------------------
    # 
    #----------------------------------------------------
    # i have 1 feature
    # 

#create train and test
from sklearn.model_selection import train_test_split
#classifier
from sklearn.linear_model import LogisticRegression
#measure accuracy
from sklearn.metrics import accuracy_score
from sklearn.metrics import recall_score
from sklearn.metrics import confusion_matrix
##  from source data 
#
def exe_classifier( source ):

    #convenction. X is the feature matrix. as many row as the samples, as many columns as the features. I need a matrix SAMPLESxFEATURES
    X = source.VALUE.to_numpy()
    X.shape = (X.shape[0],1)
    #X.shape = (-1,1)
    #logging.info(f"{X} {X.shape}")

    #y is a vector with the training class
    y = source.CLASS.to_numpy()
    #logging.info(f"{y} {y.shape}")

    #split 80%-20% taking care classes are divided with this split
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size = 0.8 )
    logging.info(f"ratio features: {X_train.shape} {X_test.shape}")
    logging.info(f"ratio classes: {y_train.shape} {y_test.shape}")

    #create my classifier and fit the model
    my_classifier = LogisticRegression()
    my_classifier.fit( X_train, y_train )

    #try to predict the train data
    y_pred_train = my_classifier.predict(X_train)
    failed_prediction_train = sum(y_pred_train != y_train)
    logging.info(f"failed training predictions: {failed_prediction_train} of {y_pred_train.shape[0]} {1.0 -1*failed_prediction_train/y_pred_train.shape[0]}") 

    #try to predict the validationd data
    y_pred_test = my_classifier.predict(X_test)
    failed_prediction_test = sum(y_pred_test != y_test)
    logging.info(f"failed training validation: {failed_prediction_test} of {y_pred_test.shape[0]} {1.0 -1*failed_prediction_test/y_pred_test.shape[0]}") 

    logging.info(f"accuracy score training: {accuracy_score(y_pred_train, y_train)}")
    

    logging.info(f"validation: accuracy score (overall correct predictions): {accuracy_score(y_pred_test, y_test)}")
    logging.info(f"validation: recall score (ability to get all positives): {recall_score(y_pred_test, y_test)}")

    my_confusion_matrix_train = confusion_matrix(y_train, y_pred_train)
    my_fig_train = plt.figure("TRAIN", figsize=(10,6))
    my_fig_train = sns.heatmap(my_confusion_matrix_train, annot=True, fmt="d")

    my_confusion_matrix_test = confusion_matrix(y_test, y_pred_test)
    my_fig_test = plt.figure("VALIDATION", figsize=(10,6))
    my_fig_test = sns.heatmap(my_confusion_matrix_test, annot=True, fmt="d")
    plt.show()

    return



    #----------------------------------------------------
    # MAIN
    #----------------------------------------------------

def main():

    #open the csv and optionally show the data
    my_csv = open_csv(False)
    
    #try the classifier
    exe_classifier(my_csv)


    pass

## if the file is being read WITH the intent of being executed
if __name__ == '__main__':
    logging.basicConfig(
        #level of debug to show
        level=logging.INFO,
        #header of the debug message
        format='[%(asctime)s] %(levelname)s: %(message)s',
    )
    main()
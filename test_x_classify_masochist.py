## use PCA to remove the most useful columns

from pandas import DataFrame
from pandas import read_csv
import time
import logging as logging
import os

import matplotlib.pyplot as plt
import seaborn as sns

## open the CSV file
#
def open_csv():
    CONFIDENTIAL_DATA_FOLDER = 'confidential_datasets'
    #two clusters
    #CONFIDENTIAL_DATA_FILE = 'tset_H10_slip_noslip.csv'
    #five clusters 
    CONFIDENTIAL_DATA_FILE = '2021_05_21_tset_new_ref_H10_2.csv'
    
    file_name = os.path.join(os.getcwd(), CONFIDENTIAL_DATA_FOLDER, CONFIDENTIAL_DATA_FILE)
    my_csv = read_csv(file_name, sep=',')
    return my_csv


from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

##
def extract_matrix( source_csv ):

    PCA_AXES = 10
    PCA_DISCCARD = 2

    source_matrix = source_csv.iloc[:,:-2]

    my_pca =PCA(n_components=PCA_AXES).fit_transform(source_matrix)
    my_pca = MinMaxScaler().fit_transform(my_pca)
    my_masochist_pca = my_pca[:,PCA_DISCCARD:]
    logging.info(f"PCA: {my_pca.shape} {my_masochist_pca.shape}")
    #extract features inside a matrix
    X = my_masochist_pca

    #extract classes
    my_encoder = LabelEncoder().fit( source_csv.Name )
    y = my_encoder.transform( source_csv.Name )
    logging.info(f"shape of data: {X.shape} {y.shape}")

    #divide in training and validation
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size = 0.8 )
    logging.info(f"training: {X_train.shape} {y_train.shape}")
    logging.info(f"validation: {X_test.shape} {y_test.shape}")

    return X_train, X_test, y_train, y_test


from sklearn.linear_model import LogisticRegression
##
def exe_classifier( X_train, X_test, y_train, y_test ):
    my_classifier = LogisticRegression( max_iter=100e3 )
    my_classifier.fit(X_train, y_train )

    y_pred_train = my_classifier.predict(X_train)
    y_pred_test = my_classifier.predict(X_test)

    return y_pred_train, y_pred_test

from sklearn.metrics import confusion_matrix
##
def show_confusion( y_train, y_pred_train, y_test, y_pred_test ):
    my_confusion_matrix_train = confusion_matrix(y_train, y_pred_train)
    my_fig_train = plt.figure("TRAIN", figsize=(10,6))
    my_fig_train = sns.heatmap(my_confusion_matrix_train, annot=True, fmt="d")

    my_confusion_matrix_test = confusion_matrix(y_test, y_pred_test)
    my_fig_test = plt.figure("VALIDATION", figsize=(10,6))
    my_fig_test = sns.heatmap(my_confusion_matrix_test, annot=True, fmt="d")
    

def show( X_train, X_test, y_train, y_pred_train, y_test, y_pred_test  ):

    #construct DataFrame
    my_dataframe = DataFrame()

    my_dataframe["PCA0"] = X_train[:, 0]
    

    #my_fig = plt.figure("SCATTERPLOT", figsize=(10,6))
    #my_fig = sns.scatterplot(data=subset_dataframe, x='PCA0', y='PCA1', hue='Cluster',marker="+")
    print(X_train)
    print(y_pred_train)

    return

def main():
    #open the CSV file
    my_csv = open_csv()
    
    #----------------------------------------------------
    # train and execute a classifier on the data
    #----------------------------------------------------

    #extract training and validation from CSV
    X_train, X_test, y_train, y_test = extract_matrix(my_csv)

    y_pred_train, y_pred_test = exe_classifier(X_train, X_test, y_train, y_test) 

    #----------------------------------------------------
    # Show
    #----------------------------------------------------

    show_confusion( y_train, y_pred_train, y_test, y_pred_test )
    show(X_train, X_test, y_train, y_pred_train, y_test, y_pred_test)
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
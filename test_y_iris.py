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
#   With random forest
#----------------------------------------------------

from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.ensemble import RandomForestClassifier
##
def exe_classifier_forest( X_train, X_test, y_train, y_test ):

    my_pipeline = make_pipeline( StandardScaler(), RandomForestClassifier(n_estimators=20) )
    my_pipeline.fit( X_train, y_train )
    y_predict_train = my_pipeline.predict( X_train )

    y_predict_test = my_pipeline.predict( X_test )

    return y_predict_train, y_predict_test

#----------------------------------------------------
#   With random forest and grid search
#----------------------------------------------------

from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
##
def exe_classifier_forest_search( X_train, X_test, y_train, y_test ):
    #dictionary with the parameters to explore
    PARAMS = { "n_estimators" : [20, 40] }
    #build a pipeline. uses best model.score equivalent to accuracy
    my_pipeline = make_pipeline( StandardScaler(), GridSearchCV( RandomForestClassifier(), PARAMS) )
    my_pipeline.fit( X_train, y_train )
    y_predict_train = my_pipeline.predict( X_train )

    y_predict_test = my_pipeline.predict( X_test )

    return y_predict_train, y_predict_test

#----------------------------------------------------
#   Assembly the data into good and bad sets
#----------------------------------------------------

## Take all data, and assemble them into a dataframe for good, and a dataframe for bad
def split_good_bad( X_train, y_train, y_pred_train, X_test, y_test, y_pred_test ):

    #construct training DataFrame
    train_dataframe = DataFrame( X_train, columns=X_train.columns )
    train_dataframe["Truth"] = y_train
    train_dataframe["Prediction"] = y_pred_train
    train_dataframe["Model"] = "Training"
    #logging.info( train_dataframe )

    #construct validation DataFrame
    test_dataframe = DataFrame( X_test, columns=X_test.columns )
    test_dataframe["Truth"] = y_test
    test_dataframe["Prediction"] = y_pred_test
    test_dataframe["Model"] = "Validation"
    #logging.info(test_dataframe)

    #append the two dataframes to get a full dataframe
    full_dataframe = train_dataframe.append(test_dataframe)
    #logging.info(full_dataframe)

    result_good = full_dataframe[full_dataframe.Truth == full_dataframe.Prediction]
    logging.info(result_good)

    result_bad = full_dataframe[full_dataframe.Truth != full_dataframe.Prediction]
    logging.info(result_bad)

    return result_good, result_bad

#----------------------------------------------------
# show confusion matrix as heatmap
#----------------------------------------------------

from sklearn.metrics import confusion_matrix
##
def show_confusion( y_train, y_pred_train, y_test, y_pred_test ):

    #compute confusion matrix
    my_confusion_matrix_train = confusion_matrix(y_train, y_pred_train)
    my_confusion_matrix_test = confusion_matrix(y_test, y_pred_test)

    my_fig = plt.figure("Confusion Matrix", figsize=(16,6))
    ax_train = my_fig.add_subplot(121)
    ax_train.title.set_text('Train')
    
    #my_fig_train = plt.figure("TRAIN", figsize=(10,6))
    
    ax_train = sns.heatmap(my_confusion_matrix_train, annot=True, fmt="d")
    ax_train.set_xlabel("Prediction")
    ax_train.set_ylabel("Ground Truth")

    ax_validation = my_fig.add_subplot(122)
    ax_validation.title.set_text('Validation')
    #my_fig_test = plt.figure("VALIDATION", figsize=(10,6))
    ax_validation = sns.heatmap(my_confusion_matrix_test, annot=True, fmt="d")
    ax_validation.set_xlabel("Prediction")
    ax_validation.set_ylabel("Ground Truth")

#----------------------------------------------------
# show scatterplot
#----------------------------------------------------

def show( i_df_source_good : DataFrame(), i_df_source_bad : DataFrame() ):

    my_fig = plt.figure("SCATTERPLOT", figsize=(16,6))

    ax_01 = my_fig.add_subplot(121)
    #my_fig = plt.subplot(1, 2, 1)
    #my_fig.suptitle('Scatterplot 01')
    ax_01 = sns.scatterplot(data=i_df_source_good, x=i_df_source_good.columns[0], y=i_df_source_good.columns[1], hue="Truth",marker="+")
    ax_01 = sns.scatterplot(data=i_df_source_bad, x=i_df_source_bad.columns[0], y=i_df_source_bad.columns[1], hue="Truth",marker="o")

    ax_23 = my_fig.add_subplot(122)
    my_fig = plt.subplot(1, 2, 2)
    #my_fig.suptitle('Scatterplot 23')
    ax_23 = sns.scatterplot(data=i_df_source_good, x=i_df_source_good.columns[2], y=i_df_source_good.columns[3], hue="Truth",marker="+")
    ax_23 = sns.scatterplot(data=i_df_source_bad, x=i_df_source_bad.columns[2], y=i_df_source_bad.columns[3], hue="Truth",marker="o")

    return


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

    #y_pred_train, y_pred_test = exe_classifier( X_train, X_test, y_train, y_test )
    y_pred_train, y_pred_test = exe_classifier_forest( X_train, X_test, y_train, y_test )
    y_pred_train, y_pred_test = exe_classifier_forest_search( X_train, X_test, y_train, y_test )

    #find good and bad predictions
    dataframe_good, dataframe_bad = split_good_bad( X_train, y_train, y_pred_train, X_test, y_test, y_pred_test )

    #show confusion matricies for training and validation
    show_confusion( y_train, y_pred_train, y_test, y_pred_test )

    #show scatterplot
    show( dataframe_good, dataframe_bad )

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
## Logistic regression
#   sigmoid usually is able to separate probabilistically a set.
#   e.g. obesity. some light weight are obese (dwarf) some high weight are not obese (strong man)

##  loss function (y-yT) output of model minus expected output
#   split data into training (80% to 90%) validation (20% to 10%)
#   durint training minimize loss on training, then see loss on validation
#   choose structure of the model: e.g. forest classificator

##  overfitting
#   when loss of train is lowering and loss of validation is increasing this means overfitting
#   the model stopped learning the law and started memorizing the values

##   supervised: i know what the right answer should be (usually classification and regression)
#   unsupervised (clustering)
#   semi supervised

##  supervised
#   discriminative vs generative
#   lazy vs eager
#   e.g. support vector machine: expensive to compute line. cheap to test line against validation
#   e.g. classify with vote to nearest cases. cheap to train, very expensive, more expensive with size to test a new case

##  Kernel Trick
#   e.g. very short or very long movies are good
#   . .    X XX    X               . . . ... ..    .
#add a new axis. time, time^2. solves the XOR problem by adding a fake linear axi with square

##  unbalanced classes
#   all simple system stop working when classes arebalanced. most value are one class
#   e.g. prime number classificator doesn't work. a prime classifier that returns false, has 90% accuracy with enough set

##  Classified
#   True    |   False   |
#   Good        Bad     |   Validation True   
#   bad         Good    |   Validation False
#
#   How many predictions were correct between all prediction
#   Accuracy        = (Good True +Good False) / (Good True + Bad False +Good False +Bad True)
# 
#   Ability to detect ALL positives
#   Sensitivity     = Good True / (Good True + Bad False)
#   Recall          = Good True / (Good True + Bad False)
#
#   Ability to detect ALL negatives
#   Specificity     = Good False / (Good False + Bad True)
#
#   Amongst positive how many are really positives
#   Precision       = Good True / (Good True + False True)
#
#   e.g. with ebola, you want to detect all trues, even at the cost of misclassifyin falses as true. High sensitivity
#   Show confusion matrix

##  Types of regression
#   linear:     can use kernel to morph the inputs and find lines in this morphed space
#   logistic:   probability that something is calss a or b
#   symbolic:   not machine learning. computational/evolutionary intelligence
#   random forest
#   support vector

##  Clustering
#   centroid algorithm e.g. finds perfect example and who is around it
#   density algorithm e.g. finds close points (do not need number of classes)

##  Normalization
#   regressors have problems with differing order of magnitudes.
#   e.g weight in km height in nm
#   remove median and fix scale. do opposite with the result

##  Representation learning
#   PCA principal component analysis    : find axis that best represent the problem. e.g. do a 2d photo of a 3d object to represent what matters
#   LSA latent semantic analysis        : e.g. i have a list of documents and subject (one text 80% whales 20% ship). synthetize
#   Autoencoder                         : make a network that first reduce dimensions, then increase dimensions.
#                                       if reconstruction works, the smallest core has somewhat compressed the data
#   Word2Vec                            : assign a word a position in a space

##  Dimensionality reduction
#   recursive feature elimination
#   train -> try to remove a dimension -> performace degraded a lot? yes was useful, no, keep it out
#   care, maybe a smarter model would have used the feature and achieved higher performance

##
#   sklearn.cluster.FeatureAgglomeration

##  sklearn like an inefficient lego for machine learning, good to try thing
#C:\Program Files (x86)\Python\Scripts>
#pip3 install sklearn
from pandas.core.frame import DataFrame
from float_to_eng_string import float_to_eng_string
from time import perf_counter

##  sklearn modules:
#   transformer : preprocess data (not the same name of a ML model)
#       .fit()              : calculate parameters ans saves them on the object
#       .transform()        : use the parameters to transform the data
#       .fit_transform()    :
#   models      : make predictions
#       all of above
#       .fit                : train
#       .predict()          : make predictions
#       .fit_predict()      :
#   pipeline    : i can line the transform and models boxes and from outside they act as a single model
#       the last box must be a transformer
#
timestamp = perf_counter()
from sklearn.decomposition import PCA
print(f'took {float_to_eng_string(perf_counter() -timestamp)}s to import sklearn')

import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

import os

import logging

## open the CSV file
#
def open_csv():
    CONFIDENTIAL_DATA_FOLDER = 'confidential_datasets'
    #CONFIDENTIAL_DATA_FILE = 'tset_H10_slip_noslip.csv'
    CONFIDENTIAL_DATA_FILE = '2021_05_21_tset_new_ref_H10_2.csv'
    

    file_name = os.path.join(os.getcwd(), CONFIDENTIAL_DATA_FOLDER, CONFIDENTIAL_DATA_FILE)
    #this csv has an header, i should let the class parse it
    #my_csv = pd.read_csv(file_name, header=None, sep=',')
    my_csv = pd.read_csv(file_name, sep=',')
    return my_csv

##Preprocess the datafrae
def extract_matrix( source_csv ):
    
    #exclude first row
    #exclude the last two columns
    data_matrix=source_csv.iloc[1:,:-2].values.astype(float)
    #print(f"my_csv{xxx}")
    return data_matrix

from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
## Principal component analysis
def apply_pca( source_matrix ):

    #my_pca =  PCA(n_components=2)
    #my_pca.fit(source_matrix)
    #my_pca.transform(source_matrix)

    #Can be done in one line
    my_pca =PCA(n_components=2).fit_transform(source_matrix)
    #Normalize 0 1 all dimensions
    my_pca = MinMaxScaler().fit_transform(my_pca)

    print(f"data{my_pca}, {type(my_pca)}, {my_pca.size}, {my_pca.shape}")
    return my_pca

from sklearn.pipeline import make_pipeline
##  apply the tool as a pipeline
def pipelinizer( source_matrix ):
    #construct pipeline
    my_pipeline = make_pipeline( PCA(n_components=2), MinMaxScaler() )
    #try different scaler
    #my_pipeline = make_pipeline( PCA(n_components=2), StandardScaler() )
    #prescalind data changes the result
    #my_pipeline = make_pipeline( StandardScaler(), PCA(n_components=2), StandardScaler() )

    #from the outside it makes the fit->transform calls of all components
    my_result = my_pipeline.fit_transform(source_matrix)
    return my_result

##
def main():
    #exercise2_correlation()
    my_csv = open_csv()
    #logging.info(f"my_csv{my_csv}")
    print(my_csv)

    my_matrix = extract_matrix(my_csv)
    print(f"data{my_matrix}, {type(my_matrix)}, {my_matrix.size}, {my_matrix.shape}")
    
    #PCA is doing a linear combination of the source and is pouring out just two dimensions
    #data_pca = apply_pca(my_matrix)
    
    #process with 
    data_pca = pipelinizer(my_matrix)
    
    #plt.scatter(x=data_pca[:,0], y=data_pca[:,1])
    #plt.show()

    dataframe_pca = DataFrame(data_pca, columns=['PCA0','PCA1'])
    #dataframe_pca = DataFrame(data_pca, columns=[f"PCA{index for index in range(data_pca.shape[1])}"])
    #take from original csv the name column
    dataframe_pca['type'] = my_csv.iloc[:,161]
    #print using seaborn, using name as hue
    sns.scatterplot(data=dataframe_pca, x='PCA0', y='PCA1', hue='type')
    plt.show()

    print(dataframe_pca[dataframe_pca.Cluster ==1])

    pass

## if the file is being read WITH the intent of being executed
if __name__ == '__main__':
    logging.basicConfig(
        #level of debug to show
        level=logging.DEBUG,
        #header of the debug message
        format='[%(asctime)s] %(levelname)s: %(message)s',
    )
    main()
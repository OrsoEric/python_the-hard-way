#compared to lesson associate right color on scatterplot

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
    #two clusters
    #CONFIDENTIAL_DATA_FILE = 'tset_H10_slip_noslip.csv'
    #five clusters 
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
    data_matrix=source_csv.iloc[:,:-2].values.astype(float)
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


from sklearn.cluster import KMeans
##
def clusterize( source_pda, num_clusters ):
    my_km = KMeans(n_clusters=num_clusters)
    result = my_km.fit_predict(source_pda)
    return result

from sklearn.manifold import TSNE


## TSNE has a strong random component
def try_tsne(source):
    tsne_preprocess = TSNE(n_components=2)
    result = tsne_preprocess.fit_transform(source)
    return result

#something to do with scanning scores... one day try if it does something
from sklearn.metrics import silhouette_score
def try_clusterization( source ):
    for num_clusters in range(2,11):
        my_kmeans = make_pipeline(KMeans(n_clusters=num_clusters))
        labels = my_kmeans.fit(source)
        my_score = silhouette_score(source, labels)
        print(f"{my_score}")
        
    return

from sklearn.model_selection import GridSearchCV
##????????
def wut( source ):
    #this is to see what scoring asks for
    def my_score(*arg,**kwargs):
        #print(f"{arg}-{kwargs}")
        #sys.exit(10)
        pass

    xxx = GridSearchCV(KMeans(),{"n_clusters":range(2,11)}, scoring=my_score)
    yyy= xxx.fit(source)
    print("------------------------------------")
    print(yyy)
    return yyy





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
    
    print("------------------------------------")

    print(f"column names: {data_pca.shape} {[index for index in range(data_pca.shape[1])]}")
    #pri
    dataframe_pca = DataFrame(data_pca, columns=['PCA0','PCA1'])
    #dataframe_pca = DataFrame(data_pca, columns=['PCA0','PCA1','PCA2','PCA3','PCA4'])
    #dataframe_pca = DataFrame(data_pca, columns=[ [f"PCA{[index for index in range(data_pca.shape[1]+1)]}"] ])

    #TSNE has a random component
    #data_tsne = try_tsne(data_pca)
    #dataframe_pca = DataFrame(data_tsne, columns=['PCA0','PCA1'])

    #
    data_cluster = clusterize(data_pca, 6)
    print("------------------------------------")
    print(f"my_clusters {data_cluster} {data_cluster.shape}")

    #add cluster to data
    dataframe_pca["Cluster"] = data_cluster

    #take from original csv the name column
    #dataframe_pca['type'] = my_csv.iloc[:,161]
    dataframe_pca['type'] = my_csv.loc[:,"Name"]
    #print using seaborn, using name as hue
    #i'm builidng a palette as a dictionary
    my_palette = dict()
    for index, row in my_csv[["Name", "Color"]].iterrows():
        my_palette[row[0]] = row[1]
    print("------------------------------------")
    print(my_palette)

    #categorize based on color
    plt.figure(0)
    sns.scatterplot(data=dataframe_pca, x='PCA0', y='PCA1', hue='type', palette=my_palette)
    plt.figure(1)
    #categorize based on cluster found by 
    sns.scatterplot(data=dataframe_pca, x='PCA0', y='PCA1', hue='Cluster')
    plt.show()

    #
    #try_clusterization(data_pca)
    
    #?????
    wut(data_pca)

    #
    #print(dataframe_pca[dataframe_pca.Cluster ==1 and dataframe_pca.Type =="HDPE"])

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
## use dbscan to try and find clusters and outlier

from numpy.core.numeric import outer
from pandas.core.frame import DataFrame
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
    CONFIDENTIAL_DATA_FILE = 'tset_H10_slip_noslip.csv'
    #five clusters 
    #CONFIDENTIAL_DATA_FILE = '2021_05_21_tset_new_ref_H10_2.csv'
    
    file_name = os.path.join(os.getcwd(), CONFIDENTIAL_DATA_FOLDER, CONFIDENTIAL_DATA_FILE)
    my_csv = read_csv(file_name, sep=',')
    return my_csv

##
def extract_matrix( source_csv ):
    data_matrix=source_csv.iloc[:,:-2].values.astype(float)
    return data_matrix

from sklearn.decomposition import PCA
from sklearn.preprocessing import MinMaxScaler
#
def compute_pca( source_matrix  ):
    
    my_pca =PCA(n_components=2).fit_transform(source_matrix)
    my_pca = MinMaxScaler().fit_transform(my_pca)
    #logging.debug(f"--------------------------------------\ndata{my_pca}, {type(my_pca)}, {my_pca.size}, {my_pca.shape}")
    return my_pca

#something to do with scanning scores... one day try if it does something
from sklearn.metrics import silhouette_score
def try_clusterization( source ):
    for num_clusters in range(2,11):
        my_kmeans = make_pipeline(KMeans(n_clusters=num_clusters))
        labels = my_kmeans.fit(source)
        my_score = silhouette_score(source, labels)
        print(f"{my_score}")
        
    return

from sklearn.cluster import DBSCAN
from sklearn.pipeline import make_pipeline
#from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
##cluster
#   outliers aare identified as -1, automatically count number of classes
def exe_dbscan( source ):
    my_cluster_tool = make_pipeline( MinMaxScaler(), DBSCAN(eps=0.5) )
    my_ret = my_cluster_tool.fit_predict(source)
    return my_ret

def main():
    #open the CSV file
    my_csv = open_csv()
    #logging.debug(f"{my_csv}")
    
    data_matrix = extract_matrix(my_csv)

    ##
    data_pca = compute_pca(data_matrix)
    logging.debug(f"--------------------------------------\nPCA: {data_pca} {data_pca.shape}")
    #construct a dataframe
    my_dataframe = DataFrame(data_pca, columns=['PCA0','PCA1'])
    my_dataframe["Name"] = my_csv["Name"]
    
    data_cluster = exe_dbscan(data_matrix)
    logging.debug(f"--------------------------------------\DBSCAN: {data_cluster} {data_cluster.shape}")
    #add to dataframe
    my_dataframe["Cluster"] = data_cluster
    #compute the index of outliers
    my_dataframe["label"]=""
    my_dataframe.loc[my_dataframe.Cluster==-1,"label"] = [f"{index}" for index in my_dataframe[my_dataframe.Cluster < 0].index  ]

    #initialize plot
    my_figure, my_axes_a = plt.subplots(figsize=(10,6))
    #my_axes_b = my_axes_a.twinx()

    #show all data
    my_axes_a = sns.scatterplot(data=my_dataframe, x='PCA0', y='PCA1', hue='Cluster',marker="+")

    #construct a dataframe with the outliers
    dataframe_outlier = my_dataframe[my_dataframe["Cluster"]<0]
    my_axes_a = sns.scatterplot(data=dataframe_outlier, x='PCA0', y='PCA1')

    #label the outliers
    outliers = my_dataframe[my_dataframe.Cluster < 0]
    for label, x, y in zip(outliers.label, outliers.PCA0, outliers.PCA1):
        plt.annotate( label, (x,y))

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
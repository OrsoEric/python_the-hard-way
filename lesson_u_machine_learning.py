## Logistic regression
#   sigmoid usually is able to separate probabilistically a set.
#   e.g. obesity. some light weight are obese (dwarf) some high weight are not obese (strong man)

#loss function (y-yT) output of model minus expected output
#split data into training (80% to 90%) validation (20% to 10%)
#durint training minimize loss on training, then see loss on validation
#choose structure of the model: e.g. forest classificator

#   supervised: i know what the right answer should be (usually classification and regression)
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


##  sklearn like an inefficient lego for machine learning, good to try thing
#C:\Program Files (x86)\Python\Scripts>
#pip3 install sklearn
from float_to_eng_string import float_to_eng_string
from time import perf_counter

timestamp = perf_counter()
import sklearn
print(f'took {float_to_eng_string(perf_counter() -timestamp)}s to import sklearn')


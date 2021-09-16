from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.preprocessing import scale
from matplotlib import pyplot as plt
import pandas as pd
# %matplotlib inline


# DATASET_URL = ''
# FEATURE_NAME = ''

# def load_data():
#     data = pd.read_csv(DATASET_URL, sep=';')
#     return data

# df = load_iris()
# iris = scale(df.data)


def kmc():
    iris = pd.read_csv('IRIS.csv')
    x = iris.iloc[:, [0, 1, 2, 3]].values

    cluster = KMeans(n_clusters=3, init='k-means++', n_init=3,
                     max_iter=300, tol=1e-04, random_state=0)
    fitted = cluster.fit_predict(x)
    return(fitted)


def main():
    labels = kmc()
    print("Cluster labels: ", labels)


if __name__ == '__main__':
    main()

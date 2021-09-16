from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

# DATASET_URL = ''
# FEATURE_NAME = ''

# def load_data():
#     data = pd.read_csv(DATASET_URL, sep=';')
#     return data

# data = load_data()

data = load_breast_cancer()


def svm():
    X = data.data
    Y = data.target

    x_train, x_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=0.2, random_state=5)

    classifier = SVC(kernel='linear', C=3)
    classifier.fit(x_train, Y_train)

    return(classifier.score(x_test, Y_test))


def main():
    score = svm()
    print("Classifier score is: ", score*100)


if __name__ == '__main__':
    main()

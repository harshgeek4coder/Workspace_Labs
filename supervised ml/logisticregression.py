from sklearn.linear_model import LogisticRegression

class CustomModel(object):
    
    def fit(self, X, y):
        
        model_params = {
            'penalty': 'l2',
            'dual': False,
            'tol': 0.0001,
            'C': 1.0,
            'fit_intercept': True,
            'intercept_scaling': 1,
            'class_weight': None,
            'random_state': 1234,    # Fixed to 1234 for reproducibility
            'solver': 'liblinear',
            'max_iter': 100,
            'multi_class': 'ovr',
            'verbose': 0,
            'warm_start': False,
            'n_jobs': 1
        }
    
        self.clf = LogisticRegression(**model_params)
        self.clf.fit(X, y)
        
        return self 

    def predict(self, X):
    
        return self.clf.predict_proba(X)[:,1]


from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

X, y = load_breast_cancer(return_X_y=True)

X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                    train_size=0.75, 
                                                    test_size=0.25, 
                                                    random_state=1234)


# load our model
model = CustomModel()

# fit our model
model.fit(X_train, y_train)

# generate some predictions
model.predict(X_test)

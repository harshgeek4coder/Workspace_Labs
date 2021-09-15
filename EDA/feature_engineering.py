class DiscretizeByDecisionTree():
    
    def __init__(self, col=None, max_depth=None, tree_model=None):
        self.col = col
        self._dim = None
        self.max_depth = max_depth
        self.tree_model = tree_model


    def fit(self, X, y, **kwargs):

        self._dim = X.shape[1]

        _, tree = self.discretize(
            X_in=X,
            y=y,
            max_depth=self.max_depth,
            col=self.col,
            tree_model=self.tree_model
        )
        self.tree_model = tree
        return self

    def transform(self, X):

        if self._dim is None:
            raise ValueError('Must train encoder before it can be used to transform data.')

        #  make sure that it is the right size
        if X.shape[1] != self._dim:
            raise ValueError('Unexpected input dimension %d, expected %d' % (X.shape[1], self._dim,))

        X, _ = self.discretize(
            X_in=X,
            col=self.col,
            tree_model=self.tree_model
        )

        return X 


    def discretize(self, X_in, y=None, max_depth=None, tree_model=None, col=None):

        X = X_in.copy(deep=True)

        if tree_model is not None:  # transform
            X[col+'_tree_discret'] = tree_model.predict_proba(X[col].to_frame())[:,1]

        else: # fit
            if isinstance(max_depth,int):
                tree_model = DecisionTreeClassifier(max_depth=max_depth)
                tree_model.fit(X[col].to_frame(), y)
            
            elif len(max_depth)>1:
                score_ls = [] # here I will store the roc auc
                score_std_ls = [] # here I will store the standard deviation of the roc_auc
                for tree_depth in max_depth:
                    tree_model = DecisionTreeClassifier(max_depth=tree_depth)
                    scores = cross_val_score(tree_model, X[col].to_frame(), y, cv=3, scoring='roc_auc')
                    score_ls.append(np.mean(scores))
                    score_std_ls.append(np.std(scores))
                temp = pd.concat([pd.Series(max_depth), pd.Series(score_ls), pd.Series(score_std_ls)], axis=1)
                temp.columns = ['depth', 'roc_auc_mean', 'roc_auc_std']
                print('result ROC-AUC for each depth')
                print(temp)
                max_roc = temp.roc_auc_mean.max()
                optimal_depth=temp[temp.roc_auc_mean==max_roc]['depth'].values
                print('optimal_depth:',optimal_depth)
                tree_model = DecisionTreeClassifier(max_depth=optimal_depth)
                tree_model.fit(X[col].to_frame(), y)
            else:
                raise ValueError('max_depth of a tree must be an integer or a list')

        return X, tree_model
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import GradientBoostingClassifier

def RunKNN(TrainData, Target, TestSize, RandomState, neighbors):
    """ The function splits the data, fits the XGBoost model, predits the classification and probablity of each classification and returns the tet set with the values in a dataframe"""
    X_train, X_test, y_train, y_test = train_test_split(TrainData, Target, test_size=TestSize, random_state=RandomState)
    clf = KNeighborsClassifier(n_neighbors = neighbors)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    y_prob = clf.predict_proba(X_test)
    predictions = [round(value) for value in y_pred] 
    X_test['StatusPrediction'] = y_pred
    X_test['StatusProbability_0'] = y_prob[:,0]
    X_test['StatusProbability_1'] = y_prob[:,1]
    Accuracy = accuracy_score(y_test, predictions)
    AccuracyPercent = (Accuracy * 100.0)
    return X_test,AccuracyPercent

def RunDecisionTree(TrainData, Target, TestSize, RandomState, MaxDepth):
    """ The function splits the data, fits the tree, predits the classification and probablity of each classification and returns the tet set with the values in a dataframe"""
    X_train, X_test, y_train, y_test = train_test_split(TrainData, Target, test_size=TestSize, random_state=RandomState)
    tree = DecisionTreeClassifier(max_depth = MaxDepth, random_state = RandomState)
    tree.fit(X_train, y_train)
    y_pred = tree.predict(X_test)
    y_prob = tree.predict_proba(X_test)
    predictions = [round(value) for value in y_pred] 
    X_test['StatusPrediction'] = y_pred
    X_test['StatusProbability_0'] = y_prob[:,0]
    X_test['StatusProbability_1'] = y_prob[:,1]
    Accuracy = accuracy_score(y_test, predictions)
    AccuracyPercent = (Accuracy * 100.0)
    return X_test,AccuracyPercent

def RunRandomForest(TrainData, Target, TestSize, RandomState, Estimators):
    """ The function splits the data, fits the tree, predits the classification and probablity of each classification and returns the tet set with the values in a dataframe"""
    X_train, X_test, y_train, y_test = train_test_split(TrainData, Target, test_size=TestSize, random_state=RandomState)
    forest = RandomForestClassifier(n_estimators = Estimators, random_state = RandomState)
    forest.fit(X_train, y_train)
    y_pred = forest.predict(X_test)
    y_prob = forest.predict_proba(X_test)
    predictions = [round(value) for value in y_pred] 
    X_test['StatusPrediction'] = y_pred
    X_test['StatusProbability_0'] = y_prob[:,0]
    X_test['StatusProbability_1'] = y_prob[:,1]
    Accuracy = accuracy_score(y_test, predictions)
    AccuracyPercent = (Accuracy * 100.0)
    return X_test,AccuracyPercent

def RunGradientBoostingClassifier(TrainData, Target, TestSize, RandomState):
    """ The function splits the data, fits the GradientBoosting model, predits the classification and probablity of each classification and returns the tet set with the values in a dataframe"""
    X_train, X_test, y_train, y_test = train_test_split(TrainData, Target, test_size=TestSize, random_state=RandomState)
    gbrt = GradientBoostingClassifier()
    gbrt.fit(X_train, y_train)
    y_pred = gbrt.predict(X_test)
    y_prob = gbrt.predict_proba(X_test)
    predictions = [round(value) for value in y_pred] 
    X_test['StatusPrediction'] = y_pred
    X_test['StatusProbability_0'] = y_prob[:,0]
    X_test['StatusProbability_1'] = y_prob[:,1]
    Accuracy = accuracy_score(y_test, predictions)
    AccuracyPercent = (Accuracy * 100.0)
    return X_test,AccuracyPercent

def RunXGBOOST(TrainData, Target, TestSize, RandomState):
    """ The function splits the data, fits the XGBoost model, predits the classification and probablity of each classification and returns the tet set with the values in a dataframe"""
    X_train, X_test, y_train, y_test = train_test_split(TrainData, Target, test_size=TestSize, random_state=RandomState)
    model = XGBClassifier()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)
    predictions = [round(value) for value in y_pred] 
    X_test['StatusPrediction'] = y_pred
    X_test['StatusProbability_0'] = y_prob[:,0]
    X_test['StatusProbability_1'] = y_prob[:,1]
    Accuracy = accuracy_score(y_test, predictions)
    AccuracyPercent = (Accuracy * 100.0)
    return X_test,AccuracyPercent

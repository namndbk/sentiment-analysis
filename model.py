from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import GridSearchCV
from sklearn.svm import LinearSVC, LinearSVR
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.externals import joblib


import time, os, json
import numpy as np
import scipy

from collections import Counter


class EnsembelModel:
    def __init__(self, score, cross_validation=3):
        self.cross_validation = cross_validation
        self.score = score
        self.models = {}
        self.n_models = 0
    

    def add_model(self, name, estimator):
        self.models.update({
            name: estimator
        })
        self.n_models += 1
    

    def remove_model(self, name):
        if self.models.get(name):
            del self.models[name]
            self.n_models -= 1
        else:
            print("\tNot found {} in models stack".format(name))
        

    def fit(self, X_train, y_train):
        print("\tTraning model ...")
        t0 = time.time()
        if len(self.models) == 0:
            estimator = LinearSVC()
            name = "LinearSVC"
            self.add_model(name, estimator)
        for name, model in self.models.items():
            model.fit(X_train, y_train)
        train_time = time.time() - t0
        print("\tTrain time: {:.4f}s".format(train_time))

    
    def predict(self, X_test):
        t0 = time.time()
        result = [[] for _ in range(X_test.shape[0])]
        for name, model in self.models.items():
            y_pred = model.predict(X_test)
            for i, c in enumerate(y_pred):
                result[i].append(c)
        y_pred = []
        y_rate = []
        for i, c in enumerate(result):
            pred = Counter(c).most_common(1)[0]
            rate = int(c[pred]) / self.n_models
            y_pred.append(pred)
            y_rate.append(rate)
        test_time = time.time() - t0
        print("\tTest time: {:.4f}s".format(test_time))
        return y_pred, y_rate


    def save_model(self, folder_path):
        print("\tSaving model ...")
        try:
            os.mkdir(folder_path)
        except:
            pass
        meta = []
        for name, model in self.models.items():
            path = os.path.join(folder_path, "{}.joblib".format(name))
            joblib.dump(model, path)
            meta.append({
                "name": name,
                "model_path": path,
            })
        meta_path = os.path.join(folder_path, "meta.txt")
        with open(meta_path, "wb") as f:
            json.dump(meta, f)
        print("\tDone !")


    def load_model(self, folder_path):
        print("\tLoading model ...")
        meta_path = os.path.join(folder_path, "meta.txt")
        with open(meta_path, "rb") as f:
            meta = json.load(f)
        for info in meta:
            name = info["name"]
            estimator = joblib.load(info["model_path"])
            self.models.update({
                name: estimator
            })
        print("\tDone !")


class Classifier():

    def __init__(self, estimator=None, cross_validation=None):
        self.cross_validation = cross_validation
        self.estimator = estimator

    
    def fit(self, X_train, y_train):
        print("\tTraining model ...")
        t0 = time.time()
        self.estimator.fit(X_train, y_train)
        train_time = time.time() - t0
        print("\tTrain time: {:.4f}s".format(train_time))
    

    def predict(self, X_test):
        print("\Testing model ...")
        t0 = time.time()
        y_pred = self.estimator.predict(X_test)
        test_time = time.time() - t0
        print("\tTest time: {:.4f}s".format(test_time))
        return y_pred
    
    def save_model(self, folder_path):
        pass
    

    def load_model(self, file_path):
        pass
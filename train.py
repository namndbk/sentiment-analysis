from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split


from utils.dataset import load_data
from utils.preprocess import normalize

from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import GridSearchCV
from sklearn.svm import LinearSVC, LinearSVR
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

from model import EnsembelModel

import copy


import warnings
warnings.filterwarnings('ignore')

from model import Classifier

X, y = load_data("data/data_20_4.json")
print(X.shape[0])
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2020)
X_train = normalize(X_train)
X_test = normalize(X_test)


# transform = TfidfVectorizer(max_df=0.65)
# X_train = transform.fit_transform(X_train)
# X_test = transform.transform(X_test)
# estimator = LinearSVC(C=0.3)
# clf = Classifier(estimator=estimator)
# clf.fit(X_train, y_train)
# y_pred = clf.predict(X_test)
# print(accuracy_score(y_test, y_pred))
# print(confusion_matrix(y_test, y_pred))
# print(classification_report(y_test, y_pred, labels=["good", "bad"]))



# C = 0.1
# while C <= 0.5:
#     clf = LinearSVC(C=C)
#     print(C)
#     clf.fit(X_train, y_train)
#     y_pred = clf.predict(X_test)
#     print(accuracy_score(y_test, y_pred))
#     print(confusion_matrix(y_test, y_pred))
#     print(classification_report(y_test, y_pred, labels=["good", "bad"]))
#     C += 0.1
# import pickle
a = 0.1
while a <= 0.5:
    df = 0.1
    while df <= 1.0:
        train = copy.deepcopy(X_train)
        test = copy.deepcopy(X_test)
        transform = TfidfVectorizer(max_df=df, ngram_range=(1, 2))
        train = transform.fit_transform(train)
        test = transform.transform(test)
        estimator = MultinomialNB(alpha=a)
        print((a, df))
        clf = Classifier(estimator=estimator)
        clf.fit(train, y_train)

        y_pred = clf.predict(test)
        print(accuracy_score(y_test, y_pred))
        print(confusion_matrix(y_test, y_pred))
        print(classification_report(y_test, y_pred, labels=["good", "bad"]))
        df += 0.1
    a += 0.1
# with open("models/naivebayes/svm", "wb") as f:
#     pickle.dump(clf, f)
# with open("models/naivebayes/transform", "wb") as f:
#     pickle.dump(transform, f)

# est1 = LinearSVC()
# est2 = MultinomialNB()
# est3 = KNeighborsClassifier()

# clf = EnsembelModel()
# clf.add_model("svm", est1)
# clf.add_model("naive_bayes", est2)
# clf.add_model("knn", est3)
# clf.fit(X_train, y_train)
# y_pred, y_rate = clf.predict(X_test)
# print(accuracy_score(y_test, y_pred))
# print(confusion_matrix(y_test, y_pred))
# print(classification_report(y_test, y_pred, labels=["good", "bad"]))
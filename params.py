
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
from utils.preprocess import normalize_text

import warnings
warnings.filterwarnings('ignore')



model = pickle.load(open("models/modelv2/svm", "rb"))
print(model.estimator.get_params())
transform = pickle.load(open("models/modelv2/transform", "rb"))
print(transform.get_params())
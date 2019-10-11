from sklearn.dummy import DummyClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import SGDClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import FeatureUnion, Pipeline
from sklearn.pipeline import make_union
from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np
from sklearn.preprocessing import StandardScaler


#class FeatureExtractor(BaseEstimator, TransformerMixin):
#    def fit(self, X, y=None):
#        return self
#
#
#class NumberOfCharactersFeatureExtractor(FeatureExtractor):
#    def transform(self, X, y=None):
#        return np.array([len(x) for x in X]).reshape(-1, 1)
#
#
#class NumberOfWhitespacesFeatureExtractor(FeatureExtractor):
#    def transform(self, X, y=None):
#        return np.array([len(x) - len(x.replace(' ', '')) for x in X]).reshape(-1, 1)
#
#
#class HeOrSheFeatureUnion(FeatureUnion):
#    def __init__(self):
#        super().__init__([
#            ('tfidf', TfidfVectorizer()),
#            ('noc', NumberOfCharactersFeatureExtractor()),
#            ('nows', NumberOfWhitespacesFeatureExtractor()),
#        ])
#
#
#class HeOrSheSGDClassifier(Pipeline):
#    def __init__(self):
#        super().__init__([
#            ('feat', HeOrSheFeatureUnion()),
#            ('clf', SGDClassifier(loss='hinge', penalty='l2', alpha=1e-3, random_state=42, max_iter=5, tol=None)),
#        ])

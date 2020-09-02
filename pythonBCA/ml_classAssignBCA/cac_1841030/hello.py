import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.naive_bayes import CategoricalNB
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import precision_recall_fscore_support
from sklearn.metrics import confusion_matrix , accuracy_score, classification_report
from sklearn import preprocessing
from sklearn import metrics
import seaborn as sns
from sklearn.neighbors import KNeighborsClassifier
from matplotlib.pyplot import savefig
from sklearn import tree
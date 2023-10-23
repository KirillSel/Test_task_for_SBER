# -*- coding: utf-8 -*-
"""train_model.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QQqNzsMKndhufKdsyMuGcHQotLUT2TKT
"""

import pandas as pd
import re
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from argparse import Namespace, ArgumentParser

from sklearn.metrics import classification_report, confusion_matrix, f1_score, make_scorer
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.model_selection import GridSearchCV

def arg_parser() -> Namespace:
    
    parser = ArgumentParser()

    parser.add_argument('--save_train_df_path',
                        type=str,
                        required=True,
                        help='Path where located preprocessed train df')

    parser.add_argument('--save_test_df_path',
                        type=str,
                        required=True,
                        help='Path where located preprocessed test df')

    args = parser.parse_args()

    return args

def train(args):
    train_df = pd.read_csv(args.save_train_df_path)
    test_df = pd.read_csv(args.save_test_df_path)

    X_train = train_df.drop(columns=["diabetes"]).to_numpy()
    X_test = test_df.drop(columns=["diabetes"]).to_numpy()
    y_train = train_df[['diabetes']].to_numpy().ravel()
    y_test = test_df[['diabetes']].to_numpy().ravel()

    gbc = GradientBoostingClassifier(random_state = 42)

    gbc_model = gbc.fit(X_train, y_train)

    y_pred = gbc_model.predict(X_test)

    print('F1 Score: %.3f' % f1_score(y_test, y_pred))

if __name__ == '__main__':
    train(arg_parser())

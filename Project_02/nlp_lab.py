# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 15:31:47 2016

@author: mg
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


from sklearn.datasets import fetch_20newsgroups

categories = [
    'alt.atheism',
    'talk.religion.misc',
    'comp.graphics',
    'sci.space',
]

data_train = fetch_20newsgroups(subset='train', categories=categories,
                                shuffle=True, random_state=42,
                                remove=('headers', 'footers', 'quotes'))

data_test = fetch_20newsgroups(subset='test', categories=categories,
                               shuffle=True, random_state=42,
                               remove=('headers', 'footers', 'quotes'))
                               
                               
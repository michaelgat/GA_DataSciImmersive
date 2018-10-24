# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 18:02:48 2016

@author: mg
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

bb_df = pd.read_csv('billboard.csv')

#Assign new column titles
new_columns = ['year', 'artist', 'song', 'play_time', 'genre', 'entered_date', 'peak_date'] + range(1,77)
bb_df.columns = new_columns

#Drop everything past 65, as it's all blank and doesn't add anything
bb_df.drop(range(66,77), inplace=True, axis=1)
print bb_df.head()

# Look at the basic structure
# OK, really I did this in a spreadsheet first, as that's a much better way
# of looking at the structure of a dataset when possible

mean_by_week = bb_df.groupby('genre').mean()
mean_by_week.drop('year', inplace=True, axis=1)
x = mean_by_week.transpose()
print x.idxmax()
print x.idxmin()
x.plot()

median_by_week = bb_df.groupby('genre').median()
median_by_week.drop('year', inplace=True, axis=1)
y = median_by_week.transpose()
print y.idxmax()
print y.idxmin()
y.plot()


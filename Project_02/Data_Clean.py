# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 19:24:03 2016

@author: mg
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

bb_df = pd.read_csv('billboard.csv')

# Assign new column titles that are simple and easy to use
new_columns = ['year', 'artist', 'song', 'play_time', 'genre', 'entered_date', 'peak_date'] + range(1,77)
bb_df.columns = new_columns

# Earlier examination of data showed that there was no data past week 65
# Drop everything past 65, as it's all blank and doesn't add anything
bb_df.drop(range(66,77), inplace=True, axis=1)

# Clean up the textual columns
# First make sure it's a string not some other type
bb_df['artist'].apply(str)
# Drop non ascii characters -- there were a few visible and it's a good practice in any case
# Replace with nothing
bb_df['artist'] = bb_df['artist'].apply(lambda x: ''.join(["" if ord(i) < 32 or ord(i) > 126 else i for i in x]))
print bb_df['artist']
# Repeat with the song column
bb_df['song'].apply(str)
bb_df['song'] = bb_df['song'].apply(lambda x: ''.join(["" if ord(i) < 32 or ord(i) > 126 else i for i in x]))
print bb_df['song']


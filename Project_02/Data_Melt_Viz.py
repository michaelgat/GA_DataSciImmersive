# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 21:26:32 2016

@author: mg
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import timedelta

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
# Repeat with the song column
bb_df['song'].apply(str)
bb_df['song'] = bb_df['song'].apply(lambda x: ''.join(["" if ord(i) < 32 or ord(i) > 126 else i for i in x]))


# New Stuff starts here.

bb_df = pd.melt(bb_df, id_vars=['year', 'artist', 'song', 'play_time', 'genre', 'entered_date', 'peak_date'], value_vars=range(1,66), var_name="week", value_name="rank")
bb_df = bb_df.sort_values(by=['entered_date', 'peak_date', 'artist', 'song', 'week'], ascending=[True, True, True, True, True])

bb_df['entered_date'] = bb_df['entered_date'].apply(pd.to_datetime)
bb_df['peak_date'] = bb_df['peak_date'].apply(pd.to_datetime)


# I want a column that shows me the date for each ranking. This is relatively
# simple, as the BB results are tabulated weekly. To find the date for the ranking
# take the date entered and add one week for each week beyond 1.
# OR put otherwise, add week -1 weeks to the entered date.

def add_date(date, week):
    newdate = date + timedelta(weeks = week)
    return newdate

bb_df['rank_date'] = 0

bb_df['rank_date'] = bb_df.apply(lambda row: add_date(row['entered_date'], row['week'] - 1), axis=1)


# Now I'm going to pivot so I can chart things by week on the BB 100
# Averaging by genre. This will give a similar result to the one during
# initial exploration.

charting_df = pd.pivot_table(bb_df, values=('rank'), columns=('genre'), index=('week'), aggfunc='mean')

plot = charting_df.plot()

fig = plot.get_figure()
fig.set_size_inches(15,12)
plot


# How about looking at individual songs

charting_df = pd.pivot_table(bb_df, values=('rank'), columns=('song'), index=('week'))

plot = charting_df.plot(legend=False)

fig = plot.get_figure()
fig.set_size_inches(15,12)
fig.savefig('output.png')
plot

# How about looking at the Pop genre, but looking at individual songs

slice_df = bb_df.loc[bb_df['genre'] == 'Pop']
charting_df = pd.pivot_table(slice_df, values=('rank'), columns=('song'), index=('week'))

plot = charting_df.plot()

fig = plot.get_figure()
fig.set_size_inches(15,12)
plot

# Jazz had a weird profile, I'd like to look at that by song

slice_df = bb_df.loc[bb_df['genre'] == 'Jazz']
charting_df = pd.pivot_table(slice_df, values=('rank'), columns=('song'), index=('rank_date'))

plot = charting_df.plot()

fig = plot.get_figure()
fig.set_size_inches(15,12)
plot
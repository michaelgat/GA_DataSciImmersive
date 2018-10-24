# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

bb_df = pd.read_csv('billboard.csv')

# Look at the basic structure
# OK, really I did this in a spreadsheet first, as that's a much better way
# of looking at the structure of a dataset when possible
print bb_df.head()
print

# What's the mix of songs by genre?
print bb_df[['genre', 'year']].groupby('genre').count()
print


# I wonder what is the mean position on the chart of each song in each week
# Since it entered
# Interesting finding, while BB reports data out to the 76th week,
# In fact, no songs stay on the charts for more than 65 weeks.
# And in fact, might as well drop columns 66-76 entirely going forward.
# Suspicion: they do this to allow for extreme outliers, and none were encountered
# In 2000.


mean_by_week = bb_df.loc[:,'x1st.week':'x76th.week'].mean()
print mean_by_week
print

# Interesting finding, while BB reports data out to the 76th week,
# In fact, no songs stay on the charts for more than 65 weeks.
# And in fact, might as well drop columns 66-76 entirely going forward.
# Suspicion: they do this to allow for extreme outliers, and none were encountered
# In 2000.

mean_by_week = mean_by_week['x1st.week':'x65th.week']
print mean_by_week

# How about the highest mean? This would be the point where most songs
# Hit their lowest ranking, presumably right after they enter or right before
# they leave. Turns out it's week 1. No surprise. But means that typically
# will drop out from higher positions than the one they entered at.
#
# Interesting finding, while BB reports data out to the 76th week,
# In fact, no songs stay on the charts for more than 65 weeks.
# And in fact, might as well drop columns 66-76 entirely going forward.
# Suspicion: they do this to allow for extreme outliers, and none were encountered
# In 2000.

# Note to self, 1 is highest ranking, 100 is lowest...

print "Week of lowest mean ranking: " + mean_by_week.idxmax()

# Minimum would give us the opposite. In what week does the average song peak
# out? Turns out it's 42 weeks in.
print "Week of highest mean ranking: " + mean_by_week.idxmin()

# I wonder how that changes if we look at the median rather than the mean?
# Same general idea:

median_by_week = bb_df.loc[:,'x1st.week':'x65th.week'].median()
print median_by_week
print
print "Week of lowest median ranking:" + median_by_week.idxmax()
print "Week of highest median ranking: " + median_by_week.idxmin()

# Quick 'n dirty chart of these things
df_temp = pd.concat([median_by_week, mean_by_week], axis=1)
df_temp.columns = ['median','mean']

plot = df_temp.plot(kind = 'bar')
fig = plot.get_figure()
fig.set_size_inches(15,12)
plot




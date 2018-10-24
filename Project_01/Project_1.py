# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 18:57:25 2016

@author: mg
"""

import matplotlib.pyplot as plt
import numpy as np
import csv
scores_list = []

data_path = "sat_scores.csv"

with open(data_path) as file:
    for row in csv.reader(file):
        scores_list.append(row)
print [score for score in scores_list]
print

header_row = scores_list.pop(0)
print header_row
print

states = []
state_index = header_row.index("State")
states.append([score[state_index] for score in scores_list])

print [type(col) for col in scores_list[0]]
print

scores_list_num = []
for i in range (0,len(scores_list)):
    new_row = []
    new_row.append(scores_list[i][0])        
    new_row += (map(int, scores_list[i][1:4]))
    scores_list_num.append(new_row)
print scores_list_num
print

dict_rate = {}
dict_verbal = {}
dict_math ={}

for row in scores_list_num:
    dict_rate[row[0]] = row[1]
    dict_verbal[row[0]] = row[2]
    dict_math[row[0]] = row[3]
    
print dict_rate
print dict_verbal
print dict_math
print

def dict_by_value(dict_input):
    """
    Takes dictionary input, returns output of dictionary ordered by
    values, with the original keys now stored as lists of values.
    """
    dict_output = {}
    for key, value in dict_input.items():
        if value in dict_output.keys():
            dict_output[value].append(key)
        else:    
            dict_output[value] = [key]
    return dict_output

dict_rate_by_value = dict_by_value(dict_rate)
dict_verbal_by_value = dict_by_value(dict_verbal)
dict_math_by_value = dict_by_value(dict_math)


print "Rates  min/max: " + str(min(dict_rate_by_value.keys())) + ' ' + str(max(dict_rate_by_value.keys()))
print "Verbal min/max: " + str(min(dict_verbal_by_value.keys())) + ' ' + str(max(dict_verbal_by_value.keys()))
print "Math   min/max: " + str(min(dict_math_by_value.keys())) + ' ' + str(max(dict_math_by_value.keys()))
print

def myStdDev(myList):
    """
    Function takes a list of numbers and returns the standard deviation as a float
    """
    myMean = sum(myList)/float(len(myList))
    return sum([(float(value) - myMean) ** 2/len(dict_rate) for value in myList]) ** .5

print "Participation Rate Std Dev: %f" % myStdDev(dict_rate.values())
print "Verbal Score Std Dev: %f" % myStdDev(dict_verbal.values())
print "Math Score Std Dev: %f" % myStdDev(dict_math.values())
print

#Just for fun, compare to numpy std dev
print "Participation Rate Std Dev (Numpy): %f" % np.std(dict_rate.values())
print "Verbal Score Std Dev (Numpy): %f" % np.std(dict_verbal.values())
print "Math Score Std Dev(Numpy): %f" % np.std(dict_math.values())

"""
PLOT SECTION STARTS HERE
"""


plt.hist(dict_rate.values(), 90, facecolor='green')
plt.xlabel('Rate')
plt.ylabel('# of States')
plt.title(r'Histogram of SAT Participation Rate per State')
plt.axis([0, 90, 0, 3.5])
plt.yticks(np.arange(0,3.5,1))
plt.grid(True)
plt.show()

plt.hist(dict_math.values(), 50, facecolor='red')
plt.xlabel('Rate')
plt.ylabel('# of States')
plt.title(r'Histogram of SAT Math Scores by State')
plt.axis([450, 650, 0, 10])
plt.yticks(np.arange(0,10,2))
plt.grid(True)
plt.show()

plt.hist(dict_verbal.values(), 50, facecolor='blue')
plt.xlabel('Rate')
plt.ylabel('# of States')
plt.title(r'Histogram of SAT Math Scores by State')
plt.axis([450, 650, 0, 10])
plt.yticks(np.arange(0,10,2))
plt.grid(True)
plt.show()


#A Scatter Plot by State
x = [i[2] for i in scores_list_num]
y = [i[3] for i in scores_list_num]
z = [i[1] for i in scores_list_num]
colors = np.random.rand(len(scores_list))
plt.scatter(x, y, s=5, c=colors)
plt.xlabel('Verbal')
plt.ylabel('Math')
plt.title(r'Verbal vs Math SAT Scores by State')
plt.show()

#Box Plots
plt.boxplot((x,y), 0, 'rs', 0, showmeans = True, labels=('Verbal','Math'))
plt.title(r'Average SAT Score by State')
plt.show()

#Did the box plot for rate seperately as it has a different scale and doesn't really make sense with the others
#Notch this one, just for fun
plt.boxplot(z, 1, 'rs', 0, showmeans = True, labels = (' '))
plt.title(r'Average SAT Participation Rate by State')
plt.show()
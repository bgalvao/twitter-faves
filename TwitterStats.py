import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as tick

from scipy.stats.kde import gaussian_kde
from scipy.interpolate import UnivariateSpline

def mean(s):
    calc = sum(s)/len(s)
    return calc

def stdev(s):
    calc1 = mean(s)
    calc2 = [(s[i]-calc1)**2 for i in range(len(s))]
    calc3 = mean(calc2)**0.5
    return calc3

def median(s):
    array = sorted(s)
    if len(array) % 2 == 0:
        i = int((len(array) / 2) - 1)
        j = i + 1
        calc = (array[i] + array[j]) / 2
        return calc
    else:
        k = int((len(array) + 1) / 2) - 1
        return array[k]
    
def stats(s):
    result = {'Min': min(s), 'Max': max(s), 'Mean': round(mean(s),2), 'Median': median(s), 'St Dev': round(stdev(s),2)}
    return result

def iqr(s):
#IQR interpolation algorithm set as 'linear', where i + (j - i) * fraction of index
    array = sorted(s)
    indexq1 = (len(array) + 1) / 4
    indexq3 = 3 * (len(array) + 1) / 4
    getposq1 = array[int(indexq1 - 1)]
    getposq3 = array[int(indexq3 - 1)]
    calcq1 = getposq1 + (indexq1 - (int(indexq1))) * (array[int(indexq1)] - array[int(indexq1) - 1])
    calcq3 = getposq3 + (indexq3 - (int(indexq3))) * (array[int(indexq3)] - array[int(indexq3) - 1])
    return (calcq3 - calcq1)

potato = [0,1,2,5,8,8,9,10,12,14,18,20,21,23,25,27,34,43]

numpyiqr = (np.subtract(*np.percentile(wordplot, [75, 25], interpolation='linear')))
print(numpyiqr)
iqr(wordplot)

#

summary = step4
socnet = users

# STEP X: Aggregating measures, removing indices
chartweet = [(summary[i][0], len(summary[i][1])) for i in range(len(summary))]
print(chartweet[0:3])

wordtweet = [(summary[i][0], len(summary[i][1].split())) for i in range(len(summary))]
print(wordtweet[0:3])

charplot = [chartweet[i][1] for i in range(len(chartweet))]
wordplot = [wordtweet[i][1] for i in range(len(wordtweet))]

# STEP X: Summary statistics 
stats(charplot)
stats(wordplot)

# STEP X: Plotting: Boxplot
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10,5))

boxplt1 = axes[0].boxplot(charplot,
                          whis='range',
                          showfliers=False,
                          vert=True,
                          patch_artist=True,
                          widths=0.25
                          )
axes[0].set_title('Character distribution per tweet')
#plt.xticks([])

boxplt2 = axes[1].boxplot(wordplot,
                          whis='range',
                          showfliers=False,
                          vert=True,
                          patch_artist=True,
                          widths=0.25
                          )
axes[1].set_title('Word distribution per tweet')
#plt.xticks([])

colors = ['lightblue']
for x in (boxplt1, boxplt2):
    for patch, color in zip(x['boxes'], colors):
        patch.set_facecolor(color)

for x in axes: 
    x.yaxis.grid(True, color='#dddddd')
    x.set_xlabel('')
    x.set_ylabel('')
    x.set_xticks([])
    x.spines['top'].set_color('#dddddd')
    x.spines['left'].set_color('#dddddd')
    x.spines['bottom'].set_color('#dddddd')
    x.spines['right'].set_color('#dddddd')
plt.show()

[item.get_ydata() for item in boxplt1['whiskers']]
[item.get_ydata() for item in boxplt2['whiskers']]

# STEP X: Plotting: Density plot
# probability is calculated by using a gaussian function (kernel density estimation)
kde_chars = gaussian_kde(charplot)
kde_words = gaussian_kde(wordplot)
dist_chars = np.linspace(min(charplot), max(charplot), 100)
dist_words = np.linspace(min(wordplot), max(wordplot), 100)

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10,5))
densplt1 = axes[0].plot(dist_chars, kde_chars(dist_chars),
                        color='lightblue'
                        )
axes[0].set_title('Probability Density Plot - Characters')

densplt2 = axes[1].plot(dist_words, kde_words(dist_words),
                        color='lightblue'
                        )
axes[1].set_title('Probablity Density Plot - Words')

for x in axes:
    x.yaxis.grid(True, color='#dddddd')
    x.set_xlabel('')
    x.set_ylabel('')
    x.spines['top'].set_color('#dddddd')
    x.spines['left'].set_color('#dddddd')
    x.spines['bottom'].set_color('#dddddd')
    x.spines['right'].set_color('#dddddd')
plt.show()


# STEP X: Plotting: Histogram
taglabel = list(zip(*hashtags_freq[0:13]))[0]
tagcount = list(zip(*hashtags_freq[0:13]))[1]
x_pos = np.arange(len(taglabel)) 

# creating trendline with two points (x,y) 
# fits a polynomial function into a linear function that minimises the squared error
slope, intercept = np.polyfit(x_pos, tagcount, 1)
trendline = intercept + (slope * x_pos)

plt.figure(num=None, figsize=(12,8), dpi=80, facecolor='w', edgecolor='k')
plt.plot(x_pos, trendline, color='red', linestyle='--')    
plt.bar(x_pos, tagcount, align='center')
plt.xticks(x_pos, taglabel) 
plt.ylabel('Number of occurences')
plt.xticks(rotation=45)
plt.gca().set_axisbelow(True) #plt.gca() gets current axis attributes
plt.gca().yaxis.grid(True)
plt.show()

# STEP X: Plotting: Social Network Analysis
sna



# to export plots fig.savefig() or plt.savefig()
# to browse plot styles plt.style.available() and plt.style.use()
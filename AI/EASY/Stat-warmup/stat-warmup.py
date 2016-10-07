# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
import scipy as sp
import scipy.stats

n = int(raw_input())

data = [float(val) for val in raw_input().split()]
d_a = np.array(data)

# mean
#print str(np.mean(d_a))
print "{0:.1f}".format(np.mean(d_a))
    
# median
#print str(np.median(d_a))
print "{0:.1f}".format(np.median(d_a))

# mode
#counts = np.bincount(d_a)
#print np.argmax(counts)
from scipy import stats
ans = stats.mode(d_a, axis=None)
b = int(ans[0])
print str(b)
#print ' '.join(map(str, b))
#print ' '.join(map(str, stats.mode(d_a)[0]))

# std
print "{0:.1f}".format(np.std(d_a))

# confidence interval
import math 

def confidence_interval(a, z_critical = 1.96):
    # http://hamelg.blogspot.com/2015/11/python-for-data-analysis-part-23-point.html
    
    sample_mean = np.mean(a)
    sample_size = len(a)

    #z_critical = stats.norm.ppf(q = 0.96)  # Get the z-critical value*

    pop_stdev = np.std(a)  # Get the population standard deviation

    margin_of_error = z_critical * (pop_stdev/math.sqrt(sample_size))

    print "{0:.1f}".format(sample_mean - margin_of_error) + " " + "{0:.1f}".format(sample_mean + margin_of_error)

    
confidence_interval(d_a)
#print str(m__h) + ' ' +str(m_h)
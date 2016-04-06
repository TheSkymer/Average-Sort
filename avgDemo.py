##
# Test per avgSort.py
#

from avgSort import avgSort
from time import time
from random import randint

lmax = 100000

values = [randint(1, lmax) for n in range(1, lmax)]
ti = time()
avgSort(values)
print("avgsort time: %.3f s" %(time() - ti))

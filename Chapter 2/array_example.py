from array import array
from random import random

#creates an array of 10 million floats
floats = array('d', (random() for i in range(10**7)))

#print the last item in the array
print(floats[-1])

fp = open('floats.bin', 'wb')
floats.tofile(fp)
fp.close()
floats2 = array('d')
fp  = open('floats.bin', 'rb')
floats2.fromfile(fp, 10**7)
fp.close()

print(floats2[-1])
print(floats2 == floats)
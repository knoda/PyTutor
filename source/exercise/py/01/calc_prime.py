
import math

data = raw_input("data? ")
data = int(data)

if data>=2:
    Limit = int(math.sqrt(data))
    for i in range(Limit, 0, -1):
        print i
        if data % i == 0:
            break
    if i==1:
        print "a prime number"
    else:
        print "NOT a prime number"


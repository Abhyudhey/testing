import os
import sys

def myfunc(a,b):
    a,b = map(int, [a,b])
    return a*b

if __name__ == '__main__':
    result = myfunc(sys.argv[1], sys.argv[2])
    print result

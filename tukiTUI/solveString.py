# math objs

from math import *
from math import sin as sen

#-------------------------------------

def solveString(string):
    try:data=eval(str(string)); return data
    except: return None

#----------------------------------

if __name__=="__main__":
    print(solveString("2"))
    print(solveString("2+4**3"))
    print(solveString("2*pi"))
    for n in range(10):
        v=input("\n >> ")
        print(solveString(v))
    input()


import math
def Task1_SQRT():
    import math
    print(math.sqrt(2401))

def Task2_LOG2():
    from math import log2
    print(log2(1024))

def displayTwice(msg):
    """prints a message twice"""
    print(msg)
    print(msg)

def findMax(a,b):
    """Finds the maximum of two values."""
    if ( a > b ):
	    max = a
    else:
	    max = b
    return max

def DefualtArgument(num1 , num2 = "?"):
    if num2 == "?":
        return num1 * num1
    else:
        return num1 * num2

def someFunc(x, y, z):
	print("x is", x, "\ny is", y, "\nz is", z)

def printDifferentSeperator():
    print("hello" , "There" , "!", sep="-")


def calcAve(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total/len(numbers)


hypot = lambda a,b : math.sqrt(a * a + b * b)

ToSeconds = lambda a,b = 0 : (a*60*60 + b*60)


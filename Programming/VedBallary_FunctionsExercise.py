#Ved Ballary
#Version #0.2
#VedBallary_FunctionsExercise.py
#Last edit 27 Oct 2017
#This program makes a box and figures out the lowest number in  range.

import math
Width = 10
Height = 5

def min3(a, b , c):
#    """Takes three numbers and returns the smallest value."""
    if a <= b and a <= c:
        print(a)
    elif b <= a and b <= c:
        print(b)
    elif c <= b and c <= a:
        print(c)

def box(width, height):
    box = ""
    for i in range(height):
        box += (width * "* " + "\n")
    return(box)

def main():
    print(min3(7, 5, 4)) #print 4
    print(min3(4, 5, 5))
    print(min3(4, 4, 4))
    print(min3(-3, -2, -1000))
    print(min3("Z", "B", "A"))
    print(box(12, 7))
if __name__ == "__main__":
    main()

#box

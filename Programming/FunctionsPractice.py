#FunctionsPractice.py
#Ved Ballary
# 25 October 2017
#V0.1
#Mr. Ubial will empower us with functions

#def print_instructions():
#    print("You stole a camel and are trying to get away from its owners")
#    print("Do your best to outrun.")
#    print("Good luck!")
'''
def volume_of_sphere_improper(radius):
    pi = 3.1415
    volume = (4.0/3.0) * pi * (radius ** 3)
    print("The volume of the sphere is " + str(volume) + "units cubed")

volume_of_sphere(30)
'''
def volume_of_sphere_return(radius):
    pi = 3.1415
    volume = (4.0/3.0) * pi * (radius ** 3)
    return volume
#volume_of_sphere = volume_of_sphere_return(30)

#print(volume_of_sphere)
#print(volume_of_sphere_return(30))

def calculate_average_three(a, b, c):
    """Calculates the average of three numbers. """
    sum = a + b + c
    return sum / 3
#print(calculate_average_three(10, 11, 12))

x = 10

def sum(a, b):
    x = a + b
    print(x)

sum(10, 10)
print(x)

#VedBallary
#Dog.py
#Last edited 14 November 2017
#V0.1
#Classes redux



# When creating a class in python 2,
# the superclass should be Object
class Dog(object):
    # COnstructor
    # Constructors should always have
    # self as first parameter
    def __init__(self, name):
        self.name = name
        self.master = ""

    def fetch(self): #first parameter is self
        return "stick."

    def speak(self):
        print ("Yo, what up " + self.master +  ".")
        #print "{} says, \"Woof!\"".format(self.name)

my_dog = Dog("Bowwow")
print(my_dog.fetch())
my_dog.speak()


# New subclass
class Bulldog(Dog):
    # A bulldog IS A dog

    #Pay attention to this
    # WHen you call the constructor of
    # the superclass, you MUST follow
    # this format
    def __init__(self,name):
        # super(CurrentClass, self).__init__(any parameters)
        super(Bulldog, self). __init__(name)

    def speak(speak):
        print "{} says, \"Hkrrhhrhhrhrhrhrhrhrhrhhrhrhrhrhrh\"".format(self.name)


neighbour_dog = Bulldog("Sirloin")
neighbour_dog.master = "Dean"
print(neighbour_dog.fetch())
neighbour_dog.speak()


print(type(my_dog))
print(type(neighbour_dog))

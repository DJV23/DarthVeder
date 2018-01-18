#CamelRun.py
#Ved Ballary
#V.3.3.9
#last update: 4 october 2017
#Object of the game is to get across the dessert on a stolen camel while the owners are chasing you
import random

print ("Welcome to Plane Run")
print ("You are trying to get away from bad guys on an airplane.")
print("")
print("Good luck!")

done = False


plane_fuel = 20
engine_heat = 40
badguy_distance = 500
safe_distance = 10241
glide_count = 0


#n_ground = raw_input("")
#if on_ground ==
name = raw_input("Enter your name ")
if safe_distance <= 0 :
    done = True
else:
    done = False
while not done:
    print("A. Full throttle.")
    print("B. Medium Throttle. ")
    print("C. Glide. ")
    print("D. Status Check. ")
    print("E. Quit. ")
    first_check = raw_input("Ans: ")

    if first_check == "E":
        done = True
    else:
            if first_check == "D":
                print ("Your distance to safety is " + str(safe_distance) +"km" + "\n The fuel left in your plane is " + str(plane_fuel) + "\n The engine heat measurment is " + str(engine_heat) + "\n The badguys are " +str(badguy_distance) + "km away from you" )

            else:

                    if first_check == "C" or first_check == "C.":
                        glide = random.randrange(100,150)
                        safe_distance = safe_distance - glide
                        print("You glided " + str(glide) + "km")
                        glide_count = 1

                        if safe_distance <= 0 :
                            done = True
                            print("You have suceeded. Good job! Get of  the plane NOW! I need it for my next pilot. Good bye " + str(name))
                        else:
                            done = False
                        badguy_distance = badguy_distance - 100


                        if badguy_distance <= 0:
                            print ("Oh!! You got captured. Hard luck. Try again next time")
                            done = True

                        else:
                            pass

                    else:

                            if first_check == "B":
                                Medium_throttle = random.randrange(150,499)
                                safe_distance = safe_distance - Medium_throttle
                                badguy_distance = 500 - random.randrange(60,99)
                                print("You flew " + str(Medium_throttle ) + "km in medium Throttle")
                                if safe_distance <= 0 :
                                    print("You have suceeded. Good job! Get of  the plane NOW! I need it for my next pilot. Good bye " + str(name))



                                    done = True
                                else:
                                    done = False
                                badguy_distance = badguy_distance - 100


                                if badguy_distance <= 0:
                                    print ("Oh!! You got captured. Hard luck. Try again next time")
                                    done = True
                                else:
                                    pass
                            else:

                                    if first_check == "A":
                                        Full_throttle = random.randrange(301,600)
                                        safe_distance = safe_distance - Full_throttle
                                        badguy_distance = 500 - random.randrange(10,50)
                                        print("You flew " + str(Full_throttle) + "km in Full Throttle")
                                        if safe_distance <= 0 :
                                            done = True
                                            print("You have suceeded. Good job! Get of  the plane NOW! I need it for my next pilot. Good bye " + str(name))
                                        else:
                                            done = False
                                        if badguy_distance <= 0:
                                            print("Oh!! You got captured. Hard luck. Try again next time")
                                            done = True
                                        badguy_distance = badguy_distance - 100


                                        if badguy_distance <= 0:
                                            print ("Oh!! You got captured. Hard luck. Try again next time")
                                            done = True
                                        else:
                                            pass
                                    else:

                                        pass

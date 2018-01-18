#CamelRun4.py
#Ved Ballary
#V.4.1.5
#last update: 4 october 2017
#Object of the game is to get across the dessert on a stolen camel while the owners are chasing you

'''
Peter Guo:
1) say good luck (Name) if they catch up to you.
    *Updated in version 4.0.9
2) Check colon. should have whenever asking for input
    *Updated in version 4.0.8
3)Check output spacing.
    *Updated in version 4.0.8
4) Maybe add how close the player was to the end game (in km or what not), i feel like it would give the player a sense of progess.
    *Kept that to increase diffculty
Paul Tang: 1) 1 grammar mistake detected ("off")
                * Updated in version 4.1.0
           2) the game does not rerquire tactics or much thinking after playing a few times to learn the rules of it, you could basically repeat a sequence of letters to win the game (easy mode).
           3) hard mode IMPOSSIBLE to beat
                *LOL
'''
import random

print ("Welcome to Plane Run")
print ("You are trying to get away from bad guys on an airplane.")
print("")
print("Good luck!")

done = False


plane_fuel = 1000
engine_heat = 0
badguy_distance = 500
safe_distance = 10241



#n_ground = raw_input("")
#if on_ground ==
name = raw_input("Enter your name: ")
print ("Choose your level:\n " + "a. Easy \n" + "b. Hard" )
level = raw_input("Ans: ")
if level.lower() == "a":

    print ("You are on easy mode\n" + "----------------")
    if safe_distance <= 0 :
        done = True
    else:
        done = False
    while not done:
        print("A. Full throttle.")
        print("----------------")
        print("B. Medium Throttle. ")
        print("----------------")
        print("C. Glide. ")
        print("----------------")
        print("D. Status Check. ")
        print("----------------")
        print("E. Quit. ")
        first_check = raw_input("Ans: ")

        if first_check.lower() == "e":
            done = True
        else:
                if first_check.lower() == "d":
                    print ("Your distance to safety is " + str(safe_distance) +"km" + "\n The fuel left in your plane is " + str(plane_fuel) + "\n The engine heat measurment is " + str(engine_heat) + "\n The badguys are " +str(badguy_distance) + "km away from you" )

                else:

                        if first_check.lower() == "c":
                            glide = random.randrange(100,150)
                            safe_distance = safe_distance - glide
                            print("You glided " + str(glide) + "km")
                            glide_count = 1
                            plane_fuel = plane_fuel - 5
                            engine_heat = engine_heat - 10
                            if safe_distance <= 0 :
                                done = True
                                print("You have suceeded. Good job! Get out of the plane NOW! I need it for my next pilot. Good bye " + str(name))
                            else:
                                done = False
                            badguy_distance = badguy_distance - 100


                            if badguy_distance <= 0:
                                print ("Oh!! You got captured. Hard luck. Try again next time " + str(name))
                                done = True

                            else:

                                if plane_fuel <= 0 :
                                    done = True
                                    print ("Hard luck. You ran out of fuel and the aircraft crashed. Good luck next time " + str(name))
                                elif plane_fuel <= 250:
                                    print("-----You are running low on fuel. Please glide or go on medium throttle-------")
                                elif plane_fuel <= 100:
                                    print ("-----Warning!-----")
                                    print ("")
                                    print ("-----You are running serioulsy low on fuel------")
                                elif plane_fuel <= 50:
                                    print ("----You are almost out of fuel-----")
                                    print("")
                                    print ("----You are going to crash any minute-----")

                                if engine_heat <= 200 and engine_heat >= 100:
                                    print ("Your engine is slightly heating up. Be careful")
                                elif engine_heat <= 300 and engine_heat >=201:
                                    print ("-----WARNING-----")
                                    print ("")
                                    print ("Your enigine heat is getting high. The engine may shut down any moment")
                                elif engine_heat >= 350 and engine_heat <= 400:
                                    print ("----ENGINE HAS OVERHEATED AND SHUT DOWN----")
                                    print ("----YOU DIED----")
                                    print ("Thanks for playing " + str(name))
                                    done = True

                        else:

                                if first_check.lower() == "b":
                                    Medium_throttle = random.randrange(150,499)
                                    safe_distance = safe_distance - Medium_throttle
                                    badguy_distance = 500 - random.randrange(60,99)
                                    plane_fuel = plane_fuel - 25
                                    engine_heat = engine_heat + 25
                                    print("You flew " + str(Medium_throttle ) + "km in medium Throttle")
                                    if safe_distance <= 0 :
                                        print("You have suceeded. Good job! Get of  the plane NOW! I need it for my next pilot. Good bye " + str(name))



                                        done = True
                                    else:
                                        done = False
                                    badguy_distance = badguy_distance - 100


                                    if badguy_distance <= 0:
                                        print ("Oh!! You got captured. Hard luck. Try again next time " + str(name))
                                        done = True
                                    else:

                                        if plane_fuel <= 0 :
                                            done = True
                                            print ("Hard luck. You ran out of fuel and the aircraft crashed " + str(name))
                                        elif plane_fuel <= 250:
                                            print("-----You are running low on fuel. Please glide or go on medium throttle-----")
                                        elif plane_fuel <= 100:
                                            print ("-----Warning!-----")
                                            print ("")
                                            print ("-----You are running serioulsy low on fuel------")
                                        elif plane_fuel <= 50:
                                            print ("----You are almost out of fuel-----")
                                            print("")
                                            print ("----You are going to crash any minute-----")
                                        if engine_heat <= 200 and engine_heat >= 100:
                                            print ("Your engine is slightly heating up. Be careful")
                                        elif engine_heat <= 300 and engine_heat >=201:
                                            print ("-----WARNING-----")
                                            print ("")
                                            print ("Your enigine heat is getting high. The engine may shut down any moment")
                                        elif engine_heat >= 350 and engine_heat <= 400:
                                            print ("----ENGINE HAS OVERHEATED AND SHUT DOWN----")
                                            print ("----YOU DIED----")
                                            print ("Thanks for playing " + str(name))
                                            done = True
                                        else:
                                            pass
                                else:

                                        if first_check.lower() == "a":
                                            Full_throttle = random.randrange(301,600)
                                            safe_distance = safe_distance - Full_throttle
                                            badguy_distance = 500 - random.randrange(10,50)
                                            plane_fuel = plane_fuel - 100
                                            engine_heat = engine_heat + 50
                                            print("You flew " + str(Full_throttle) + "km in Full Throttle")
                                            if safe_distance <= 0 :
                                                done = True
                                                print("You have suceeded. Good job! Get of  the plane NOW! I need it for my next pilot. Good bye " + str(name))
                                            else:
                                                done = False
                                            if badguy_distance <= 0:
                                                print("Oh!! You got captured. Hard luck. Try again next time " + str(name))
                                                done = True
                                            badguy_distance = badguy_distance - 100


                                            if badguy_distance <= 0:
                                                print ("Oh!! You got captured. Hard luck. Try again next time " + str(name))
                                                done = True
                                            else:

                                                if plane_fuel <= 0 :
                                                    done = True
                                                    print ("Hard luck. You ran out of fuel and the aircraft crashed " + str(name))
                                                elif plane_fuel <= 250:
                                                    print("-----You are running low on fuel. Please glide or go on medium throttle-----")
                                                elif plane_fuel <= 100:
                                                    print ("-----Warning!-----")
                                                    print ("")
                                                    print ("-----You are running serioulsy low on fuel------")
                                                elif plane_fuel <= 50:
                                                    print ("----You are almost out of fuel-----")
                                                    print("")
                                                    print ("----You are going to crash any minute-----")
                                                if engine_heat <= 200 and engine_heat >= 100:
                                                    print ("Your engine is slightly heating up. Be careful")
                                                elif engine_heat <= 300 and engine_heat >=201:
                                                    print ("-----WARNING-----")
                                                    print ("")
                                                    print ("Your enigine heat is getting high. The engine may shut down any moment")
                                                elif engine_heat >= 350 and engine_heat <= 400:
                                                    print ("----ENGINE HAS OVERHEATED AND SHUT DOWN----")
                                                    print ("----YOU DIED----")
                                                    print ("Thanks for playing " + str(name))
                                                    done = True
                                                else:
                                                    pass
                                        else:

                                            pass
else:
    print ("You are on hard mode")
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

        if first_check.lower() == "e":
            done = True
        else:
                if first_check.lower() == "d":
                    print ("Your distance to safety is " + str(safe_distance) +"km" + "\n The fuel left in your plane is " + str(plane_fuel) + "\n The engine heat measurment is " + str(engine_heat) + "\n The badguys are " +str(badguy_distance) + "km away from you" )

                else:

                        if first_check.lower() == "c":
                            glide = random.randrange(100,150)
                            safe_distance = safe_distance - glide
                            print("You glided " + str(glide) + "km")
                            pass
                            plane_fuel = plane_fuel - 1
                            engine_heat = engine_heat - 10
                            if safe_distance <= 0 :
                                done = True
                                print("You have suceeded. Good job! Get of  the plane NOW! I need it for my next pilot. Good bye " + str(name))
                            else:
                                done = False
                            badguy_distance = badguy_distance - 175


                            if badguy_distance <= 0:
                                print ("Oh!! You got captured. Hard luck. Try again next time " + str(name))
                                done = True

                            else:
                                pass
                            if plane_fuel <= 0 :
                                done = True
                                print ("Hard luck. You ran out of fuel and the aircraft crashed " + str(name))
                            elif plane_fuel <= 250:
                                print("-----You are running low on fuel. Please glide or go on medium throttle-------")
                            elif plane_fuel <= 100:
                                print ("-----Warning!-----")
                                print ("")
                                print ("-----You are running serioulsy low on fuel------")
                            elif plane_fuel <= 50:
                                print ("----You are almost out of fuel-----")
                                print("")
                                print ("----You are going to crash any minute-----")

                            if engine_heat <= 200 and engine_heat >= 100:
                                print ("Your engine is slightly heating up. Be careful")
                            elif engine_heat <= 300 and engine_heat >=201:
                                print ("-----WARNING-----")
                                print ("")
                                print ("Your enigine heat is getting high. The engine may shut down any moment")
                            elif engine_heat >= 350 and engine_heat <= 400:
                                print ("----ENGINE HAS OVERHEATED AND SHUT DOWN----")
                                print ("----YOU DIED----")
                                print ("Thanks for playing " + str(name))
                                done = True

                        else:

                                if first_check.lower() == "b":
                                    Medium_throttle = random.randrange(150,499)
                                    safe_distance = safe_distance - Medium_throttle
                                    badguy_distance = 500 - random.randrange(60,99)
                                    plane_fuel = plane_fuel - 25
                                    engine_heat = engine_heat + 35
                                    print("You flew " + str(Medium_throttle ) + "km in medium Throttle")
                                    if safe_distance <= 0 :
                                        print("You have suceeded. Good job! Get of  the plane NOW! I need it for my next pilot. Good bye " + str(name))



                                        done = True
                                    else:
                                        done = False
                                    badguy_distance = badguy_distance - 100


                                    if badguy_distance <= 0:
                                        print ("Oh!! You got captured. Hard luck. Try again next time " + str(name))
                                        done = True
                                    else:
                                        pass
                                    if plane_fuel <= 0 :
                                        done = True
                                        print ("Hard luck. You ran out of fuel and the aircraft crashed")
                                    elif plane_fuel <= 250:
                                        print("-----You are running low on fuel. Please glide or go on medium throttle-----")
                                    elif plane_fuel <= 100:
                                        print ("-----Warning!-----")
                                        print ("")
                                        print ("-----You are running serioulsy low on fuel------")
                                    elif plane_fuel <= 50:
                                        print ("----You are almost out of fuel-----")
                                        print("")
                                        print ("----You are going to crash any minute-----")
                                    if engine_heat <= 200 and engine_heat >= 100:
                                        print ("Your engine is slightly heating up. Be careful")
                                    elif engine_heat <= 300 and engine_heat >=201:
                                        print ("-----WARNING-----")
                                        print ("")
                                        print ("Your enigine heat is getting high. The engine may shut down any moment")
                                    elif engine_heat >= 350 and engine_heat <= 400:
                                        print ("----ENGINE HAS OVERHEATED AND SHUT DOWN----")
                                        print ("----YOU DIED----")
                                        print ("Thanks for playing" + str(name))
                                        done = True
                                    else:
                                        pass
                                else:

                                        if first_check.lower() == "a":
                                            Full_throttle = random.randrange(301,600)
                                            safe_distance = safe_distance - Full_throttle
                                            badguy_distance = 500 - random.randrange(10,50)
                                            plane_fuel = plane_fuel - 100
                                            engine_heat = engine_heat + 65
                                            print("You flew " + str(Full_throttle) + "km in Full Throttle")
                                            if safe_distance <= 0 :
                                                done = True
                                                print("You have suceeded. Good job! Get of  the plane NOW! I need it for my next pilot. Good bye " + str(name))
                                            else:
                                                done = False
                                            if badguy_distance <= 0:
                                                print("Oh!! You got captured. Hard luck. Try again next time " + str(name))
                                                done = True
                                            badguy_distance = badguy_distance - 125


                                            if badguy_distance <= 0:
                                                print ("Oh!! You got captured. Hard luck. Try again next time " + str(name))
                                                done = True
                                            else:
                                                pass
                                            if plane_fuel <= 0 :
                                                done = True
                                                print ("Hard luck. You ran out of fuel and the aircraft crashed " + str(name))
                                            elif plane_fuel <= 250:
                                                print("-----You are running low on fuel. Please glide or go on medium throttle")
                                            elif plane_fuel <= 100:
                                                print ("-----Warning!-----")
                                                print ("")
                                                print ("-----You are running serioulsy low on fuel------")
                                            elif plane_fuel <= 50:
                                                print ("----You are almost out of fuel-----")
                                                print("")
                                                print ("----You are going to crash any minute-----")
                                            if engine_heat <= 200 and engine_heat >= 100:
                                                print ("Your engine is slightly heating up. Be careful")
                                            elif engine_heat <= 300 and engine_heat >=201:
                                                print ("-----WARNING-----")
                                                print ("")
                                                print ("Your enigine heat is getting high. The engine may shut down any moment")
                                            elif engine_heat >= 350 and engine_heat <= 400:
                                                print ("----ENGINE HAS OVERHEATED AND SHUT DOWN----")
                                                print ("----YOU DIED----")
                                                print ("Thanks for playing " + str(name))
                                                done = True
                                            else:
                                                pass
                                        else:

                                            pass

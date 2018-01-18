#CamelRun.py
#Ved Ballary
#V.0.0.1
#last update: 28 september 2017
#Object of the game is to get across the dessert on a stolen camel while the owners are chasing you
print ("Welcome to Plane Run")
print ("You are trying to get away from bad guys on an airplane.")
print("")
print("Good luck!")

done = False

thirst = 30
hunger = 20
plane_fuel = 20
engine_heat = 40
badguy_distance = 0


#n_ground = raw_input("")
#if on_ground ==


while not done:
    print("A. Full throttle.")
    print("B. Medium Throttle. ")
    print("C. Glide. ")
    print("D. Status Check. ")
    print("E. Quit. ")
    first_check = raw_input("")

    if first_check  == "Quit" :
        done = True
    else

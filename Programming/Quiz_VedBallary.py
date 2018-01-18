'''
This is a quiz
'''
#VedBallary
#Quiz_VedBallary.py
#25/9/2017
#V0.5.0.6
total_score = 0
print ("Welcome to the most confusing quiz")
name = raw_input("What is your name? ")
entry = raw_input("Type 'let's begin' to start: ")


if entry.lower() == "let's begin":
    print  ("The game has begun")
    print  ("")
    print  ("Good luck")

    '''
    Question 1
    '''
    print ("Where in the world is Carmen Sandiego?")
    print ("a. In South Africa")
    print ("b. In New Mexico")
    print ("c. On the National Geographic channel")
    print ("d. In Spain")

    question_1 = raw_input("Ans: ")

    if question_1 == "c":
        print ("Correct")
        total_score =total_score + 1

    else:
        print ("Wrong")
        print ("The answer is c")
        print ("")
        print ("Where in the World is Carmen Sandiego is a TV show")

    print ("You score is" + " " + str(total_score))

    '''
    Question 2
    '''
    print ("What is the capital in Japan?")

    question_2 = raw_input("Ans: ")

    if question_2 == ("J") :
        print("You are a genius!")
        total_score = total_score + 1
    else:
        print ("Ohhh! That's the wrong answer =(")
        print ("The right answer is 'J'")


    print ("You score is" + " " + str(total_score))

    '''
    Question 3
    '''
    print ("John is 20 years old. His sister is 10 years old. In 20 years, if John is 40, how old are you? ")
    print("")

    question_3 = raw_input("Ans:")

    if question_3 == ("20"):
        print ("That's wrong")
    else:
        print ("You have a great mind. That's right")
        total_score = total_score + 1
    print ("Your score is" + " " + str(total_score))

    '''
    Question 4
    '''
    print ("What is the 7th letter of the alphabet?")
    print("")

    question_4 = raw_input("Ans: ")

    if question_4 == "e" or question_4 == "E":
        print ("You are on fire!")
        total_score = total_score + 1

    else :
        print ("that's wrong")
    print ("Your score is"+ " " + str(total_score))

    '''
    Question 5
    '''
    print ("If a Mr.Mo's rooster laid an egg in Mr.Quesly's backyard, whose egg is it")

    question_5 = raw_input("Ans: ")

    if question_5 == "Mr.Quesly's" or question_5 == "Mr.Mo's" or question_5 == "Mr.Mo" or question_5 == "Mr. Quesly":
        print("Error rooster's cannot lay eggs")
    else:
        print ("You are right. Roosters cannot lay eggs")
        total_score=total_score + 1

    total_score1 = (float(total_score) / 5) * 100

    if total_score1 <= 40.0:
        print ("Nice try " + str(name)  + ". Try harder next time. Thanks for playing " + str(name) + ".")
    elif total_score1 <= "79.0%":
        print ("That's okay" + " " + str(name) + "Just a little bit more effort and you'll be there." + " " + "Thanks for playing" + " " + str(name))
    else:
        print ("That's an awesome score" + " " + str(name) + "You are a mastermind. You did a great job" + " " + "Thanks for playing" + " " + str(name))


    print("You final score is: " + str(total_score1) + "%")

else:
    print ("You are a coward")

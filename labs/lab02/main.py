# Starting file for LAB 2
# Include your course number, student first and last name, and date in the comment header
# CS 31 Josh L. 10-7-26

print("My Quiz on RANDOMNESS")
print() # prints an empty line
print("* " * 20) #print a line of 20 astericks


# Ask for the user's name
print()
username = input("What is your name? ")
print(f"Hello, {username}!") #f-string format

# Ask if they want to take a quiz
print()
start_quiz = input("Do you want to take my random quiz? Y/N ")
if start_quiz.upper() == "Y": #if the student inputs a lower case you can do if start_quiz.upper()
    print("Great! Let's get started!")
    # put our quiz questions here all indented
    # #START OUR QUIZ QUESTIONS

    # Set out counter to 0
    counter = 0

    # Question 1
    print()
    print(">>>>QUESTION 1<<<<")
    q1 = int(input("How would Python solve 5 * 5? "))
    if q1 == 25:
        # update my counter
        counter += 1 #shorthand for counter = counter + 1
        print("Yes! You are correct. Python would solve this as 25.")
    else: #INCORRECT
        print("Sorry. That is not correct. ")

    # Question 2
    print()
    print(">>>>QUESTION TWO<<<<")
    print("What is the function that we use to output something to the terminal?")
    print(" A - output()")
    print(" B - print()")
    print(" C - format()")
    print(" D - None of the above")
    q2 = input ("Your Answer - Choose A/B/C/D: ")
    if q2.upper() == "B":
        #update my counter because they got the answer right
        counter += 1 # shorthand for counter = counter + 1
        print("Yes! You are correct. Python would use the print() function to output something to the terminal.")
    else: #INCORRECT
        print("Sorry. That is not correct. ")
    # Question 3
    print()
    print(">>>>QUESTION 3 :)<<<<")
    print("What is another way to print a string with a variable within it?")
    print(" A - f-string format")
    print(" B - camelCasing()")
    print(" C - print")
    print(" D - sudo apt")
    q3 = input ("Choose answer please...")
    if q3.upper() == "A":
            #update my counter because they got the answer right
            counter += 1 # shorthand for counter = counter + 1
            print("Yes! You are correct!")
    else:  #INCORRECT
            print("Sorry. Not even close...")
    # Question 4
    print()
    print(">>>>QUESTION 4<<<<")
    print("Which hero is the best?")
    print(" A - Superman")
    print(" B - Batman")
    print(" C - Joker")
    print(" D - Hulk")    
    q4 = input ("Choose answer please...")
    if q4.upper() == "B":
                #update my counter because they got the answer right
                counter += 1 # shorthand for counter = counter + 1
                print("Yes! You are correct!")
    else:  #INCORRECT
                print("Sorry. Not even close...")
    # Question 5
    print()
    print(">>>>QUESTION 5<<<<")
    print("If i were to turn around, how many degrees is that?")
    print(" A - 180")
    print(" B - 360")
    print(" C - 500")
    print(" D - 100")    
    q5 = input ("Choose answer please...")
    if q5.upper() == "A":
                    #update my counter because they got the answer right
                    counter += 1 # shorthand for counter = counter + 1
                    print("Yes! You are correct!")
    else:  #INCORRECT
                    print("Sorry. Not even close...")

    # Output the score
    print("* * * * YOUR FINAL SCORE * * * *")
    print(f"Your final score is: {counter}")#f-string format


    # Give them feedback on their overall score
    if counter == 5:
        print("You are big brain!")
    elif counter >= 3 and counter < 5:
        print("Super mid bro.")
    elif counter >=1 and counter < 3:
        print("not good brobro.")
    else:
        print("Did you even try?")


elif start_quiz.upper() == "N":#if the student inputs a lower case you can do if start_quiz.upper()
    print("Sorry, maybe next time!")

else: #if they type anything else tell them its invalid
    print("Sorry. That is an invalid response. Try again.")

# print a farewell message
print("Bye bye have great time.")


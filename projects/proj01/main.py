# Starting file for PROJECT 1
# Include your course number, student first and last name, and date in the comment header
# CS 31 - 72473 Josh Lucero 11/21/26
#Programming Project 1: Simulated Sales Pitch

print("~~~~Hello, I am spaghetti.io. Would you like some spaghetti?~~~~~")
start_sales = input("Y or N   ")
if start_sales.upper() == "Y":
    print("The spaghetti.io gives spaghetti *laughs in robot* ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("It all started in the year 2026, when spagolfo was interested in the advancement of...")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("... the spaghetti robots, long since then we have been called the spaghetti.io")
    print(" so are you interested in our spaghetti?   ")

    #we input the customer's purchase decision and check if they want to buy spaghetti or not
    user_purchase = input("Y or N")
    if user_purchase.upper() == "Y":
        # We now ask for their information
        print ("Awesome, now I need a few bits of information from you.")
        firstName = input("What is your first name?   ")
        lastName = input("What is your last name?   ")
        emailAddress = input("What is your email address? ")
        phoneNumber = input("What's your phone number?   ")
        print (" I will tell you that the spaghetti is $20 per unit.  ")


        #we ask for how many units they want to purchase and calculate the total cost
        unitsPurchased = int(input("How many spaghett.io would you like to purchase? "))
        totalCost = int(unitsPurchased * 20)
        total = int(totalCost * 0.1)
        print("Your total cost is: $", totalCost, "with tax hahahaha")
        print("================================================================")
        print("                  RECEIPT                                       ")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Thank you for your trying my spaghetti.io", firstName, lastName)
        print(emailAddress + phoneNumber)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Subtotal: $", totalCost)
        print("Tax: $0.1")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Total: $", total + totalCost)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

        print("It was a pleasure doing business with you, please visit again!")




    elif user_purchase.upper() == "N":
        print("aww okay... goodbye!")
else:
    print("It's okay, maybe you'll come back! ")
    

    
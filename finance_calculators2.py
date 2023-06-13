import math

print("investment - to calculate the amount of interest you'll earn on your investment\n")
print("bond - to calculate the amount you'll have to pay on a home loan\n")

calculation = input("Enter either 'investment' or 'bond' from the menu above to proceed: \n")

calculation = calculation.lower() #changes string to lower case so user can input upper or lowercase without causing an error

if "investment" in calculation:
    money = int(input("\nHow much to invest?: "))
    interest_rate = int(input("What is the interest rate(value only)?: "))
    years = int(input("For how many years?: "))
    
    interest = input("Do you want simple or compound?: ")
    interest = interest.lower()
   
    
    interest_rate = interest_rate / 100
    
    
    if "compound" in interest:
        total = money * math.pow((1+interest_rate), years) #calc for profit from compound interest
        total = "{:.2f}".format(total)
        print("\nThe total amount including interest after", years, "years is £",total)
        
    
    elif "simple" in interest:
        total = money * (1+interest_rate*years) #calc for profit from simple interest
        total = "{:.2f}".format(total)
        print("\nThe total amount including interest after", years, "years is £",total)
        
    elif "simple" not in interest:
        print("Please choose between simple or compound investment")
    
elif "bond" in calculation:
    house_value = int(input("What is the value of your house?: "))
    interest_rate = int(input("What is the interest rate on the property?: "))
    repay_length = int(input("How many months do you intend to make repayments?: "))
    
    interest_rate = interest_rate / 100
    
    interest_rate = interest_rate / 12
    
    repayment = (interest_rate * house_value)/(1-(1+interest_rate)**(-repay_length)) #calc for total amount to be repaid
    repayment = "{:.2f}".format(repayment)
    print("\nThe amount you have to repay each month for", repay_length, "months is £",repayment)
    
else:
    print("Oops, something went wrong! You can only choose bond or investment")
    
    #bond repayment does not seem right, copied math for the bond and seems unusually large. used math calculator for original formula with same result but wondering if typo if it is month or year? Sorry mentor sessions take a month to book in advance.
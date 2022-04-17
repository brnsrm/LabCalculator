#Addition
def addition(a,b):
    result = a + b
    return result

#Subtraction
def subtraction(a,b):
    result = a - b
    return result

#Multiplication
def multiplication(a,b):
    result = a * b
    return result

#Division
def division(a,b):
    result = a / b
    return result

#Percentage
def percentage(a,b):
    result = (a * b) / 100
    return result

print("Which calculation do you want to execute?")
print("Following Options: 1. Addition, 2. Subtraction, 3. Multiplication, 4. Division, 5. Percentage")

secondcalculation = ""

while not secondcalculation == "no":
    #Input of the user - choice of calculation
    try:
        choice = input("Enter choice (1, 2, 3, 4 or 5):")
    except:
        print("Unknwon choice!")
        continue
        
    #Input of user - adding numbers
    if choice in("1", "2", "3", "4", "5"):
        try:
            num1 = float(input("Enter first number:"))
            num2 = float(input("Enter second number:"))
        except:
            print("That is not a number!")
            continue

        #Calculation Options
        if choice == "1":
            print(num1, "+", num2, "=", addition(num1,num2))
        elif choice == "2":
            print(num1, "-", num2, "=", subtraction(num1,num2))
        elif choice == "3":
            print(num1, "*", num2, "=", multiplication(num1,num2))
        elif choice == "4":
            print(num1, "/", num2, "=", division(num1,num2))
        elif choice == "5":
            print((num1, "*", num2),"/", "100", "=", percentage(num1,num2))
        
        #Ask for another calculation
        secondcalculation = input("Do you want to do another calculation?: (Yes/No)")







# Python Syntax Assignment

#1.1 Code Correction

weather = "sunny"

if weather == "sunny":
    print("Wear sunglasses!")
else:
    print("Take an umbrella!")

#1.2 Your Mood Today

userAnswer = input("How are you feeling today?\n")
if userAnswer == "happy":
    print("That's great to hear!");
elif userAnswer == "sad":
    print("I hope your day gets better!")
else:
    print("... Oooookay then!");

#2.1 Code Correction

PI_VALUE = 3.14
userAge = 25
user_location = "New York"
MAX_LIMIT = 1000

#3.1 Code Correction

variable_a = "Hello, World!"
variable_b = 23
variable_c = 3.14
variable_d = True

print(type(variable_a))
print(type(variable_b))
print(type(variable_c))
print(type(variable_d))

#4.1 Grocery Store Math

bread, eggs, bacon = 1.39, 6.00, 6.99
totalPrice = bread + eggs + bacon
print('${:,.2f}'.format(totalPrice)) #formatting the float into currency

#4.2 Bank Interest

savingsAmount = 500
INTEREST_RATE = 0.07
interestAmount = savingsAmount * INTEREST_RATE # <-- 35
savingsAmount += interestAmount
print('${:,.2f}'.format(savingsAmount))

#5.1 Value Swapping

num1 = 10
num2 = 5

num1 = 5
num2 = 10

if num1 == 10 and num2 == 5:
    print("It never changed...")
else:
    print("It was swapped!")

#6.1 Validating Calculations



#6.2 Mix & Match
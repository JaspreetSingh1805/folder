# user = int(input("Enter here a user score: "))
# if user < 13:
#     print("He/she is a child")
# elif   13 < user <18 :
#     print("He/she is teenager")
# elif  20 < user < 60:
#     print("He/she is Adult")
# elif user > 60:
#     print("He/she is Senior citizen")

# age = int(input("Enter a age here: "))
# day = "Wednesday"
# price = 12 if age >= 18 else 10
# if day=="Wednesday":
#     price -= 2
# print("Ticket price for you is $",price)

# fruit = input("Enter the color of banana: ")
# if fruit == "green":
#     print("banana is Unripe")
# elif fruit == "Yellow":
#     print("banana is Ripe")
# elif fruit == "Brown":
#     print("Banana is Overripe")


# order_size = "Medium"
# extra_shot = True
# if extra_shot:
#     coffee = order_size + " coffee with an extra shot"
# else: 
#     coffee = order_size + " coffee"
# print(" Order: ", coffee)

# password = input("Enter your password here: ")
# if 0 <  len(password) <= 6:
#     print("Weak password")
# elif   6 < len(password) < 10:
#     print("Medium password") 
# elif len(password) > 10:
#     print("Strong password")

# year = int(input("Enter a year here "))
# if year%4==0:
#     print("This year is leap year")
# elif year%100!=0:
#     print("This is not a leap year")
# elif year%400==0:
#     print("This is leap year")

species = str(input("Enter which type of species your pet is (e.g., dog, cat): ")).lower()
age = int(input("Enter the age of your pet: "))
try:
    if species == "dog":
      if age <= 2:
        print("Puppy food")
      else:
        print("Senior dog food")

    elif species == "cat":
       if age <= 2:
        print("Kitten food")
       else:
        print("Senior cat food")
    else:"cant recomended the food"
except:
    print("BKL Dalal")



    

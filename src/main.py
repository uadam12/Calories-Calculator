print ("Welcome to Calories Calculator\n")

fat = int(input("Enter weight of fats in kg:- "))
carbohydrates = int(input("Enter weight of carbohydrates in kg:- "))

caloriesFromFats = 9 * fat
caloriesFromCarbohydrates = 4 * carbohydrates

print ()
print ("Number of calories from fats:-", caloriesFromFats)
print ("Number of calories from carbohydrates:-", caloriesFromCarbohydrates)

print ("Bye")
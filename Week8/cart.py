
#Create a shopping cart programme that will continuously ask the user for a food prooduct and price for that product
#Have an exit clause if the user wishes to stop adding more things to thier chart
#At the end show the food iteams and the total cost to the user

foods = []
prices =  []
total = 0

while True:
    food = input("Enter a food to buy or press q to quit: ")
    if food.lower() == 'q':
       break 
    else:
        price = float(input(f"Enter the price of the {food}: R"))
        foods.append(food)
        prices.append(price)
        
        
print("-----YOUR CART-----")

for food in foods:
    print(food)
    
    for price in prices:
        total += price
        
print(f"Your total is: R{total}")
        
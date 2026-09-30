# PIZZA COST CALCULATOR

print("Welcome to the Pizza Cost Calculator!")
print("------------------------------------------")

print("\nPizza Sizes:")
print("1. Small       - $10.00")
print("2. Medium      - $12.00")
print("3. Large       - $15.00")
print("4. Extra Large - $18.00")

size = int(input("\nChoose a pizza size (1-4): "))

if size == 1:
    pizza_name = "Small"
    pizza_price = 10.00

elif size == 2:
    pizza_name = "Medium"
    pizza_price = 12.00

elif size == 3:
    pizza_name = "Large"
    pizza_price = 15.00

elif size == 4:
    pizza_name = "Extra Large"
    pizza_price = 18.00

else:
    print("Invalid pizza size.")
    exit()

print("\nToppings:")
print("1. Pepperoni        - $1.50")
print("2. Sausage          - $1.50")
print("3. Bacon            - $1.50")
print("4. Pineapple        - $1.50")
print("5. Mushrooms        - $1.00")
print("6. Onions           - $1.00")
print("7. Green Peppers    - $1.00")
print("8. Banana Peppers   - $1.00")
print("9. Jalapeno Peppers - $1.00")
print("10. Extra Cheese    - $1.00")
print("0. No more toppings")

topping_total = 0
topping_list = []

while True:

    topping = int(input("\nChoose a topping (0 when finished): "))

    if topping == 0:
        break

    elif topping == 1:
        topping_total = topping_total + 1.50
        topping_list.append("Pepperoni")

    elif topping == 2:
        topping_total = topping_total + 1.50
        topping_list.append("Sausage")

    elif topping == 3:
        topping_total = topping_total + 1.50
        topping_list.append("Bacon")

    elif topping == 4:
        topping_total = topping_total + 1.50
        topping_list.append("Pineapple")

    elif topping == 5:
        topping_total = topping_total + 1.00
        topping_list.append("Mushrooms")

    elif topping == 6:
        topping_total = topping_total + 1.00
        topping_list.append("Onions")

    elif topping == 7:
        topping_total = topping_total + 1.00
        topping_list.append("Green Peppers")

    elif topping == 8:
        topping_total = topping_total + 1.00
        topping_list.append("Banana Peppers")

    elif topping == 9:
        topping_total = topping_total + 1.00
        topping_list.append("Jalapeno Peppers")

    elif topping == 10:
        topping_total = topping_total + 1.00
        topping_list.append("Extra Cheese")

    else:
        print("Invalid topping choice.")

# Calculate subtotal

subtotal = pizza_price + topping_total

# Student Discount

student = input("\nAre you a student? (yes/no): ")

if student.lower() == "yes":
    discount = subtotal * 0.10
else:
    discount = 0

price_after_discount = subtotal - discount

# Pickup or Delivery

delivery = input("\nDo you want delivery? (yes/no): ")

if delivery.lower() == "yes":
    delivery_charge = price_after_discount * 0.20
else:
    delivery_charge = 0

# Calculate total before tip

total_before_tip = price_after_discount + delivery_charge

# Tip

tip_choice = input("\nWould you like to add a tip? (yes/no): ")

if tip_choice.lower() == "yes":
    tip_percent = float(input("Enter tip percentage: "))
    tip = total_before_tip * (tip_percent / 100)
else:
    tip_percent = 0
    tip = 0

# Final total

total = total_before_tip + tip

# Receipt

print("\n")
print("==========================================")
print("              PIZZA RECEIPT")
print("==========================================")

print("Pizza Size:       ", pizza_name)
print("Pizza Price:      $", format(pizza_price, ".2f"))

print("\nToppings:")

if len(topping_list) == 0:
    print("  No additional toppings")
else:
    for item in topping_list:
        print("  -", item)

print("\nTopping Cost:     $", format(topping_total, ".2f"))
print("Subtotal:         $", format(subtotal, ".2f"))
print("Student Discount: $", format(discount, ".2f"))
print("Delivery Charge:  $", format(delivery_charge, ".2f"))
print("Tip:              $", format(tip, ".2f"))

print("------------------------------------------")
print("TOTAL:            $", format(total, ".2f"))
print("==========================================")

print("\nThank you for your order!")
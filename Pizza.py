print("Welcome to Python Pizza Deliveries!")
size = input("what size pizza do you want? S,M,, or L = ")

add_pepperoni = input("Do you want pepperoni? Y or N = ")

extra_cheese = input("Do you want extra cheese? Y or N = ")

# condition 1:
# Small Pizza : $15
# medium Pizza : $ 20
# Large Pizza: $ 25

# condetion 2: 
# pepperoni for Small Pizza : +$2
# pepperoni for Small Pizza : +$3

# condition 3: 
# Extra cheese for any size pizza: +$1

# condition 1:
bill=0

if size == 'S' or size == 's':
    bill=15
elif size == 'M' or size == 'm':
    bill = 20
else:
    bill = 25
 
# condition 2: 
if add_pepperoni == 'Y' or add_pepperoni == 'y':
    if size == 'S' or size == 's':
        bill+=2
    else: bill+=3
 
# condition 3: 
if extra_cheese == 'Y' or extra_cheese == 'y':
    bill+=1
    
else: bill+=0   
    
    
print(f"Your final bill is {bill}")    





print('Welcome to the tip calculator.\n ')
bill = float(input('What was total bill? = '))
presentage = int(input("What presentage tip would you give? 10 ,12 or 15 = "))
bilByPeople = int(input("How many people to split the bill? = "))

trp_as_presentage = presentage /100
trip_amount = bill * trp_as_presentage
totall_bill = bill + trip_amount
perperson = totall_bill / bilByPeople
final_amount = round(perperson,2)

print(f"every one pay: $ {final_amount}");




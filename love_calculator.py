print("Welcome to the Love Calcutor!")
name1 = input("What is your nam? ")
name2 = input("What is their name? ")

combined_string = name1 + name2

lower_case = combined_string.lower()

print(lower_case)

t= lower_case.count("t")
r= lower_case.count("r")
u= lower_case.count("u")
e= lower_case.count("e")

true = t + r + u +e

l= lower_case.count("l")
o= lower_case.count("o")
v= lower_case.count("v")
e= lower_case.count("e")

love = l + o + v + e

love_score = int(str(true) + str(love))

if love_score < 10 or love_score > 90:
    print(f"your love score is {love_score}")

elif love_score >= 40 and love_score <= 50 :
    print(f"your score is {love_score},you are alright together.")

else:
    print(f"Your score is {love_score}")
     
    

print(love_score)


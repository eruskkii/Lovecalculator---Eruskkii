# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name_combined = name1 + name2
name1_l = name_combined.lower()


# This for when you want to combine counts. 
# Count for "true"
name1_tcount = name1_l.count('t') + name1_l.count('r') + name1_l.count('u') + name1_l.count('e') 
# Count for "love"
name1_locount= name1_l.count('l') + name1_l.count('o') + name1_l.count('v') + name1_l.count('e')

# Use this if you want to add the counts together like normal maths calculations. 
# name2_count = name2_l.count('t') + name2_l.count('r') + name2_l.count('u') + name2_l.count('e') + name2_l.count('l') + name2_l.count('o') + name2_l.count('v')

lovescore = str(name1_tcount) + str(name1_locount)
lovescore_int = int(lovescore)

if lovescore_int < 10 or lovescore_int > 90:
    print (f"Your score is {lovescore}, you go together like coke and mentos.")
elif lovescore_int >=40 and lovescore_int<=50:
    print(f"Your score is {lovescore}, you are alright together.")
else:
    print(f"Your score is {lovescore}.")


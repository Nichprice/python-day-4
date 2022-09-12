import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

list_size = len(names) - 1

random_person = random.randint(0, list_size)

print(f"{names[random_person]} has to pay")

# OR
one_person = random.choice(names)

print(f"{one_person} has to pay")
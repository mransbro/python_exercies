age = input("How old are you? ")

age = int(age)

if age < 18:
    print("Sorry too young to enter")
elif age >= 21:
    print("You are old, normally entry for you")
else:
    print("Old enough to enter but too young to drink")

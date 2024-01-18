age = int(input("How old are you"))

if age == 100:
    print("you are an elder")
elif age >= 18:
    print("You are an adult")
elif age < 0:
    print("You are not born yet")
else:
    print("you are a kid")
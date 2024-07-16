import random

temperature = random.randrange(0,40)

print("Temperature: " + str(temperature))

if temperature > 30:
    print("It's very hot today!")
elif temperature < 10: # (0, 10)
    print("It's very cold today!")
else: # (10 , 29)
    print("It's lovely today!")
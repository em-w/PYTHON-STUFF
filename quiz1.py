import random
x = random.randrange(1, 100)
print(x)

if x % 17 == 0:
    print("Clydesdale")

if x % 3 == 0:
    print("Arabian")

if x > 90:
    print("Shetland")

if x % 2 == 0:
    print("Thoroughbred")
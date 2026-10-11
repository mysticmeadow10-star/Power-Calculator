# Power Calculator

base = int(input("Enter the base number: "))
exponent = int(input("Enter the exponent (power): "))

result = 1

for i in range(exponent):
    result = result * base

print("The answer is:", result)
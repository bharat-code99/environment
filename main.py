import math

num = int(input("Enter a number: "))

print("Divisors are: ")

count = 0

for i in range(1, int(math.sqrt(num))+1):
    count += 1
    if num % i == 0:
        print(i)
        if i != num // i:
            print(num // i)

print(f"\nLoop ran: {count} times")
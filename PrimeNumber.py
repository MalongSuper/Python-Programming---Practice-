# This program checks if a number is prime
print("Prime Number")
number = int(input("Enter a number: "))
is_prime = True

# Check for prime number
if number == 0 or number == 1:  # Number 0 and 1 are not prime
    print(f"{number} is not a prime number")
elif number > 1:
    # Check for factor
    for i in range(2, number):
        if (number % i) == 0:  # If a factor is encountered
            is_prime = False
            break

# Display the result
if is_prime:
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")
    
#Print Alternate Prime Numbers till 20
#A Prime Number is a number that can only be divided by itself and 1 without remainders (e.g., 2, 3, 5, 7, 11).

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

user_input = int(input("give the upper limit: "))

primes = []
for num in range(2, user_input + 1):
    if is_prime(num):
        primes.append(num)

print(f"\nprimes from 1 to {user_input}:")
print(primes)

print("\nevery second prime number:")
for i in range(0, len(primes), 2):
    print(primes[i], end=" ")

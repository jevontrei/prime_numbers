import math
import os
os.system('clear')

# Use num**0.5 or num**(1/2) for sqrt?
# x = input("Enter an integer greater than 1: ")

# The fundamental theorem of arithmetic: every natural number greater than 1 is either a prime itself or can be factorized as a product of primes that is unique up to their order.

# Is it prime?


def is_it_prime(num):
    """_summary_

    Args:
        num (_type_): _description_

    Returns:
        _type_: _description_
    """

    if num < 2:
        return f"N/A. Integer must be greater than 1."
    elif num == 2:
        return "Prime"
    else:
        for n in range(2, int(num**0.5)+1):
            if num % n == 0:
                return "Composite"
        return "Prime"

# Universal print number:
examples = 10

# Show whether n is prime or composite:
# for k in range(examples):
#     result = is_it_prime(k)
#     print(f"{k}: {result}")

print("-----------------------------")
# Print all primes up to n:
# print("The prime numbers are:")
# for k in range(examples):
#     if is_it_prime(k) == "Prime":
#         print(k)

print("-----------------------------")
# Prime factors


def find_factors(num, fn):
    """_summary_

    Args:
        num (_type_): _description_
        fn (function): _description_

    Returns:
        _type_: _description_
    """

    ans = fn(num)
    if ans == f"N/A. Integer must be greater than 1.":
        return ans
    elif ans == "Prime":
        return "Prime."
    else:
        factors = [1]
        for n in range(1, int(num / 2) + 1):
            if fn(n) == "Prime" and num % n == 0:
                factors.append(n)
        return factors


# for k in range(examples):
#     factors = find_factors(k, is_it_prime)
#     if factors == "N/A. Integer must be greater than 1.":
#         print(f"{k}: N/A; Integer must be greater than 1.")
#     elif factors == "Prime.":
#         print(f"{k}: Prime.")
#     else:
#         print(f"{k}: Factors are {factors}")


print("-----------------------------")
# Prime factorisation


def prime_factorisation(num, fn):
    """_summary_

    Args:
        num (_type_): _description_
        fn (function): _description_

    Returns:
        _type_: _description_
    """

    factors = fn(num, is_it_prime)

    if factors == f"N/A. Integer must be greater than 1.":
        print()
        return f"N/A; {num} is less than 2."

    elif factors == "Prime.":
        print()
        return f"N/A; {num} is prime."

    else:
        # Prime factor decomposition = PFD
        pfd = f""
        for p in factors:
            if p > 1:
                exp = int(math.log(num, p))
                if exp == 1:
                    pfd += str(p) + " * "
                else:
                    pfd += str(p) + f"^{exp}" + " * "
        print()
        print(factors)
        return f"The prime factorisation of {num} is: {pfd[:-3]}."


# This isn't working! it prints e.g. "[1, 3] \n The prime factorisation of 9 is: 3^2.":
for k in range(examples):
    result = prime_factorisation(k, find_factors)
    print(result)

# To test a single number:
# print(prime_factorisation(4, find_factors))


print("-----------------------------")
# Try these Mersenne primes:
# m = 2**3 - 1
# print(prime_factorisation(m, find_factors))

# m = 2**7 - 1
# print(prime_factorisation(m, find_factors))

# m = 2**31 - 1
# print(prime_factorisation(m, find_factors))

print("-----------------------------")

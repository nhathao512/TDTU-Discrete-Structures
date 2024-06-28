def extended_euclid(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        gcd, x, y = extended_euclid(b % a, a)
        return (gcd, y - (b // a) * x, x)

def inverse_modulo(a, b):
    gcd, x, y = extended_euclid(a, b)
    if gcd == 1:
        return f"inverse_modulo({a}, {b}) is: {x%b}"
    else:
        return f"The GCD of {a} and {b} is not 1, so {a} does not have a modular inverse modulo {b}."
    
# TestCase
print(inverse_modulo(20, 23))
# Result: inverse_modulo(20, 23) is : 15

print(inverse_modulo(15, 20))
# Result: The GCD of 15 and 20 is not 1, so 15 does not have a modular inverse modulo 20.

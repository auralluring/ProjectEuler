"""
The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit number, 134217728=8^9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
"""

def powerful_digit_counts(power_upper_limit: int) -> int:
    matches : int = 1
    for power in range(1, power_upper_limit+1):
        base : int = 2
        while len(str(base ** power)) < power:
            base += 1
        
        while len(str(base ** power)) == power:
            matches += 1
            base += 1
    return matches


print(powerful_digit_counts(100))
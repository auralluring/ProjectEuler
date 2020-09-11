def doubleBasePalindrome(num):
    binary = bin(num)[2:]
    return binary == binary[::-1] and str(num) == str(num)[::-1]
total = 0
for n in  range(1, 1000000):
    if doubleBasePalindrome(n):
        total += n
print(total)

#done!
def abundant(num):
    factors = [f for f in range(1, num) if num % f == 0]
    if  num < sum(factors):
        return True
    else:
        return False

from math import sqrt
def divisors(n):
	"""This function will generate 
	divisors of given number
	Example: divisors(28) will give
	[1,2,4,7,14]"""
	divs = [1]
	for i in range(2,int(sqrt(n))+1):
		if n%i == 0:
			divs.extend([i,n/i])
	return list(set(divs))

#list to store the values of abundant numbers
ab = []

#For loop to generate the abundant numbers
for i in range(12,28123):
	if sum(divisors(i))>i:
		ab.append(i)
sums = [x for x in range(1, 28123)]
for a in range(len(ab)):
    for b in range(a, len(ab)):
        if ab[a] + ab[b] < 28123:
            sums[ab[a] + ab[b] - 1] = 0
        else:
            break

print(sum(sums))

#first let us assume all the numbers are 
#not sum of abundant numbers
non_ab_sum = [x for x in range(28123)]

#for loop to generate sum of two 
#abundant numbers
for i in range(len(ab)):
	for j in range(i,28123):
		if ab[i]+ab[j] < 28123:
			#negating the value of the abundant sum
			non_ab_sum[ab[i]+ab[j]] = 0
		else:
			break
print(sum(non_ab_sum))
print(ab)

#done!
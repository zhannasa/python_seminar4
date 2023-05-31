n = int(input('Enter the number of bushes: '))
bushes = []
import random
for i in range(n):
    bushes.append(random.randint(1, 100000))
print(bushes)
i = int(input('Enter the index number of bushes: '))

#s = bushes[i]+bushes[i+1]+bushes[i+2]
s = sum(bushes[i : i+3]) 
#s = [sum(bushes[i : i+3]) for i in range(len(bushes))]
print(s)


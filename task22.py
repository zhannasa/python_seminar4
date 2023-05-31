n = int(input('Enter the number of first set: '))
first_set = set()
for i in range(n):
    first_set.add(i**2)
print(first_set)
m = int(input('Enter the number of second set: '))
second_set = set()
for i in range(m):
    second_set.add(i*2)
print(second_set)
i = first_set.intersection(second_set)
print(i)

# n = int(input('Enter the number of first list elements: '))
# first_list = []
# for i in range(n):
#     first_list.append(int(input()))
# print(first_list)
# m = int(input('Enter the number of second list elements: '))
# second_list = []
# for i in range(m):
#     second_list.append(int(input()))
# print(second_list)
# first_set = set(first_list)
# second_set = set(second_list)
# print(first_set)
# print(second_set)
# i = first_set.intersection(second_set)
# print(sorted(i))





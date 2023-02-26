num = [1, 8, 3, 8, 2, 6, 8, 8, 15, 5, 14, 21, 80, 74]
index = 0
max_num = 0
num_size = len(num)
max_num_two = 0
while index < num_size:
    if max_num < num[index]:
        max_num = num[index]
    index = index + 1
index = 0
while index < num_size:
    if max_num_two < num[index] < max_num:
        max_num_two = num[index]
    index = index + 1
print(max_num, max_num_two)

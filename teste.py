min_val = int(input("Value minimum: "))
max_val = int(input("Value minimum: "))
list_num_pairs = []

for num in range(min_val, max_val + 1):
    if num % 2 == 0:
        list_num_pairs.append(num)

print(list_num_pairs)
total = 0

for num in list_num_pairs:
    total += num
print(total)




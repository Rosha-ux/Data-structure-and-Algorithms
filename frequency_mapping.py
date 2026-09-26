arr = [1,2,3,1,1,2,2,3]  # To check how many times each number repeated in this list.

frequency = {}

for num in arr:
    if num in frequency:
        frequency[num] += 1

    else:
        frequency[num] = 1

print(frequency)


# n = 12345
# num = n
# count = 0
# while num > 0:
#     num = num // 10
#     count += 1

# print (count)



#Example Two 
n = 456789

num = n
count = 0

while num > 0:
    num = num // 10
    count += 1

print(count)


# From the Logrithm base:

import math

n = 123456

count = math.floor(math.log10(n)) + 1

print(count)

# And if we need to start n with Zero at that case we need to assign n with one like;

"""n= 0
if n == 0:
    count = 1
"""
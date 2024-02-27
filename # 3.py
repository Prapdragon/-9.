# 1. 1, 3, 5, 7, 9, 11, 13, 15
result1 = ""
for i in range(1, 16, 2):
    result1 += str(i) + ", "
print(result1)

# 2. 2, 5, 8, 11, 14, 17, 19
result2 = ""
for i in range(2, 20, 3):
    result2 += str(i) + ", "
print(result2)

# 3. 30, 20, 10, 0, -10, -20, -30
result3 = ""
for i in range(30, -31, -10):
    result3 += str(i) + ", "
print(result3)

# 4. 15, 23, 31, 39, 47, 55
result4 = ""
for i in range(15, 56, 8):
    result4 += str(i) + ", "
print(result4)
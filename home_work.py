data = [1, 3, 10, 9, 6]

# 1번
for i in range(len(data)):
    print(data[i])

# 2번
for i in range(len(data)):
    print(i)

# 3번

for i in data:
    print(i)

# 4번
for i in range(len(data)):
    if i < 5:
        print(data[i])

# 5번
for i in range(len(data)):
    if data[i] < 5:
        print(i)

# 6번
for i in range(len(data)):
    if data[i] < 5:
        print(data[i])

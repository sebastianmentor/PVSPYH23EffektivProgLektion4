result = [
    x**2 + y**2
    for x in range(1, 6)
    for y in range(1, 4)
    if (x**2 + y**2) % 2 == 0 and x**2 > y**2
]

print(result)
# print(x,y)

result_2 = []
for x in range(1,6):
    for y in range(1,4):
        if (x**2 + y**2) % 2 == 0 and x**2 > y**2:
            result_2.append(x**2 + y**2)

print(result_2)
print(x,y)

import timeit

# Mät for-loop prestanda
loop_time = timeit.timeit(
    "kvadrater = []\nfor x in range(10000):\n    kvadrater.append(x**2)", number=1000)

# Mät list comprehension prestanda
comprehension_time = timeit.timeit(
    "kvadrater = [x**2 for x in range(10000)]", number=1000)

print(f"For-loop tid: {loop_time}")
print(f"List comprehension tid: {comprehension_time}")


# Mät for-loop prestanda
loop_time_2 = timeit.timeit(
    "resultat = []\nfor x in range(10000):\n    if x % 2 == 0:\n        resultat.append(x**2)", number=1000)

# Mät list comprehension prestanda
comprehension_time_2 = timeit.timeit(
    "resultatet = [x**2 for x in range(10000) if x % 2 == 0]", number=1000)

print(f"For-loop tid: {loop_time_2}")
print(f"List comprehension tid: {comprehension_time_2}")


# resultat = []
# for x in range(10000):
#     if x % 2 == 0:
#         resultat.append(x**2)

# kvadrater = [x**2 for x in range(10000) if x % 2 == 0]

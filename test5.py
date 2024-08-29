data = [1, {2, 3, 4},5]

första, [*hejsan], sista = data
# första, mellan, sista = data
print(första)   # Output: 1
print(hejsan)   # Output: [2, 3, 4]
print(sista)    # Output: 5


d = {1:2, 2:3, 3:4}

l = [num for tup in [(k,v) for k,v in d.items()] for num in tup]
print(l)


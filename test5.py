data = [1, {2, 3, 4},5]

första, [*hejsan], sista = data
# första, mellan, sista = data
print(första)   # Output: 1
print(hejsan)   # Output: [2, 3, 4]
print(sista)    # Output: 5


d = {1:2, 2:3, 3:4}

l = [num for tup in [(k,v) for k,v in d.items()] for num in tup]
print(l)

stupid = [[[i+k+j for i in range(5)] for k in range(5)] for j in range(5)]
# flat_stupid = [num for num in l1 for l1 in l2 for l2 in stupid]
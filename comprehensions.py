# List--------------------
kvadrater = [x**2 for x in range(10)]

jämna_kvadrater = [x**2 for x in range(10) if x % 2 == 0]

ordlista = ["apple", "banana", "cherry"]
omvända_ord = [word[::-1] for word in ordlista]

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
platt_lista = [item for sublista in list_of_lists for item in sublista]

# Set---------------------
kvadrater_set = {x**2 for x in range(10)}

unikt_tecken = {bokstav for bokstav in "abracadabra" if bokstav != 'a'}

# Dict--------------------
kvadrater_dict = {x: x**2 for x in range(10)}

original_dict = {'a': 1, 'b': 2, 'c': 3}
omvänd_dict = {värde: nyckel for nyckel, värde in original_dict.items()}


original_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
ny_dict = {nyckel: värde * 2 for nyckel, värde in original_dict.items() if värde % 2 == 0}

# Generator---------------
kvadrater_gen = (x**2 for x in range(10))

jämna_kvadrater_gen = (x**2 for x in range(10) if x % 2 == 0)

# Nested------------------
matris = [[rad * kolumn for kolumn in range(5)] for rad in range(5)]
tensor = [[[rad * kolumn*tens for kolumn in range(5)] for rad in range(5)] for tens in range(5)]

m = []
for rad in range(5):
    r = []
    for kolumn in range(5):
        r.append(rad*kolumn)

    m.append(r)

for row in matris: print(row)
for row in m: print(row)

for matrix in tensor:
    print('-'*20)
    for row in matrix: print(row)

#[print(row) for row in matris]
#[0,0,0,0,0] 
#[0,1,2,3,4]
#[0,2,4,6,8]
#[0,3,6,9,12]
#[0,4,8,12,16]
matris = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
platt_lista = [item for rad in matris for item in rad]


lista = [[1, 'a'], [2, 'b'], [3, 'c']]
dictionary = {nyckel: värde for nyckel, värde in lista}


# Funktionanrop
def är_primt(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

primtals_kvadrater = [x**2 for x in range(20) if är_primt(x)]


# Textdata
ordlista = ["Apple", "is", "a", "fruit"]
rensa_ord = [word.lower() for word in ordlista if len(word) >= 3]

print(rensa_ord)

namn = ["John Doe", "Jane Smith", "Albert Einstein"]
initialer = [namn.split()[0][0] + namn.split()[1][0] for namn in namn]


# Advanced

list_a = [1, 2, 3]
list_b = ['a', 'b', 'c']
par = [(x, y) for x in list_a for y in list_b]
print(par)
lag = ['Hammarby', 'AIK', 'Djurgården', 'Irsta FK']

from itertools import permutations,combinations

matcher = [(lagA, lagB) for lagA in lag for lagB in lag if lagB != lagA]
matcher_v2 = [(lagA, lagB) for lagA,lagB in permutations(lag, 2) if lagB != lagA] 
print(matcher)
print(matcher_v2, 'permutations') 


sträng = "abracadabra"
mängd_sträng = set(sträng)
tecken_antal = {tecken: sträng.count(tecken) for tecken in mängd_sträng}
for l in mängd_sträng:
    print(l)

print(tecken_antal)



nycklar = ['a', 'b', 'c']
värden = [1, 2, 3]
ny_dict = {nyckel: värde for nyckel, värde in zip(nycklar, värden)}

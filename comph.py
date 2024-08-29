# lista med alla tal mellan 10 och 100 

lista1 = []
for tal in range(10,101):
    lista1.append(tal)

print(lista1)

lista2 = [tal for tal in range(10,101)]

print(lista2)

lista3 = []
for tal in lista1:
    lista3.append(tal*100)
print(lista3)

lista4 = [tal * 100 for tal in lista1]

print(lista4)

stefan = 'stefan'
vokaler = 'aouåeiyäö'

set_vokaler = {vokal for vokal in vokaler}

stefan_vokaler = []
for letter in stefan:
    if letter in set_vokaler:
        stefan_vokaler.append(letter)
print(stefan_vokaler)

stefan_vokaler_v2 = [letter for letter in stefan if letter in set_vokaler]
print(stefan_vokaler_v2)
print(set_vokaler)

[print(x) for x in range(10)]

hej = (print(x) for x in range(10))

h = iter(hej)
try:
    while True:
        next(h)
except StopIteration:
    print('Slutar loopa nu!!')

    
for skriv_ut in hej:
    skriv_ut
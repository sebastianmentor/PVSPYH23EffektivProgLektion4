################################################################################
##################################   LISTOR   ##################################
################################################################################
# Övningar
# 1. Skapa en lista med kvadrater av alla jämna tal från 0 till 20.
# 2. Filtrera ut alla ord i listan ["apple", "banana", "cherry", "date"]
# som innehåller bokstaven ”a”.
# 3. Skapa en lista med de första bokstäverna av varje ord i listan ["Python",
# "is", "fun"].

kvad = [x**2 for x in range(21) if x % 2 == 0]

frukter = ["apple", "banana", "cherry", "date"]

a_frukter = [frukt for frukt in frukter if 'a' in frukt]

orden = ["Python", "is", "fun"]

första_bokstav = [word[0] for word in orden]

################################################################################
###################################  SETS  #####################################
################################################################################

# 1. Skapa ett set med kvadrater av alla unika tal i listan [1, 2, 2, 3,
# 4, 4, 5].
# 2. Skapa ett set av alla vokaler som finns i str¨angen "comprehensions".
# 3. Skapa ett set med längderna på orden i listan ["apple", "banana",
# "cherry"].

unika_tal = [1, 2, 2, 3, 4, 4, 5]

kvad_av_unika_tal = {x**2 for x in unika_tal}

nya_ord = ["apple", "banana", "cherry"]

längd_på_orden = {len(word) for word in nya_ord}

# print(längd_på_orden)

################################################################################
###############################  DICTIONARY  ###################################
################################################################################
# övningar
# 1. Skapa en dictionary där nycklarna är talen från 1 till 5 och värdena är
# kvadraterna av dessa tal.
# 2. Skapa en dictionary från listan ["apple", "banana", "cherry"] där
# varje nyckel är ett ord och värdet är längden på ordet.
# 3. Givet dictionaryt "a": 1, "b": 2, "c": 3, skapa ett nytt dictionary
# där värdena är kvadraterna av de ursprungliga värdena.


kvad_dict = {key:key**2 for key in range(1,6)}

fr = ["apple", "banana", "cherry"]

frukt_längd = {frukt:len(frukt) for frukt in fr}

scores = {"a": 1, "b": 2, "c": 3}

d_kvad = {key:scores[key]**2 for key in scores}

d_kvad_2 = {key:value**2 for key,value in scores.items()}

# print(d_kvad)
# print(d_kvad_2)

################################################################################
#################################  ADVANCED  ###################################
################################################################################
# 1. Skapa en lista med alla kvadrater av jämna tal från 1 till 100 som är
# delbara med 4 men inte med 8.
# 2. Skapa ett set med de första bokstäverna av orden i listan ["Python",
# "is", "powerful", "and", "fun"] där ordet har mer än tre bokstäver.
# 3. Skapa en dictionary där nycklarna är orden i meningen "Python comprehensions
# are powerful" och värdena är orden baklänges.

l_kvad = [n for n in range(1,101) if n % 4 == 0 and n % 8 != 0] # 4, 12, 20, 28, 36, 44
# 44 = 11*4 + 0 -> 44/4 = 11.0 -> 44//4 = 11 -> 44 % 4 = 0
# 44 = 5*8 + 4 -> 44/8 = 5.5 -> 44//8 = 5 -> 44 % 8 = 4
# n = k*4 + c -> fyra delar alla helta n där k är ett heltal. 
# print(l_kvad)

o = ["Python", "is", "powerful", "and", "fun"]

set_of_words = {letter[0] for letter in o if len(letter) > 3}
# print(set_of_words)

meningen = "Python comprehensions are powerful"
# {Python:nohtyP, comprehensions:snoisneherpmoc, are:era, powerful:lufrewop}

def baklängesord(ordet:str) -> str:
    # "Python" -> "nohtyp"
    ord_som_lista = list(ordet)
    # ['P','y','t','h','o','n']
    baklängesordet = []
    längd_på_ordet = len(ordet)
    # längden_på_ordet = 6
    baklänges = -1

    for _ in range(längd_på_ordet):
        baklängesordet.append(ord_som_lista[baklänges])
        baklänges = baklänges - 1
     
    return "".join(baklängesordet)

def bak_v2(ordet:str) -> str:
    ret_word = []
    for index in range(1,len(ordet)+1):
        ret_word.append(ordet[-index])
    return ''.join(ret_word)

def rev(word:str) -> str:
    word_list = list(word)
    word_list.reverse()
    return ''.join(word_list)




d_mening = {word:baklängesord(word) for word in meningen.split()}
d_mening_v2 = {word:word[::-1] for word in meningen.split()} # <- do this!!!!
d_mening_v3 = {word:bak_v2(word) for word in meningen.split()}
print(d_mening)
print(d_mening_v2)
print(d_mening_v3)

################################################################################
################################################################################

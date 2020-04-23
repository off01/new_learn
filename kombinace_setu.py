# Prirazeni promennych
str1 = 'New York'
str2 = 'Yorkshire'

# Najde spolecne prvky
spolecne = set(str1).intersection(set(str2))


# Najde unikatni prvky
unikatni = set(str1)

# Najde nesdilene prvky
nesdilene = set(str1).symmetric_difference(set(str2))


# Najde vsechny prvky
vsechny = set(str1).union(set(str2))

# Vypis vsechn
print(spolecne)
print(unikatni)
print(nesdilene)
print(vsechny)
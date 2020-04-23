# vytvor prazdne slovniky do slovníků
muj_slovnik = {}
novy_slovnik = {}

# vloz klice 'jméno', 'přijmení' do 'muj_slovnik' a přidej libovolne hodnoty
muj_slovnik['jméno'] = 'Karel'
muj_slovnik['přijmení']	= 'Novák'

# vytvor z tuple 'muj_tuple' slovnik do slovniku 'novy_slovnik'
muj_tuple = 'věk', 'email'
novy_slovnik = novy_slovnik.fromkeys(muj_tuple)		#Metoda použitá pro vytvoření dictonary z tuple
print(novy_slovnik)

# dopln muj_slovnik o novy_slovnik
muj_slovnik.update(novy_slovnik)
print(muj_slovnik)

# vypln klice 'věk' a 'mail'
muj_slovnik['věk'] = '15'
muj_slovnik['email']	= 'Novák@Karel.cz'
print(muj_slovnik)


# TADY NIC NEPIŠ!! Slouží pro kontrolu :)
if (len(muj_slovnik) + 1) % 5 == 0 and '@' in muj_slovnik['email']:
	print('Paráda, metody slovníků ovládáš na jedničku, blahopřejeme!')
else:
	print('Bohužel jsi někde udělal chybku :(\nPodívej se ještě jednou na tabulku s metodami.\n\npozn. Obsahuje tvůj email "@"?')
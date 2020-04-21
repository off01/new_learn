# Nas slovnik
data = {
	'uzivatel1': 'heslo',
	'Marek': '1234',
	'Danko': 'qwert',
			}

print(data['Marek'])

# Zeptej se na uzivatelske jmeno a heslo
jmeno = input('Zadejte uživatelské jméno: ')
heslo = input('Zadejte uživatelské heslo: ')


# Podminkovy vyraz
if data.get(jmeno) == heslo:
	print('Povolení pokračovat!')

elif data.get(jmeno) != heslo:
	print('Heslo, nebo uživatelské jméno je špatně!')
# Vytvor list 'tyden' a uloz dny v tydnu v podobe stringu (vse malymi pismeny!)
tyden = ('pondělí','úterý','středa','čtvrtek','pátek','sobota','neděle')

tyden_1 = ['pondělí','úterý','středa','čtvrtek','pátek','sobota','neděle']

print(tyden_1)

# Ziskej tip uzivatele
tip_uzivatele = input('Jakým písmenem začíná jméno pátého dne v týdnu?:')

# Ziskej prvni pismeno z 'pátek' 3
patek_pismeno = tyden_1[4][0] == tip_uzivatele ## VYCHYTAVKA v oblasti listu !!!! tyden_1[4][0]



# Vytiskni porovnani promennych
print(patek_pismeno)

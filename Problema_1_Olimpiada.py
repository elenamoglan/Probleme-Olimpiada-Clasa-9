total = eval(input('Introduceti numarul de pasari: '))
gaini = total // 2
rate = gaini // 4
gaste = total - gaini - rate
print(f'La ferma sunt {gaini} gaini, {rate} rate si {gaste} gaste')
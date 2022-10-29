prod = int(input("production : "))
taxe = float(input("taxe : "))

prod *= 24
taxe = taxe / 4 * 3
taxe = 100-taxe
taxe /= 100
taxe = round(taxe, 3)

total = prod * taxe
total /= 3

print(total)

surtaxe = 0
chariot = 0
reste = 0

if total >= 3000000 and total <=5999999:
    chariot = 1
    reste  = total - 3000000
    surtaxe = reste / 100 * taxe
elif total >= 6000000 and total <=8999999:
    chariot = 2
    reste  = total - 6000000
    surtaxe = reste / 100 * taxe
elif total >= 9000000 and total <=11999999:
    chariot = 3
    reste  = total - 9000000
    surtaxe = reste / 100 * taxe
elif total >= 12000000 and total <=14999999:
    chariot = 4
    reste  = total - 12000000
    surtaxe = reste / 100 * taxe
    reste += surtaxe
    reste = round(reste, 0)

print(f"""Vous devez envoyer {chariot} chariots entier,
Vous devez envoyer {reste} dans un autre chariot """)
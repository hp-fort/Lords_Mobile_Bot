rss = input("ressouce demander (8m/10m/7m/85k/5m) : ")

rss = rss.split("/")
food = rss[0]
stone = rss[1]
wood = rss[2]
ore = rss[3]
gold = rss[4]

for i in range(5):
    if i == 0:
        var = food
    if i == 1:
        var = stone
    if i == 2:
        var = wood
    if i == 3:
        var = ore
    if i == 4:
        var = gold
        
    if var.endswith("k"):
        var = var.split("k")
        var = float(var[0])
        var *= 1000
        var = round(var)
    elif var.endswith("m"):
        var = var.split("m")
        var = float(var[0])
        var *= 1000000
        var = round(var)
    elif var.endswith("b"):
        var = var.split("b")
        var = float(var[0])
        var *= 1000000000
        var = round(var)

print(food)
print(stone)
print(wood)
print(ore)
print(gold)
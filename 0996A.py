money = int(input())
count = 0
while money > 0:
    while money >= 100:
        count += 1
        money -= 100
    while money >= 20:
        count += 1
        money -= 20
    while money >= 10:
        count += 1
        money -= 10
    while money >= 5:
        count += 1
        money -= 5
    while money >= 1:
        count += 1
        money -= 1
print(count)

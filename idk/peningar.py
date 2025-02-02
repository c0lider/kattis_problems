_, step = map(int, input().split())

fields = [int(number) for number in input().split()]

i = 0
money = 0

while fields[i] != 0:
    money += fields[i]
    fields[i] = 0
    i = (i + step) % n

print(money)

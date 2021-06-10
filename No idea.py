
input()
i = input().strip().split(' ')
a = set(input().strip().split(' '))
b = set(input().strip().split(' '))

happiness = 0

for n in i:
    if n in a:
        happiness += 1

for n in i:
    if n in b:
        happiness -= 1

print(happiness)
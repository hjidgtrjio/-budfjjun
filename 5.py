N = int(input("Zadejte cislo N "))
s = 0
for i in range(1, N + 1):
    if i < N:
        print(i, end="+")
    else:
        print(i, end="=")
    s += i
print(s)
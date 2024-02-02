aikencode = {
    0 : "0000",
    1 : "0001",
    2 : "0010",
    3 : "0011",
    4 : "0100"
}

code = "000000110100"

liste = [code[i:i+4] for i in range(0,len(code), 4)]

print("liste", liste)

zahl = ""
for i in liste:
    for j in aikencode:
        if aikencode.get(j) == str(i):
            zahl += str(j)


zahl0 = [j for i in liste for j in aikencode if aikencode.get(j) == str(i)]
print(zahl0)
print(zahl)
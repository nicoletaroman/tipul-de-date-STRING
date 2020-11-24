s=str(input('Dati sirul'))
import string
sm=0
smic=0
sp=0
special_chars=string.punctuation

for i in s:
    if i in string.ascii_uppercase:
        sm=sm+1
    elif ((ord(i)<=57) and (ord(i)>=48)):
        smic=smic+1
    if i in special_chars:
        sp=sp+1

print('Numarul de majuscule este  ',sm)
print('Numarul de cifre este  ',smic)
print('Numarul de caractere speciale este  ',sp)


c1=str(input("dati un cuvant"))
c2=str(input("dati un cuvant"))
c3=str(input("dati un cuvant"))
c4=str(input("dati un cuvant"))
if len(c1)>=3 and len(c2)>=3 and len(c3)>=3 and len(c4)>=3:
       k=len(c4)//2
       cuvantnou=c1[0:2]+c2[0]+c3[0:3]+c4[0:int(k)]
   
print("cuvantul 1 este ",c1)
print("cuvantul 2 este ",c2)
print("cuvantul 3 este ",c3)
print("cuvantul 4 este ",c4)
print("cuvantul nou este",cuvantnou)

if len(c1)<3 or len(c2)<3 or len(c3)<3 or len(c4)<3:
       print("prea putine litere")





import sys
c=str(input('CNP este '))
t=True
if (len(c)==13):
    for i in c:
        if ((ord(i)<=57) and (ord(i)>=48)):
            t=True
        else:
            t=False
else:
    print('introduceti 13 caractere')    
    sys.exit()   
if t==True:
    print('CNP corect')  
else:
    print('CNP incorect') 
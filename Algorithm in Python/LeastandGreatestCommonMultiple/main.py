#ƏBOB tapılması
a=int(input("Ədəd daxil edin"))
b=int(input("Ədəd daxil edin"))
while a!=b :
    if a>b :
        a=a-b
    else :
        b=b-a
print("ƏBOB = ",a)

#ƏKOB tapılması
a=int(input("Ədəd daxil edin"))
b=int(input("Ədəd daxil edin"))
x=a
y=b
s=x*y
while a!=b :
    if a>b :
        a=a-b
    else :
        b=b-a
print("ƏKOB = ",int(s/a))
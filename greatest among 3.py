#program to find greatest among three numbers
a=int(input("enter a value"))
b=int(input("enter b vaue"))
c=int(input("enter c value"))
if (a>b)&(a>c):
    print("a is greatest value")
elif (b>a)&(b>c):
    print("b is greatest value")
else:
    print("c is greatest value")

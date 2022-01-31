import random

a="abcdefghijklmnopstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
b="0123456789"
c="~`!@#$%^7*()_-+={[}]|\:;'<,>.?/"
d="abcdefghijklmnopstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
e="abcdefghijklmnopstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ~`!@#$%^7*()_-+={[}]|\:;'<,>.?/"
f="0123456789~`!@#$%^7*()_-+={[}]|\:;'<,>.?/"
g="abcdefghijklmnopstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789~`!@#$%^7*()_-+={[}]|\:;'<,>.?/"
print("\nHey, You need a strong password right?\nI'm here to help you\n")
print("Which type of password is required?\n\n1.Characters(Contains Uppercase and lowercase)\n2.Numbers\n3.Special characters\n4.Characters & numbers\n5.Characters & Special symbols\n6.Numbers & Special characters\n7.Contains everything")
ch=int(input("\nEnter your choice"))
leng=int(input("How much length is required to your password?"))
count=int(input("How many password do you want?"))
if ch==1:
    z=a
elif ch==2:
    z=b
elif ch==3:
    z=c
elif ch==4:
    z=d
elif ch==5:
    z=e
elif ch==6:
    z=f
elif ch==7:
    z=g
print("\nSome cool passwords:\n")
for x in range(count):
    empty=""
    for y in range(leng):
        s=random.choice(z)
        empty=empty+s
    print(empty,"\n")
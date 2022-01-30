array=[1000000000000000,1000000000000,1000000,1000,1,0.001,0.000001,0.000000001,0.000000000001]
unit=["Gigatonne","Megatonne","Tonne","Kilogram","Gram","Milligram","Microgram","Nanogram","Picogram"]
print("Welcome to weight convertor\nWhich type of weight are you going to enter?")
print("1.Gigatonne\n2.Megatonne\n3.Tonne\n4.Kilogram\n5.Gram\n6.Milligram\n7.Microgram\n8.Nanogram\n9.Picogram")
a=int(input("Enter your choice"))
b=int(input("Convert to which weight?"))
weight=float(input("Enter the weight"))
for x in range(a):
    for y in range(b):
        p=array[x]
        q=array[y]
        u=unit[y]
converted_weight=weight*p/q
print("The CONVERTED weight is",converted_weight,u)
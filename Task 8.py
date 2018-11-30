textt = "test1.txt"
exist = 0
sname = input("Enter Name to Search: ")
txtfile=open(textt).read()
for line in open(textt).readlines():
    name = line.split(" , ")[0]
    address = line.split(" , ")[1]
    if sname.lower() == name.lower():
        exist = exist + 1
if exist >= 1:
    print("Name found. There are " +str(exist) +" names matching.")
else:
    print("No names found.")

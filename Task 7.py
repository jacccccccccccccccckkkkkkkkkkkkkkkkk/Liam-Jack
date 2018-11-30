Aname= input("enter name: ")
txtfile=open("text.txt").read()
for line in open("text.txt").readlines():
  name = line.split(", ")[0]
  address = line.split(", ")[1]
  if Aname.lower() == name.lower():
    print(address)

sentence = "your name is "
name = input("enter name: ")
address = input("enter address: ")
sentence = sentence + name
sentence = sentence + " your address is " + address
txtfile=open("text.txt", "a")
txtfile.write(sentence)
txtfile.close()

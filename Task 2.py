def read():
  asd = 0
  lines = int(input("Lines?"))
  f = open("file.txt", "r")
  for line in f:
    while asd < lines:
      print(line)
      asd = asd + 1
      break
read()

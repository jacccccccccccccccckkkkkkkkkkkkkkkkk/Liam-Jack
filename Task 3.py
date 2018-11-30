def lines():
  noOFlines = 0
  f = open("Text.txt")
  for lines in f:
    noOFlines = noOFlines + 1
  print(noOFlines)
lines()

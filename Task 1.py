for line in open("hello.txt").readlines():
  sentence = line.split(",")[0]
print(sentence)

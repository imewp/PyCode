
textFile = open("7.1.txt", "rt", encoding="utf-8")
print(textFile.readline())
textFile.close()
binFile = open("7.1.txt", "rb")
print(binFile.readline())
textFile.close()

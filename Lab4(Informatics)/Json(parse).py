inputFile = open("Friday1.json", "r", encoding = "utf-8")
text = inputFile.read()
inputFile.close()
text = text.replace('{', '')
text = text.replace('"', '')
text = text.replace('}', '')
text = text.replace(',', '')
outputFile = open("Friday1.txt", "w", encoding = "utf-8")
outputFile.write(text)
outputFile.close()
print(text)



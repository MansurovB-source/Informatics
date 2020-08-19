inputFile = open("Friday.json", "r", encoding = "utf-8")
text = inputFile.read()
inputFile.close()
text = text.replace('{', '')
text = text.replace('"', '')
text = text.replace('}', '')
text = text.replace(',', '')
levels = []
maxLevel = 0
text = text.split('\n')
text.pop(0)
i = 0
while i < len(text) - 1:
    if text[i].count('\t') == len(text[i]) and text[i + 1].count('\t') == len(text[i + 1]):
        text.pop(i)
        i -= 1
    i += 1
for line in text:
    tabs = 0
    for symbol in line:
        if symbol != '\t':
            break
        tabs += 1
    if line.count('\t') == len(line): tabs = 1
    levels.append(tabs)
    maxLevel = max(maxLevel, tabs)

outputFile = open("Friday.yml", "w", encoding = "utf-8")
for i in range(len(text)):
    line = text[i]
    if levels[i] != 1 and levels[i] != maxLevel:
        line = line[levels[i]:]
        line = '\t' * levels[i] + '- ' + line
    line = line.replace('\t', '    ')
    outputFile.write(line + '\n')
outputFile.close()
printFile = open("Friday.yml", "r", encoding = "utf-8")
text1 = printFile.read()
print(text1)

inputFile = open("table.txt", "r")
text = inputFile.read().strip(' ').split('\n')
inputFile.close()
resultArray = []
for i in text:
    if i == "":
        continue
    surname, init, date, sc1, sc2, sc3 = i.strip(' ').split(' ')
    sc1, sc2, sc3 = int(sc1), int(sc2), int(sc3)
    dateNew = '.'.join(list(reversed(date.split('.'))))
    resultArray.append([dateNew, surname + ' ' + init, sc1, sc2, sc3, (sc1 + sc2 + sc3) / 3])
resultArray = sorted(resultArray, reverse = True)
for i in resultArray:
    print(i[1] + '\t|\t' + '.'.join(list(reversed(i[0].split('.')))) +
          '\t|', i[2], i[3], i[4], '->', i[5], sep = '\t')
          

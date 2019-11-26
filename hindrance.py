import csv
csv.register_dialect('myDialect',
delimiter = ',',
skipinitialspace=True)

with open('hindrance.csv', 'r') as csvFile:
    reader = csv.reader(csvFile, dialect='myDialect')
    for row in reader:
        print(row)

csvFile.close()



#rowNum=input("Enter ID: ")
#product=input("Enter Product: ")
#hindrance=input("hindrance: ")


#row = [rowNum, hindrance, product]

with open('hindrance.csv', 'r') as readFile:
    reader = csv.reader(readFile)
    lines = list(reader)
    lines[2] = row

with open('hindrance.csv', 'w') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerows(lines)

readFile.close()
writeFile.close()
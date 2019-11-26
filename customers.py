import csv
csv.register_dialect('myDialect',
delimiter = ',',
skipinitialspace=True)

with open('customers.csv', 'r') as csvFile:
    reader = csv.reader(csvFile, dialect='myDialect')
    for row in reader:
        print(row)

csvFile.close()



rowNum=input("Enter ID: ")
name=input("Enter Name: ")
phoneNum=input("Phone Nummber ")
device=input("Enter Device: ")
hindrence=input("Enter The Tye Of corruptions: ")


row = [rowNum, name, phoneNum,device, hindrence]

with open('customers.csv', 'r') as readFile:
    reader = csv.reader(readFile)
    lines = list(reader)
    lines[2] = row

with open('customers.csv', 'w') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerows(lines)

readFile.close()
writeFile.close()
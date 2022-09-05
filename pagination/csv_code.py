import csv

with open('data-398-2018-08-30.csv', 'r', encoding='utf8', newline='\n') as csv_file:
    reader = csv.DictReader(csv_file)
    data = []
    for row in reader:
        data += [[row['Name'], row['Street'], row['District']]]


for x, y, z in data:
    print(x, y, z)

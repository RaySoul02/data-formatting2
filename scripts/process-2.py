import csv
r = csv.reader(open('source-2.csv'))
h = next(r)
h1 = ['year', 'region', 'value']
data = list(r)
data.sort()
for i in range(len(data) -1, 0, -1):
    try:
        if (data[i][0], data[i][1]) == (data[i-1][0], data[i-1][1]):
            data[i-1][2] = int(data[i][2]) + int(data[i-1][2])
            data.remove(data[i])
    except IndexError as e:
        pass
writer = csv.writer(open('result-2.csv', 'w', newline=''))
writer.writerow(h1)
for line in data:
    line[0] = '{month}-{day}-{year}'.format(month = line[0][4:6], day = line[0][6:], year = line[0][:4])
    writer.writerow(line)
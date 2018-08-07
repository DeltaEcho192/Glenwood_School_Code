weekdays = []
filelines = []

weekdays.append(int(input("Please input Mondays Sales")))
weekdays.append(int(input("Please input Tuesday Sales")))
weekdays.append(int(input("Please input Wednesday Sales")))
weekdays.append(int(input("Please input Thursday Sales")))
weekdays.append(int(input("Please input Friday Sales")))

total_sales = sum(weekdays)
print(total_sales)


f = open('record.txt', "r")
for line in f:
    filelines.append(line)

filelen = len(filelines) - 1
print(filelen)

lastweeknum = int(filelines[filelen])
print(lastweeknum)
int(total_sales)
perincrease = total_sales/lastweeknum
perincrease = perincrease * 100

print("Percentage Increase Over last week: ")
print(perincrease)
f.close()
f = open('record.txt','a')
total_sales = str(total_sales)
f.write(total_sales +"\n")
f.close()


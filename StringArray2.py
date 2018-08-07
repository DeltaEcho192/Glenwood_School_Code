word = ""
firstnames = []
bigwords = []
newbiggestword = ""
oldbiggestword  = 0
oldbiggestnames = ""
positionmeter = []

while word != "end":
    word = input("Please enter the name, Type end to stop: ")
    if word == "end":
        break
    else:
        firstnames.append(word)

lenfirstnames = len(firstnames)
for i in range(lenfirstnames):
    intfirstnames = int(len(firstnames[i]))
    if intfirstnames > 6:
        print(firstnames[i])
        bigwords.append(firstnames[i])
print(firstnames)


oldbiggestword = int(len(firstnames[0]))
for x in range(lenfirstnames):
    intfirstnames = int(len(firstnames[x]))
    
    if intfirstnames > oldbiggestword:
        oldbiggestword = intfirstnames
        positionmeter[0] = x
    elif intfirstnames == oldbiggestword:
        positionmeter[1] = x
        


        
for i in range(2):
    printer = positionmeter[i]
    print(firstnames[i])

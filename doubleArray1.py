import random

realnumArr = []

for z in range(10):
    randomnum = random.randint(1,50)
    realnumArr.append(randomnum)


i = 0 
print(realnumArr)
lenarray = len(realnumArr)
for i in range(lenarray):
    sizecheck = realnumArr[i]
    float(sizecheck)
    if sizecheck > 26.5:
        print(realnumArr[i])
   
print()
sumavg = sum(realnumArr)
int(sumavg)
int(lenarray)
avgArr = sumavg/lenarray
print("The Average of the Array" + " " + str(avgArr) + "\n")


x = 0
print("Numbers Smaller the Average")
for x in range(lenarray):
    sizecheck = realnumArr[x]
    float(sizecheck)    
    if sizecheck < avgArr:
        print(realnumArr[x])



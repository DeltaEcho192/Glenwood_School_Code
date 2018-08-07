import math
intergers = [2,4,55,23,12,99,145,76]

print(intergers)
x = 0
lenintergers = len(intergers)
print("These are doubles")
for i in range(lenintergers):
    worknum = intergers[i]
    worknum = worknum * 2

    print(worknum)

print("These are Squares")    
for z in range(lenintergers):
        if x < lenintergers:
            sqworknum = intergers[x]
            sqworknum = pow(sqworknum, 2)
            print(sqworknum)
            x = x + 2
        else:
            break

print("These are In reverse")
s = lenintergers - 1
for q in range(lenintergers):
    reworknum = intergers[s]
    print(reworknum)
    s = s - 1

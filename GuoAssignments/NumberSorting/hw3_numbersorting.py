def numsort(var1, var2, var3, var4, var5, var6, var7, var8, var9, var10):
    total = var1 + var2 + var3 + var4 + var5 + var6 + var7 + var8 + var9 + var10
    print('Sum of All numbers: ' , total)

    average = total/10
    print('The average is: ' , average)

    numbers = [var1, var2, var3, var4, var5, var6, var7, var8, var9, var10]
    numbers.sort(reverse = True)

    evenTotal = 0
    oddTotal = 0
    if var1 % 2 == 0:
        evenTotal = var1 + evenTotal
    if var2 % 2 == 0:
        evenTotal = var2 + evenTotal
    if var3 % 2 == 0:
        evenTotal = var3 + evenTotal
    if var4 % 2 == 0:
        evenTotal = var4 + evenTotal
    if var5 % 2 == 0:
        evenTotal = var5 + evenTotal
    if var6 % 2 == 0:
        evenTotal = var6 + evenTotal
    if var7 % 2 == 0:
        evenTotal = var7 + evenTotal
    if var8 % 2 == 0:
        evenTotal = var8 + evenTotal
    if var9 % 2 == 0:
        evenTotal = var9 + evenTotal
    if var10 % 2 == 0:
        evenTotal = var10 + evenTotal


    if var1 % 2 == 0:
        oddTotal = var1 + oddTotal
    if var2 % 2 == 0:
        oddTotal = var2 + oddTotal
    if var3 % 2 == 0:
        oddTotal = var3 + oddTotal
    if var4 % 2 == 0:
        oddTotal = var4 + oddTotal
    if var5 % 2 == 0:
        oddTotal = var5 + oddTotal
    if var6 % 2 == 0:
        oddTotal = var6 + oddTotal
    if var7 % 2 == 0:
        oddTotal = var7 + oddTotal
    if var8 % 2 == 0:
        oddTotal = var8 + oddTotal
    if var9 % 2 == 0:
        oddTotal = var9 + oddTotal
    if var10 % 2 == 0:
        oddTotal = var10 + oddTotal

    print('Sum of Even numbers: ' , evenTotal)
    print('Sum of Odd numbers: ' , oddTotal)


    smallestNum = 100
    largestNum = 0

    if var1 < smallestNum:
        smallestNum = var1
    if var2 < smallestNum:
        smallestNum = var2
    if var3 < smallestNum:
        smallestNum = var3
    if var4 < smallestNum:
        smallestNum = var4
    if var5 < smallestNum:
        smallestNum = var5
    if var6 < smallestNum:
        smallestNum = var6
    if var7 < smallestNum:
        smallestNum = var7
    if var8 < smallestNum:
        smallestNum = var8
    if var9 < smallestNum:
        smallestNum = var9
    if var10 < smallestNum:
        smallestNum = var10

    if var1 > largestNum:
        largestNum = var1
    if var2 > largestNum:
        largestNum = var2
    if var3 > largestNum:
        largestNum = var3
    if var4 > largestNum:
        largestNum = var4
    if var5 > largestNum:
        largestNum = var5
    if var6 > largestNum:
        largestNum = var6
    if var7 > largestNum:
        largestNum = var7
    if var8 > largestNum:
        largestNum = var8
    if var9 > largestNum:
        largestNum = var9
    if var10 > largestNum:
        largestNum = var10

    print('The Smallest number is: ' , smallestNum)
    print('The largest number is: ' , largestNum)

################################################
# USAGE
'''
numberList = []
for i in range(0, 12, 3):
  print("i= ", i)
  numberList.append(i*2)

var1 = 6

print(numberList)
#print(numberList[var1])

'''
var1 = int(input())
var2 = int(input())
var3 = int(input())
var4 = int(input())
var5 = int(input())
var6 = int(input())
var7 = int(input())
var8 = int(input())
var9 = int(input())
var10 = int(input())

numsort(var1, var2, var3, var4, var5, var6, var7, var8, var9, var10)




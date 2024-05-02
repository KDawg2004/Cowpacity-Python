#this program can help people building fenced area
#lets you know how sutible your land is for the cows needs.
fenceL = int(input("What is the linear feet of your fence?: "))
squareF = (fenceL / 4) * 2 #take total divide by 4, then multiply width and length
print("Your farms fenced in area has", squareF, "square feet!")
cowS = squareF // 100 #for whole number
cowT = squareF % 100 #for remainder
dowR = 100 - cowT #helpful, can let you know how much more fence you need.
print("Your farms can fit ", cowS , " cows!")
print("Your farm needs another ", dowR , " square feet to fit another cow.")

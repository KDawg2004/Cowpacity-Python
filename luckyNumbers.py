#luckyNumbers lists out numbers, and lets you
#know when your lucky number will appear!
x=0
while x <= 50:
    print(x)
    x=x+1
    if ((x%13) == 0):#should return 0, if lucky 13 can be divised
        print("Next is Your lucky number!")
    
        
print('fifty is a good place to stop!')#final statemnt, to let you know its over

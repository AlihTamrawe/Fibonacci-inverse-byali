import os

def inverse(x):
    sum=1 # the n-2 and the accumalative sum
    last=1 # the n-1
    count =2 # the counte shifted by two whe the first two element 
    while x >= sum : 
        temp = sum  # keep and move wo last  which make me determine the interver fall of the inverse 
        print(sum ," ",count)
        sum = sum + last
        count=count+1

        last = temp
    countm =count-1
    if x ==sum:
        print("the inverse of The number is :",count)
    elif  x == last :
        print("the inverse of The number is :" , countm)
    else:
        print("the inverse of The number is not Avaliable")

inverse(int(input()))

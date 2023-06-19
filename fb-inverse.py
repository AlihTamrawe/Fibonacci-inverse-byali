import os

def inverse(x):
    sum=1
    last=1
    count =2 
    while x >= sum :
        temp = sum
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

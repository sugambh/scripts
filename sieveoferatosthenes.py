import math
def numberofprimes(n):
    numbers=range(2,n+1)
    for p in numbers:
        temp=p*p
        while temp<=n:
            #print temp
            if(temp in numbers):
                numbers.remove(temp)
            temp=temp+p
    return len(numbers)

#using prime theorem
def PI(x):
    return x/math.log(x)
i=1
while(1):
    x=int(math.pow(10,i))
    print "actual"+str(numberofprimes(x))+" by theorem"+str(PI(x))
    i=i+1

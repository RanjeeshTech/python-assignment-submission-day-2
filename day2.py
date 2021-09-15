#Day-2 Assignment Python zero to hero

#1-To check whether the number given prime or not
def findPrime(n):
    count=0
    for i in range(1,n+1):
        if(n%i==0):
            count=count+1

    if(count==2):
        return "Yes this is prime..."
    else:
        return "No this is not prime..."
print("Enter the number: ")
N=input()
N=int(N)
print(findPrime(N))

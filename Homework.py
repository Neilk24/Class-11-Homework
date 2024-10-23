n=int(input("Enter a number: "))
if n==0:
    print("Your number 0 has 1 digit")
else:
    temp=n
    sum=0
    while temp>0:
        temp//10
        sum=sum+1

    print("Your number", n,"has", sum, "digits")

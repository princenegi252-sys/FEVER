#TO FIND SUM OF FIRST  n NATURAL NUMBERS
n=int(input("ENTER THE VALUE OF n: "))
sum=0
for i in range(1,n+1):
    sum=sum+i
print("SUM OF FIRST",n,"NATURAL NUMBERS IS:",sum)
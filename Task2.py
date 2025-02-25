#Check given number is Prime or not
n=int(input("enter a number"))
prime=True
if n==0 or n==1:
    print("either prime nor composite")
elif n>1:
   for i in range(2,n):
     if n%i==0:
        prime=False
        break
   if prime:
    print("it is a prime number")
   else:
    print("not prime")
#Factorial of a given number
n=int(input("enter a number:"))
i=1
while n>0:
    i=i*n
    n=n-1
print(i)

#Number divisible by 3 and 5
n=int(input("enter a number:"))
if n==0:
    print("zero error")
for i in range(1,n+1):
    if i%3==0 or i%5==0:
        print(i)
#Reverse order program
n=int(input("enter a number:"))
temp=n
rev=0
sum=0
count=0
while temp>0:
    rem=temp%10
    rev=rev*10+rem
    temp=temp//10
    sum=sum+rem
    count+=1
print("reverse order of the given number:",rev)
print("sum of individual numbers in the given number",sum)
print("count of given number",count)
#print numbers from 1  to 100
n=int(input("enter a number"))
for i in range(1,n):
    print(i)
#sum of given numbers
n=int(input("enter values"))
sum=0
for i in range(1,n+1):
    sum=sum+i
print(sum)
#print even numbers
n=int(input("enter a number:"))
i=1
while i<=n:
    if i%2==0:
        print(i)
    i=i+1   
#To display multiplication table 
number = int(input("Enter a number: "))
if number==0:
    print("Anything * zero is zero")
else:
    for i in range(1, 21):  
        print(number,"x",i," =" ,number * i)

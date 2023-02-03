#1
def total(a,b):
        result1=a+b
        result2=a-b
        result3=a*b
        result4=a/b
        result5=a^b
        result6=a%b
        print("function result is",result1)
        print("function result is",result2)
        print("function result is",result3)
        print("function result is",result4)
        print("function result is",result5)
        print("function result is",result6)
a=int(input("enter the value of a"))
b=int(input("enter the value of b"))
total(a,b)

#2

x=int(input("enter the value of x"))
y=int(input("enter the value of y"))
total(x,y)

#3
def suraj(money):
    print("give suraj the sum of ",money)
money=50
suraj(money)
suraj(5*10)
suraj(5^10)
#4

var = 'suraj'
def show():
    global var1
    var1='tall'
    print("in function var cls",var)
show()
print("outside function",var1)
print("var is",var)
#5
def outf():
    var=10
    def innf():
        var=20
        print("inner var",var)
    innf()
    print("outer var",var)
outf()
#6
def cube(x):
    return(x*x*x)
num=10
result=cube(num)
print("output of the evaluation is",result)
#7
def display(name,age):
    print("name",name)
    print("age",age)
n='suraj'
y=21
display(name=n,age=y)
#8
def fib(n):
    if n<2:
        return 1
    return(fib(n-1)+fib(n-2))
n=int(input())
for i in range(n):
    print("fibonacci(",i,")",fib(i))

#9
from time import*
t1=perf_counter()
i=sum=0
while i<1000000:
    sum+=1
    i+=1
    sleep(0)
t2=perf_counter()
print("execution time =%f seconds" %(t2-t1))

#10
import datetime
base= datetime.datetime.today()
for x in range (0,10):
    print(base+datetime.timedelta(days=x))

#11
def hanoi(n,a,b,c):
    if n>0:
        hanoi(n-1,a,c,b)
    if a:
        c.append(a.pop())
        hanoi(n-1,b,a,c)
a=[1,2,3,4]
b=[]
c=[]
print("before puzzle")
print(a,b,c)
hanoi=(len(a),a,b,c)
print("after puzzle")
print(a,b,c)

#12(strong number)
sum1=0
num=int(input("Enter a number:"))
temp=num
while(num):
    i=1
    f=1
    r=num%10
    while(i<=r):
        f=f*i
        i=i-1
        sum1=sum1+f
        num=num//10
    if(sum1==temp):
        print("the number is a strong number")
    else:
        print("the number is not a strong number")










    





    


# series
val=int(input("Enter the number:"))
x=0
y=0
for i in range(1,val+1):
        if(i%2!=0):
            x=x+7
        else:
           y=y+6
if(val%2!=0):
    print('{} term in accordance to the program is {}'. format(val,x-7))
else:
    print('{} term in accordance to the program is {}'. format(val,y-6))



text='india'
index=0
for i in text:
    print("text[",index,"]=",1)
    index +=1

text='india is great'
print(text.title())

text='India Is Great'
print(text.swapcase())

text='India,Is,Great'
print(text.split())
#join case
str='India','Is','Great'
print('-'.join(str))

str1='donkey'
print(list(enumerate(str1)))

str1='donkey monkey'
print(list(enumerate(str1)))


str1='88'
print(str1.zfill(4))

str1='jai balayya'
print(str1.upper())

str='JAI BALAYYA'
print(str.lower())

# slicing program
str1='Indian'
print(str1[::])

import string
print(string.digits)
print(string.ascii_letters)
chr='g'
print('a'<=chr<='z')


str1='hello'
print(dir(str1))


import re
str1="she sells sea shells at sea shore"
p1="sells"
if re.match(p1,str1):
        print("match found")
else:
        print(p1,"not present in the string")


import re
str1="she sells sea shells at sea shore"
p1="sells"
if re.search(p1,str1):
        print("match found")
else:
        print(p1,"not present in the string")

import re
str1="she sells sea shells at sea shore"
p1="sea"
rep="ocean"
ns=re.sub(p1,rep,str1,1)
print(ns)

import re
p=r"[aeiou]"
if re.search(p,"clue"):
        print("mathcy vowel")


import re
p=r"[consonants]"
if re.search(p,"clay"):
        print("matchy consonants")
else:
        prinrt("not matchy consonants")

n=int(input("enter the number:"))
a=0
b=0
for i in range(1,n+1):
        if(i%2!=0):
                a=a+2
else:
        b=b+1
if(n%2!=0):
        print('{}'.format(a-2))
else:
        print('{}'.format(b-1))



size=int(int(input("enter the size of bin")))
max=count=flag=0
x=input()
arr=list(x)
for i in range (0,size):
        if arr[1]=='1':
                count=count+1
                flag=1
        elif(arr[1]=='0' and flag==1):
                count=0
                flag=0
        if count>max:
                max=count
print(max)

                
                
        





















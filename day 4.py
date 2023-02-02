
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














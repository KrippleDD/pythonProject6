x=int(input())
s=0

while x!=0:

    x=int(input())

    s+=1

print(s)
######

max = min = x = int(input())
while x!=0:
   if x>max:
      max = x
   elif x<min:
      min = x
   x = int(input())
print(min, max)

######

x=1

s=-1

s1=0

while x!=0:

x=int(input())

if (x%2)==0:

 s+=1

else:

 s1+=1

print('P-',s,'\n','NeP-',s1)

#########
x=int(input())

s=0

while x != 0:
    sum += x
    x = int(input())

print(sum)

#####

x=int(input())

s=0

while x != 0:
    sum += x
    x = int(input())
    sredarif = sum // 2

print(sredarif)

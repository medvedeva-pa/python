integer = int(input())
sum = 0 
b = 0
while integer != 0 :
        b = integer%10
        integer = integer // 10
        sum += b
        b = 0
print (sum)
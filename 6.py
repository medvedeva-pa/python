number = int(input('integer '))
sum = 0 
b = 0
while number != 0 :
        b = number%10
        number = number // 10
        sum += b
        b = 0
print (sum)
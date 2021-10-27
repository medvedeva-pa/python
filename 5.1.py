def func1(lst,n):
    print('all numbers in list bigger than',n,':')
    for q in lst:
        if q > n:
            print(q)

numbers = [13, 2, 4, 18, 29, 27, 8, 1, -10, 148]
min = 12
func1(numbers,min)
print('Numbers divisible by 7 and 3 from 1 to 100:')
for a in range(1, 100 + 1):
    if (a % 7 == 0) & (a % 3 == 0):
        print(a)
print('Numbers divisible by 7 but not 3 from 1 to 100:')
for b in range(1, 100 + 1):
    if (b % 7 == 0) & (b % 3 != 0):
        print(b)
print('ODD Numbers divisible by 7 but not 3 from 1 to 100:')
for c in range(1, 100 + 1):
    if (c % 2 != 0) & (c % 7 == 0) & (c % 3 != 0):
        print(c)
print('Numbers divisible by the sum of its digits from 1 to 100:')


def check_div(number):
    remainder = 0
    sum = 0
    check = False
    n = number
    while n > 0:
        remainder = n % 10
        sum = sum + remainder
        n = n // 10
    if number % sum == 0:
        check = True
    return check


for i in range(1, 100 + 1):
    if check_div(i):
        print(i)
print('Numbers divisible by the the square of the sum of its digits from 1 to 100:')


def check_divi(numb):
    add = 0
    m = numb
    check = False
    while m > 0:
        rem = m % 10
        add = add + rem
        sqr = add * add
        m = m // 10
    if numb % sqr == 0:
        check = True
    return check


for k in range(1, 100 + 1):
    if check_divi(k):
        print(k)

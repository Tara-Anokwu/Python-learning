p = int (input('please type in the principal balance '))
r = float (input('please type in the interest rate '))
t = int (input('please type in the interest applied per period '))
n = int (input('please type the number of times the period elapsed '))
a = p*(1 + (r/n)) ** (n * t)
print('Hello user, the value of the compound interest is ',a)
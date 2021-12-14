from datetime import date
from datetime import datetime


#1.Функция arithmetic

def arithmetic(a,b,op):
    if(op=='+'):
        return a+b
    elif (op == '-'):
        return a - b
    elif (op == '/'):
        return a / b
    elif (op == '*'):
        return a * b
    else:
        return 'Неизвестная операция'

print(arithmetic(3,7,'+'))


#2.Функция square

def square(a):
    return (a*4,a*a,a*2**(1/2))
print(square(3))


#3.Функция bank

def bank(a,years):
    result=a
    for i in range(years):
        result=result*1.1
    return result
print(bank(100000,10))


#4.Функция is prime

def is_prime(number):
    n = number
    counter = 0
    for i in range(1, n + 1):
        if n % i == 0:
            counter += 1
    return True if counter == 2 else False
print(is_prime(100))


#5.Функция date

def date(d,m,y):
    get_date = lambda d: datetime.strptime(d, '%d.%m.%Y').date() <= datetime.today().date()
    try:
        assert get_date(''+d+'.'+m+'.'+y)
    except Exception:

        return False
    return True





print(bank(100,1))

print(data('30','09','2019'))

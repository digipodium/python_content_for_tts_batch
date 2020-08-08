
# wap to calculate total money

def money_calc(a, b=5, c=0):
    return a + b + c

# call
x = money_calc(1000)
x2 = money_calc(2000, 10)
x3 = money_calc(1000, 23, 2)
x4 = money_calc(1000,c=200)
x5 = money_calc(1000,b=200)

print('hello',end='.')
print(x,x2,x3,x4,x5)
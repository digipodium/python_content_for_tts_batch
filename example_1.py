# wap a function to display fibonacci range

def fib():
    data= [0,1]
    for i in  range(10):
        data.append(data[-1]+data[-2])
    print(data)

def fib2(size):
    data =[0,1]
    for i in range(size):
        data.append(data[-1]+ data[-2])
    return data
fib()
results = fib2(10)
print(results, sum(results))

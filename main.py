def fibonacci(a):
    if(a==0):
        return 0
    if(a==1):
        return 1
    return fibonacci(a-1)+fibonacci(a-2)
a=int(input())
print(fibonacci(a))

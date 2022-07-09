def fun1(num):
    return (num*(num+1))//2
# Time taken: C1*n

def fun2(num):
    sum=0
    for i in range(1,num+1):
        sum+=i
    return sum
# Time taken: (C2*n)+C3

def fun3(num):
    sum=0
    for i in range(1,num+1):
        for j in range(1,i+1):
            sum+=1
    return sum
# Time taken: (C4*n*n)+(C5*n)+C6


print(fun1(100))
print(fun2(100))
print(fun3(100))
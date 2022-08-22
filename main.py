a = [1,2,3]
b=a
print(a is b,a==b)

def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
res=fact(5)
print(res)
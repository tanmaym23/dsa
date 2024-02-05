def fibo(n):
    assert n>=0 and int (n)==n,"fibo no. cant be -ve or non int"
    if n in [0,1]:
        return n
    else:
        return fibo(n-1)+fibo(n-2)

print(fibo(7))
# fibonacci(7)
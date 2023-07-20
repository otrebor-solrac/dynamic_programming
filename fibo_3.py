def get_fibo_td(n,fib):        
    if fib[n] == -1:
        if n <= 1:
            fib[n] = n
        else:
            fib[n] = get_fibo_td(n-1,fib) + get_fibo_td(n-2,fib)
    return fib[n]

def fib(a, b, prev): return (a, b) if (abs(b/a - prev) < 1E-16) else fib(b, a+b, b/a)
print(fib(1, 1, 0))
    
    
  
  


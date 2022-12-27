def f():
    D = (b ** 2) - (4 * a * c)
    return D

a = int(input("a : "))
b = int(input("b : "))
c = int(input("c : "))    
result = f()
    
if result < 0:
    print("Rishe nadarad")
elif result == 0:
    print("2 rishe mosavi darad")
    result = (- b) / (2 * a)
    print(result)
else:
    x = - b + f() ** 0.5 / 2 * a
    y = - b - f() ** 0.5 / 2 * a
    print("\nx : " , x, "\ny : ", y)
f()

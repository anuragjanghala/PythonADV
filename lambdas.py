# lambda arguments: expression

add10 = lambda x: x+10
print(add10(5)) # 15

# alternative function for lambda function
def add10_function(x):
    return x + 10

mult = lambda x,y: x * y

print(mult(2, 7)) # 14



poinst2D = [(1,2), (15,1), (5,-1), (10,4)]
poinst2D_sorted = sorted(poinst2D)

print(poinst2D)
print(poinst2D_sorted)

poinst2D = [(1,2), (15,1), (5,-1), (10,4)]
poinst2D_sorted = sorted(poinst2D, key=lambda x: x[1])

print(poinst2D)
print(poinst2D_sorted)

poinst2D = [(1,2), (15,1), (5,-1), (10,4)]
poinst2D_sorted = sorted(poinst2D, key=lambda x: x[0]+x[1])

print(poinst2D)
print(poinst2D_sorted)

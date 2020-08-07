

def eq1(a,b,c):
    return a + b * c

print(eq1(1,2,3)) # normal params

out = eq1(a=1, b=2, c=5) # named parameter
out2 = eq1(b=2, a=1, c=3) # named parameter
print(out, out2)
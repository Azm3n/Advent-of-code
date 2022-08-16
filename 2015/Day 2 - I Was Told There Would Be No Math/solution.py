def ribbon(m1,m2,h):
     return m1*m2*h+2*m1+2*m2

def wrappingPaper(m1,m2,h):
    return 2*m1*m2+2*m1*h+2*m2*h+m1*m2

result01 = 0
result02 = 0

for x in open("./input-01.txt", "r"):
    y = x.strip().split("x")
    y = [ int(x) for x in x.strip().split("x") ]
    y.sort()
    result01 = result01 + wrappingPaper(y[0], y[1], y[2])
    result02 = result02 + ribbon(y[0], y[1], y[2])

print(result01, result02)

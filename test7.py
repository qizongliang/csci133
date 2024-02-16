def goalSeek(lowLimit, highLimit, target, polynomial):
    possiblePoly = []
    step = .01
    
    low = lowLimit
    high = highLimit
    
    while high > low:
        # 3 x^3 - 1.8 x^2 - 7.6 x - 20.8
        if( float(format(polynomial(low),".2f")) == target):
            possiblePoly.append(low)
        low+=step
        low = float(format(low,".2f"))
    
    return possiblePoly
# Use GoalSeek function to find the roots of the polynomials P1, p2, and P3 listed
# in the introduction. The expected answers are: 3,1.5, and -4.2. Choose the limits
# to contain the roots you are looking for ( -5 and 5 would suffice for these three
# polynomials). Confirm that your program is finding correct roots.
def P1(x):
    return x*x*x - x*x + 4*x - 30

def P2(x):
    return x*x*x + 0.5*x*x + x - 6

def P3(x):
    return 3*x*x*x + 13.6*x*x + 13.2*x + 37.8

print(goalSeek(-5,5,0.0,P1)[0])
print(goalSeek(-5,5,0.0,P2)[0])
print(goalSeek(-5,5,0.0,P3)[0])

# Read the file Poly.txt. Discard any line that starts with a # symbol
# For each non-header line, split it and use float function to extract A,B,C,D,Lo,
# and Hi. Print them out to confirm that your program correctly extracts these
# Parameters.

def cleanArr(arr):
    cleaned = []
    for item in arr:
        if(item != ''):
            cleaned.append(item)
    return cleaned
allPoly = []
with open('Poly.txt') as poly:
    for line in poly:
        if(line[0] != "#"):
            allPoly.append([float(x) for x in (cleanArr(line.split(" "))[:6:]) ] )

# Write a function makePoly that can generate a python function represenation of
# a cubic polynomial from its coefficients A, B, C, D. For example, the polynomial
# function P1 we used earlier
def makePoly(A,B,C,D):
    def polynomial(x):
        return (A*x*x*x) + (B*x*x) +(C*x)+(D)

    return polynomial


# For each polynomial you read from the file, use makePoly to generate its Python
# Function representation. Run Goalseek on this function with given Lo and Hi limits
# to find the root. You can use WolframAlpha to check that the roots are correct.
# After that, for each polynomial, print out its coefficients A, B, C, D followed
# by the root you found Format the output nicely making sure the columns line up
for poly in allPoly:
    A=poly[0]
    B=poly[1]
    C=poly[2]
    D=poly[3]
    root = goalSeek(poly[4],poly[5],0.0, makePoly(A,B,C,D))[0]
    print("{:>}{:>10}{:>10}{:>10}  ->{:>10}".format(A, B,C,D,root) )
        



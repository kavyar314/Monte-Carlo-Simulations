import random
def MonteCarloPi(n):
    incirc=0
    for i in range(n):
        x,y=random.random(), random.random()
        if x*x+y*y<1:
            incirc+=1
    return (incirc/float(n))*4.


#piapp=MonteCarloPi
#print piapp(100000000)

def skilledapprox(n):
    values=0
    for i in range(n):
        values=values+MonteCarloPi(100000000)
    return values/n

print skilledapprox(100)


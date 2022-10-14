
import math
import random

#Your task is to optimize a set of parameters for the new engine: Propeller blade angle 𝑎, number of 
#blades 𝑏, air/fuel ratio 𝛾, propeller diameter 𝑑 (mm), and idle valve position 𝜃. 
'''
def foo(a,b,y,d,c):
    return a**b+math.log(y)/d+c**3 - 870


def fitness(a,b,y,d,c):
    ans = foo(a,b,y,d,c)
    if ans ==0:
        return 9999
    else:
        return abs(1/ans)

solutions = []
for s in range(1000):
    solutions.append((random.uniform(0,10), random.uniform(0,2), random.uniform(0,0.55),random.uniform(0,100),random.uniform(0,0.5)))

#print(solutions[:5])

for i in range(10000):
    rankedsolutions = []
    for s in solutions:
        rankedsolutions.append((fitness(s[0],s[1],s[2], s[3], s[4]), s))
    rankedsolutions.sort()
    rankedsolutions.reverse()
    print(f"===Gen {i} best solutions ===")
    print(rankedsolutions[0])
    if rankedsolutions[0][0]> 999:
        break

    bestsolutions= rankedsolutions[:100]
    elemnts = []
    for s in bestsolutions:
        elemnts.append(s[1][0])
        elemnts.append(s[1][1])
        elemnts.append(s[1][2])
        elemnts.append(s[1][3])
        elemnts.append(s[1][4])
    newGen = []
    for _ in range(1000):
        e1 = random.choice(elemnts) * random.uniform(0.99,1.01)
        e2 = random.choice(elemnts) * random.uniform(0.99,1.01)
        e3 = random.choice(elemnts) * random.uniform(0.99,1.01)
        e4 = random.choice(elemnts) * random.uniform(0.99,1.01)
        e5 = random.choice(elemnts) * random.uniform(0.99,1.01)
        newGen.append((e1,e2,e3,e4,e5))
    solutions = newGen
'''
test =0.341593958123443**9.539547584001049+math.log(0.3684207967202283)/0.35358567294242643+9.556719978859112**3 - 870
print(test)
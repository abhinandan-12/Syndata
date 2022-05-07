import random, numpy

def generate(lim):
    data=[]
    #generate pair
    while True:
        num1=int(random.randint(0,lim))
        num2=int(random.randint(0,lim))
        #remove self connections
        if num1 != num2:
            unit=[num1,num2]
        else:
            continue
        #remove duplicates
        if unit or reversed(unit) not in data:
            data.append(unit)
            unit=[]
        else:
            unit=[]
            continue
        items = list(set(x[0] for x in data))
        #print(items)
        if sorted(items)==list(range(max(items)+1)):
            break
    return numpy.array(sorted(data))

inp=int(input("Enter your limit: "))
gen=(generate(inp-1))
print(gen)
choice=int(input("(1) Generate random or (2) Dump to static db : "))
if choice==1:
    numpy.savetxt('connections_generated.csv', gen, delimiter=',', fmt="%d")
elif choice==2:
    numpy.savetxt('db_connections.csv', gen, delimiter=',', fmt="%d")

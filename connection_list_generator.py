import random, string, numpy

def generate(lim):
    data=[]
    #generate pair
    while True:
        str1=str(random.choice(string.ascii_lowercase[0:lim]))
        str2=str(random.choice(string.ascii_lowercase[0:lim]))
        #remove self connections
        if str1 != str2:
            unit=[str1,str2]
        else:
            continue
        #remove duplicates
        if unit or reversed(unit) not in data:
            data.append(unit)
            unit=[]
        else:
            unit=[]
            continue
        if len(data)==lim:
            break
    return numpy.array(sorted(data))

inp=int(input("Enter your limit: "))
gen=(generate(inp))
print(gen)
numpy.savetxt('connections_generated.csv', gen, delimiter=',', fmt="%s")

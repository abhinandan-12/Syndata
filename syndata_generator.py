import numpy as np

def syndata(lim):
    data = []
    for i in range(0,lim):
       entries = [int(np.random.uniform(1, 21, 1)), #location
                 int(np.random.uniform(0, 2, 1)), #gender
                 int(np.random.uniform(1, 71, 1)), #age
                 int(np.random.uniform(1, 9, 1))] #education
       data.append(entries)
       entries = []
    data = np.array(data)
    return data

inp=int(input("Enter your limit: "))
gen=(syndata(inp))
print(gen)
np.savetxt('dumped.csv', gen, delimiter=',', fmt='%1.0f', header='location,gender,age,education')

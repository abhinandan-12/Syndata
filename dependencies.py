import os

#os definitions
if os.name=='nt': #windows
    shell='cmd /c '
    clr='cls'
elif os.name=='posix': #linux/mac
    shell=''
    clr='clear'

#install modules and libs
print("Checking required modules")
os.system(shell + 'pip3 install NetworkX sklearn numpy matplotlib scikit yellowbrick Node2vec graphviz pydot')
os.system(shell + clr)

#create dirs
dirs = ['Agglomerative','Birch','BisectingKMeans','KMeans','MiniBatchKMeans','Spectral']
os.system('mkdir Graphviz')
os.system('cd Graphviz')
for i in dirs:
    os.system('mkdir '+str(i))
os.system('cd ..')
os.system('mkdir Node2vec')
os.system('cd Node2vec')
for i in dirs:
    os.system('mkdir '+str(i))

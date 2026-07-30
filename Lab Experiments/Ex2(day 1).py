import numpy as np
def candidate_elimination(concepts, target):
    specific = concepts[0].copy()
    general = [["?" for _ in range(len(specific))]
               for _ in range(len(specific))]
    for i, instance in enumerate(concepts):
        if target[i] == "Yes":
            for j in range(len(specific)):
                if instance[j] != specific[j]:
                    specific[j] = '?'
                    general[j][j] = '?'
        else:
            for j in range(len(specific)):
                if instance[j] != specific[j]:
                    general[j][j] = specific[j]
                else:
                    general[j][j] = '?'
    general = [g for g in general if g != ['?'] * len(specific)]
    return specific, general
#--------------------------------
data=[
    ['Sunny','Warm','Yes'],
    ['Sunny','Cold','Yes'],
    ['Rainy','Warm','No'],
    ['Sunny','Warm','Yes']
]
S=data[0][:-1]
G=['?']*len(S)
for x in data:
    if x[-1]=='Yes':
        for i in range(len(S)):
            if S[i]!=x[i]:
                S[i]='?'
    else:
        for i in range(len(S)):
            if S[i]!=x[i]:
                G[i]=S[i]
    print("S=",S,"G=",G)
print("Final S=",S)
print("Final G=",G)
print("--------")
#--------------------------------
import numpy as np
data = np.array([
['Sunny','Warm','Normal','Strong','Warm','Same','Yes'],
['Sunny','Warm','High','Strong','Warm','Same','Yes'],
['Rainy','Cold','High','Strong','Warm','Change','No'],
['Sunny','Warm','High','Strong','Cool','Change','Yes']
])
concepts = data[:,:-1]
target = data[:,-1]
S,G = candidate_elimination(concepts,target)
print("Specific Hypothesis")
print(S)
print("\nGeneral Hypothesis")
for g in G:
    print(g)
    print("--------")
#-------------------------------------
import numpy as np
data = np.array([
['High','Good','Yes'],
['High','Average','Yes'],
['Medium','Good','No'],
['High','Excellent','Yes'],
['Low','Poor','No']
])
concepts=data[:,:-1]
target=data[:,-1]
S,G=candidate_elimination(concepts,target)
print("Specific:",S)
print("General:",G)
print("--------")
#-----------------------------------
import numpy as np
data=np.array([
['High','Good','Low','Yes'],
['High','Excellent','Low','Yes'],
['Medium','Good','High','No'],
['High','Average','Low','Yes'],
['Low','Poor','High','No']
])
concepts=data[:,:-1]
target=data[:,-1]
S,G=candidate_elimination(concepts,target)
print("Specific:",S)
print("General:")
for g in G:
    print(g)
    print("--------")
#------------------------------------
import numpy as np
data=np.array([
['Fever','Cough','Yes'],
['Fever','Cold','Yes'],
['Headache','Cold','No'],
['Fever','Sneezing','Yes']
])
concepts=data[:,:-1]
target=data[:,-1]
S,G=candidate_elimination(concepts,target)
print("Specific:",S)
print("General:")
for g in G:
    print(g)
    print("--------")
#---------------------------------------
import numpy as np

data=np.array([
['High','Experienced','Yes'],
['High','Medium','Yes'],
['Low','Experienced','No'],
['High','Beginner','Yes'],
['Low','Medium','No']
])

concepts=data[:,:-1]
target=data[:,-1]

S,G=candidate_elimination(concepts,target)

print("Specific:",S)

print("General:")
for g in G:
    print(g)
    print("--------")

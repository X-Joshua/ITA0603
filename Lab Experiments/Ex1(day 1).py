import numpy as np
def find_s(concepts, target):
    hypothesis = None
    # Find first positive example
    for i in range(len(target)):
        if target[i] == "Yes":
            hypothesis = concepts[i].copy()
            break
    # Update hypothesis
    for i in range(len(concepts)):
        if target[i] == "Yes":
            for j in range(len(hypothesis)):
                if hypothesis[j] != concepts[i][j]:
                    hypothesis[j] = '?'
    return hypothesis
#------------------------------------
data = [
    ['Sunny','Warm','Normal','Yes'],
    ['Sunny','Warm','High','Yes'],
    ['Rainy','Cold','High','No'],
    ['Sunny','Warm','High','Yes']
]
h = ['0'] * (len(data[0]) - 1)
for row in data:
    if row[-1] == 'Yes':
        if h[0] == '0':
            h = row[:-1]
        else:
            for i in range(len(h)):
                if h[i] != row[i]:
                    h[i] = '?'
    print(h)
print("Final Hypothesis:", h)
#------------------------------------
import numpy as np
data = np.array([
['Sunny','Warm','Normal','Strong','Warm','Same','Yes'],
['Sunny','Warm','High','Strong','Warm','Same','Yes'],
['Rainy','Cold','High','Strong','Warm','Change','No'],
['Sunny','Warm','High','Strong','Cool','Change','Yes']
])
concepts = data[:,:-1]
target = data[:,-1]
hypothesis = find_s(concepts,target)
print("Final Hypothesis")
print(hypothesis)
import numpy as np
data = np.array([
['High','Good','Yes'],
['High','Average','Yes'],
['Medium','Good','No'],
['High','Excellent','Yes'],
['Low','Poor','No']
])
concepts = data[:,:-1]
target = data[:,-1]
print(find_s(concepts,target))
#--------------------------------
import numpy as np

data = np.array([
['High','Good','Low','Yes'],
['High','Excellent','Low','Yes'],
['Medium','Good','High','No'],
['High','Average','Low','Yes'],
['Low','Poor','High','No']
])
concepts=data[:,:-1]
target=data[:,-1]
print(find_s(concepts,target))
#----------------------------
import numpy as np
data=np.array([
['Fever','Cough','Positive'],
['Fever','Cold','Positive'],
['Headache','Cold','Negative'],
['Fever','Sneezing','Positive']
])
concepts=data[:,:-1]
target=data[:,-1]
target=np.where(target=="Positive","Yes","No")
print(find_s(concepts,target))
#-----------------------------------
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
print(find_s(concepts,target))

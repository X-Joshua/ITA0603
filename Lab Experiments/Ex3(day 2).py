from sklearn.tree import DecisionTreeClassifier
X=[[0,0],[0,1],[1,0],[1,1]]
y=['No','No','Yes','Yes']
clf=DecisionTreeClassifier(criterion='entropy')
clf.fit(X,y)
print(clf.predict([[1,0]]))
print("-----------")
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
data = {
    'Outlook':['Sunny','Sunny','Overcast','Rain','Rain','Rain','Overcast','Sunny','Sunny','Rain','Sunny','Overcast','Overcast','Rain'],
    'Temperature':['Hot','Hot','Hot','Mild','Cool','Cool','Cool','Mild','Cool','Mild','Mild','Mild','Hot','Mild'],
    'Humidity':['High','High','High','High','Normal','Normal','Normal','High','Normal','Normal','Normal','High','Normal','High'],
    'Wind':['Weak','Strong','Weak','Weak','Weak','Strong','Strong','Weak','Weak','Weak','Strong','Strong','Weak','Strong'],
    'Play Tennis':['No','No','Yes','Yes','Yes','No','Yes','No','Yes','Yes','Yes','Yes','Yes','No']
}
df = pd.DataFrame(data)
le = LabelEncoder()
for col in df.columns:
    df[col] = le.fit_transform(df[col])
X = df.iloc[:, :-1]
y = df.iloc[:, -1]
model = DecisionTreeClassifier(criterion='entropy')
model.fit(X, y)
sample = pd.DataFrame({
    'Outlook':['Sunny'],
    'Temperature':['Cool'],
    'Humidity':['High'],
    'Wind':['Weak']
})
for col in sample.columns:
    encoder = LabelEncoder()
    encoder.fit(data[col])
    sample[col] = encoder.transform(sample[col])
prediction = model.predict(sample)
print("Prediction:",
      "Yes" if prediction[0]==1 else "No")
print("-----------")
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
data = {
    'CGPA':['High','High','Medium','Medium','Low','High','Low','Medium','High','Low'],
    'Communication':['Good','Excellent','Good','Average','Poor','Good','Average','Good','Excellent','Poor'],
    'Internship':['Yes','Yes','Yes','No','No','No','No','Yes','Yes','Yes'],
    'Programming':['Good','Excellent','Good','Average','Poor','Good','Average','Excellent','Good','Average'],
    'Placement':['Yes','Yes','Yes','No','No','Yes','No','Yes','Yes','No']
}
df = pd.DataFrame(data)
for col in df.columns:
    df[col] = LabelEncoder().fit_transform(df[col])
X = df.iloc[:, :-1]
y = df.iloc[:, -1]
model = DecisionTreeClassifier(criterion='entropy')
model.fit(X, y)
sample = pd.DataFrame({
    'CGPA':['High'],
    'Communication':['Good'],
    'Internship':['Yes'],
    'Programming':['Excellent']
})
for col in sample.columns:
    encoder = LabelEncoder()
    encoder.fit(data[col])
    sample[col] = encoder.transform(sample[col])
prediction = model.predict(sample)
print("Prediction:",
      "Yes" if prediction[0]==1 else "No")
print("-----------")
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
data = {
    'Income':['High','High','Medium','Low','Medium','High','Low','Medium','High','Low'],
    'Credit Score':['Good','Good','Good','Poor','Average','Average','Poor','Good','Good','Average'],
    'Employment':['Permanent','Permanent','Permanent','Temporary','Permanent','Temporary','Temporary','Permanent','Permanent','Temporary'],
    'Property':['Yes','No','Yes','No','No','Yes','Yes','Yes','Yes','No'],
    'Loan Approved':['Yes','Yes','Yes','No','Yes','No','No','Yes','Yes','No']
}
df = pd.DataFrame(data)
for col in df.columns:
    df[col] = LabelEncoder().fit_transform(df[col])
X = df.iloc[:, :-1]
y = df.iloc[:, -1]
model = DecisionTreeClassifier(criterion='entropy')
model.fit(X, y)
sample = pd.DataFrame({
    'Income':['Medium'],
    'Credit Score':['Good'],
    'Employment':['Permanent'],
    'Property':['Yes']
})
for col in sample.columns:
    encoder = LabelEncoder()
    encoder.fit(data[col])
    sample[col] = encoder.transform(sample[col])
prediction = model.predict(sample)
print("Prediction:",
      "Yes" if prediction[0]==1 else "No")
print("-----------")
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
data = {
    'Fever':['Yes','Yes','No','Yes','No','Yes','No','Yes','Yes','No'],
    'Cough':['Yes','Yes','Yes','No','No','Yes','Yes','No','Yes','No'],
    'Headache':['Yes','No','Yes','Yes','No','Yes','No','No','Yes','Yes'],
    'Body Pain':['Yes','Yes','No','Yes','No','No','Yes','Yes','Yes','No'],
    'Disease':['Positive','Positive','Negative','Positive','Negative','Positive','Negative','Positive','Positive','Negative']
}
df = pd.DataFrame(data)
for col in df.columns:
    df[col] = LabelEncoder().fit_transform(df[col])
X = df.iloc[:, :-1]
y = df.iloc[:, -1]
model = DecisionTreeClassifier(criterion='entropy')
model.fit(X, y)
sample = pd.DataFrame({
    'Fever':['Yes'],
    'Cough':['Yes'],
    'Headache':['No'],
    'Body Pain':['Yes']
})
for col in sample.columns:
    encoder = LabelEncoder()
    encoder.fit(data[col])
    sample[col] = encoder.transform(sample[col])
prediction = model.predict(sample)
print("Prediction:",
      "Positive" if prediction[0]==1 else "Negative")
print("-----------")
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
data = {
    'Experience':['High','High','Medium','Low','Medium','Low','High','Medium','High','Low'],
    'Performance':['Excellent','Good','Good','Average','Excellent','Poor','Good','Average','Excellent','Poor'],
    'Leadership':['Yes','Yes','No','No','Yes','No','Yes','No','Yes','No'],
    'Training':['Yes','Yes','Yes','No','Yes','No','No','Yes','Yes','Yes'],
    'Promotion':['Yes','Yes','Yes','No','Yes','No','Yes','No','Yes','No']
}
df = pd.DataFrame(data)
for col in df.columns:
    df[col] = LabelEncoder().fit_transform(df[col])
X = df.iloc[:, :-1]
y = df.iloc[:, -1]
model = DecisionTreeClassifier(criterion='entropy')
model.fit(X, y)
sample = pd.DataFrame({
    'Experience':['Medium'],
    'Performance':['Good'],
    'Leadership':['Yes'],
    'Training':['Yes']
})
for col in sample.columns:
    encoder = LabelEncoder()
    encoder.fit(data[col])
    sample[col] = encoder.transform(sample[col])
prediction = model.predict(sample)
print("Prediction:",
      "Yes" if prediction[0]==1 else "No")
print("-----------")

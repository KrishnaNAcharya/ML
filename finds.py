import numpy as np
import pandas as pd
print("\n The data from csv file is: \n")
data=pd.read_csv("E:\\Downlaods\\findseg.csv")
print(data)

#making an array of all the attributes
d = np.array(data)[:,:-1]
print("\n The attributes are: \n ",d)

#seperating the target that has +ve and -ve examples
target=np.array(data)[:,-1]
print("\n The target is :\n ",target)

#training function to implement find s algorithm
def train(c,t):
    for i,val in enumerate(t):
        if val=="Yes":
            specific_hypothesis=c[i].copy()
            break
    for i,val in enumerate(c):
        if t[i]=="Yes":
            for x in range(len(specific_hypothesis)):
                if val[x]!=specific_hypothesis[x]:
                    specific_hypothesis[x]='?'
                else:
                    pass
            break   
    return specific_hypothesis

print("The final hypothesis is ",train(d,target))                
           
        
        
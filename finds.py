import numpy as np
import pandas as pd
print("\n The data from csv file is: \n")
data=pd.read_csv("E:\\Downlaods\\findseg.csv")
print(data)

hypothesis=['%' for _ in range(len(data.columns)-1)]
positive_examples=data[data['enjoy_sport']=='Yes'].iloc[:,:-1].values.tolist()

for example in positive_examples:
    for i in range(len(example)):
        if hypothesis[i]!='%' and hypothesis[i]!=example[i]:
            hypothesis[i]='?'
        else:
            hypothesis[i]=example[i]
            
print(hypothesis)

        
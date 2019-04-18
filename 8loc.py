import pandas as pd
df=pd.DataFrame({'ID':[1,2,3],'Mark1':[30,50,90],'Mark2':[80,50,40]},index=['a','b','c'])
print(df.loc['a'])
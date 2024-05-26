import pandas as pd
df=pd.read_csv('task_2_dataset.csv')
l=[]
for i in range(0,len(df)):
    print("Theme: "+df.iloc[i]['Theme']+" SubTheme: "+df.iloc[i]['Subtheme'])
    val=input("Enter Validity: ")
    l.append(val)
df['Validity']=l
df.to_csv('sajan_shrestha_task2.csv')
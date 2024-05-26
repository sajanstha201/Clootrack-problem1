import pandas as pd
import numpy as np
path='task_2_dataset.csv'
def load_data(path):
    dataset=pd.read_csv(path)
    return dataset
def check_validity(domain,theme,subtheme):
    df=load_data(path)
    df.drop('Validity',axis=1,inplace=True)
    data=pd.DataFrame({
        'Domain':[domain],
        'Theme':[theme],
        'Subtheme':[subtheme]
    })
    for i in range(0,len(df)):
        if(all(data==df.iloc[i])):
            return True
    return False
    
if __name__=="__main__":
    domain=input("Enter the Domain: ")
    theme=input("Enter theme: ")
    subtheme=input("Enter sub theme: ")
    if check_validity(domain,theme,subtheme):
        print("This is valid")
    else:
        print("This is invalid")
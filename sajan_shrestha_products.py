import pandas as pd
import numpy as np

def load_file(dataset_path):
    dataset=pd.read_csv(dataset_path)
    return dataset
    
def find_sales_percentage(data):
    try:
        df=pd.DataFrame(data)
        new_data=pd.DataFrame(columns=['Category','Product','Sales'])
        for e in df.groupby(['Category','Product']):
            new_data=pd.concat([new_data,pd.DataFrame({
                'Category':[e[1]['Category'].values[0]],
                    'Product':[e[1]['Product'].values[0]],
                    'Sales':[np.sum(e[1]['Sales'].values)]})],ignore_index=True)
        l=new_data.groupby('Category')['Sales'].sum()
        new_data['total_sales']=[l[new_data.iloc[i]['Category']] for i in np.arange(0,len(new_data))]
        new_data['Sales Percentage']=new_data['Sales']/new_data['total_sales']*100
        new_data['Sales Percentage']=pd.to_numeric(new_data['Sales Percentage']).round(2)
        new_data.drop(['Sales','total_sales'],axis=1,inplace=True)
        return new_data
        print(new_data)
    except Exception as e:
        print("This is error from my code\n")
        print("Error message: ",e)

if __name__=="__main__":
    print("\n\nFor example: \nEnter the path of dataset: task1_dataset.csv\n\n\n")
    dataset_path=input("Enter the path of dataset: ")
    data=load_file(dataset_path)
    calcualted_data=find_sales_percentage(data)
    calcualted_data.to_csv('sajan_shrestha_products.csv',index=False)
    print(calcualted_data)


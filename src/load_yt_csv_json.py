import pandas as pd

def jsonlist_to_dataframe(jsonlist):
    df = pd.DataFrame(jsonlist)
    return df

def save_to_csv(df,filename):
    df.to_csv(filename,index=False)

def save_to_json(df,filename):
    df.to_json(filename)
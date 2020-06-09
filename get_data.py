import pandas as pd
df = pd.read_csv("dataframe.csv")

def harga (sayur):
    harga = df[df['Nama_sayur'] == sayur]['harga'] 
    return int(harga)

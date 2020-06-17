import pandas as pd
df = pd.read_csv("dataHarga.csv")

def harga (sayur):
    harga = df[df['nama_sayur'] == sayur]['harga'] 
    return int(harga)

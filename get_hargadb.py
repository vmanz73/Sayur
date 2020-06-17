import urllib.request, json 
import pandas as pd
def updt_harga(host):
    with urllib.request.urlopen(host + "/Sayur/db/harga_api.php") as url:
        data = json.loads(url.read().decode())
        df = pd.DataFrame(data)
        df.to_csv ('dataHarga.csv', index = False, header=True)

def get_harga(sayur):
    df = pd.read_csv("dataHarga.csv")
    harga = df[df['nama_sayur'] == sayur]['harga'] 
    return int(harga)

#print(get_harga("Kentang"))
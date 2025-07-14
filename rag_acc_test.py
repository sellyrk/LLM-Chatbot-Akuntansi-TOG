import pandas as pd
import requests
import json

# 1. Load CSV
df = pd.read_csv("transaksi.csv", sep=";")  # pastikan nama file sesuai
print("CSV loaded, sample:")
print(df.head())

# 2. Input pertanyaan user
pertanyaan = input("Masukkan pertanyaan akuntansi: ")

# 3. Buat context sederhana
# Contoh: jika pertanyaan tentang "pengeluaran transportasi Juli"
# maka filter dan hitung

context = ""
if "transport" in pertanyaan.lower() and "juli" in pertanyaan.lower():
    df['Tanggal'] = pd.to_datetime(df['Tanggal'])
    juli_df = df[(df['Tanggal'].dt.month == 7)]
    transport_df = juli_df[juli_df['Kategori'].str.contains('Transport', case=False, na=False)]
    transport_df['Jumlah'] = transport_df['Jumlah'].str.replace('_', '').astype(int)
    total = transport_df['Jumlah'].sum()
    context = f"Total pengeluaran transportasi pada bulan Juli adalah {total}."

else:
    context = "Tidak ada data relevan yang cocok secara otomatis, jelaskan manual."

# 4. Kirim ke LLaMA via REST API
# testing commit 
response = requests.post(
    'http://localhost:11434/api/generate',
    json={
        'model': 'llama3',
        'prompt': f"Pertanyaan: {pertanyaan}\nData: {context}\nJawab dengan bahasa sederhana."
    },
    stream=False
)

print("\nJawaban LLaMA:")
for line in response.text.splitlines():
    data = json.loads(line)
    if "response" in data:
        print(data["response"], end="", flush=True)
print()  

import sqlite3
import pandas as pd
import os




DATA_DIR = r'../data'
conn = sqlite3.connect('olist_ecommerce.db')

file_list = os.listdir(DATA_DIR)

for file_name in file_list:
    if file_name.endswith('.csv'):
        table_name = os.path.splitext(file_name)[0]
        full_path = os.path.join(DATA_DIR, file_name)

        try:
            # wczytanie plików csv i zrzut do SQL
            df_tmp = pd.read_csv(full_path)
            df_tmp.to_sql(table_name, conn, if_exists='replace', index=False)
        except Exception as e:
            print(f"Nieudane otworzenie pliku {file_name}: {e}")

conn.close()
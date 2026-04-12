import sqlite3
import pandas as pd
import os


#Wczytanie plików csv

path = r'../data'
fileList = os.listdir(path)
conn = sqlite3.connect('olist_ecommerce.db')

for fl in fileList:
    if fl.endswith('.csv'):
        try:
            full_path = os.path.join(path, fl)
            df_tmp = pd.read_csv(full_path)
            coll_name = os.path.splitext(fl)[0]
            df_tmp.to_sql(coll_name, conn, if_exists='replace', index=False)


        except Exception as e:
            print(f"Nieudane otworzenie pliku {fl}: {e}")

checkTables = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table'", conn)
print(checkTables)

conn.close()

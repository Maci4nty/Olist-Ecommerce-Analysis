import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

conn = sqlite3.connect('olist_ecommerce.db')
df = pd.read_sql_query("SELECT * FROM olist_orders_features", conn)

#konfiguracja stylu
sns.set_style("whitegrid")
plt.figure(figsize=(12,6))


#wykres 1: histogram czasu dostawy
plt.subplot(1, 2, 1)
sns.histplot(df['actual_delivery_time'].dropna(), bins=50, kde=True, color='teal')
plt.xlim(0, 60)
plt.title('Rozkład czasu dostawy zamówień')
plt.xlabel('Liczba dni')
plt.ylabel('Liczba zamówień')


#wykres 2: zamówienia w dniach tygodnia
plt.subplot(1, 2, 2)
mapa_dni = {0: 'Pon', 1: 'Wt', 2: 'Śr', 3: 'Czw', 4: 'Pt', 5: 'Sb', 6: 'Ndz'}
df['day_name'] = df['order_day'].map(mapa_dni)
sns.countplot(df, x=df['day_name'], order=['Pon', 'Wt', 'Śr', 'Czw', 'Pt', 'Sb', 'Ndz'])
plt.title('Liczba zamówień w dniach tygodnia')
plt.xlabel('Dzień tygodnia')
plt.ylabel('Liczba zamówień')

plt.tight_layout()
plt.show()

conn.close()



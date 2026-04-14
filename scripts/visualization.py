import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

conn = sqlite3.connect('olist_ecommerce.db')

df_orders_feat = pd.read_sql_query("SELECT * FROM olist_orders_features", conn)


sns.set_style("whitegrid")
plt.figure(figsize=(12,6))
plt.subplot(1, 2, 1)

sns.histplot(df_orders_feat['actual_delivery_time'].dropna(), bins=50, kde=True, color='teal')

plt.xlim(0, 60)
plt.title('Rozkład czasu dostawy zamówień')
plt.xlabel('Liczba dni')
plt.ylabel('Liczba zamówień')

plt.subplot(1, 2, 2)
mapa_dni = {0: 'Pon', 1: 'Wt', 2: 'Śr', 3: 'Czw', 4: 'Pt', 5: 'Sb', 6: 'Ndz'}
df_orders_feat['day_name'] = df_orders_feat['order_day'].map(mapa_dni)
sns.countplot(df_orders_feat, x=df_orders_feat['day_name'], order=['Pon', 'Wt', 'Śr', 'Czw', 'Pt', 'Sb', 'Ndz'])
plt.title('Rozkład czasu dostawy zamówień')
plt.ylabel('Liczba dni')
plt.xlabel('Liczba zamówień')


plt.tight_layout()
plt.show()

conn.close()



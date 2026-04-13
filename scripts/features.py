import sqlite3
import pandas as pd

conn = sqlite3.connect('olist_ecommerce.db')

df_orders = pd.read_sql_query("SELECT * FROM olist_orders_dataset", conn)



collName_delivery = ['order_delivered_customer_date', 'order_estimated_delivery_date', 'order_purchase_timestamp']
df_orders[collName_delivery] = (df_orders[collName_delivery]).apply(pd.to_datetime)

df_orders['time_rest'] = (df_orders['order_estimated_delivery_date'] - df_orders['order_delivered_customer_date']).dt.days
df_orders['actual_delivery_time'] = (df_orders['order_delivered_customer_date'] - df_orders['order_purchase_timestamp']).dt.days
df_orders['order_day'] = df_orders['order_purchase_timestamp'].dt.dayofweek


print(f"Średni czas dostawy w dniach: {df_orders['actual_delivery_time'].mean():.2f}")
print(f"Liczba spóźnionych zamówień: {df_orders[df_orders['time_rest'] < 0].shape[0]}")


#0 = Poniedziałek, 6 = Niedziela
print("\nLiczba zamówień w podziale na dni tygodnia:")
print(df_orders['order_day'].value_counts().sort_index())

df_orders.to_sql('olist_orders_features', conn, if_exists='replace', index=False)

conn.close()

import sqlite3
import pandas as pd

conn = sqlite3.connect('olist_ecommerce.db')

#pobranie danych
df_orders = pd.read_sql_query("SELECT * FROM olist_orders_dataset", conn)


#rzutowanie dat
date_cols = ['order_delivered_customer_date',
             'order_estimated_delivery_date',
             'order_purchase_timestamp']

df_orders[date_cols] = df_orders[date_cols].apply(pd.to_datetime)

#czas, który pozostał do szacowanej dostawy (wartości ujemne = spóźnienie)
df_orders['time_rest'] = (df_orders['order_estimated_delivery_date'] - df_orders['order_delivered_customer_date']).dt.days

#faktyczny czas dostawy
df_orders['actual_delivery_time'] = (df_orders['order_delivered_customer_date'] - df_orders['order_purchase_timestamp']).dt.days

#dzień tygodnia (0 = Poniedziałek, 6 = Niedziela)
df_orders['order_day'] = df_orders['order_purchase_timestamp'].dt.dayofweek

#zapis do nowej tabeli
df_orders.to_sql('olist_orders_features', conn, if_exists="replace", index=False)

conn.close()

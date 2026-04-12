import sqlite3

import pandas as pd

orders = '../data/olist_orders_dataset.csv'
clients = '../data/olist_customers_dataset.csv'
conn = sqlite3.connect('olist_ecommerce.db')
df_orders = pd.read_sql_query("SELECT * FROM olist_orders_dataset", conn)
df_clients = pd.read_sql_query("SELECT * FROM olist_customers_dataset", conn)

#missing values
res = df_orders.isnull().sum()
count = res.sum()

print(f"Ile danych brakuje: {count}")


#correct data type
collName = ['order_purchase_timestamp','order_approved_at', 'order_delivered_carrier_date',
            'order_delivered_customer_date', 'order_estimated_delivery_date']

df_orders[collName] = (df_orders[collName]).apply(pd.to_datetime)
print(df_orders.dtypes)
print()

#counting customers id and unique id
cust_id = df_clients['customer_id'].nunique()
print(cust_id)
print()
unique_cust_id = df_clients['customer_unique_id'].nunique()
print(unique_cust_id)

conn.close()


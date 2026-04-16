import pandas as pd
import sqlite3

conn = sqlite3.connect('olist_ecommerce.db')

query = ("""WITH clientOrder AS (
                    SELECT c.customer_state, 
                    o.order_id, 
                    (julianday(o.order_delivered_customer_date) - julianday(o.order_purchase_timestamp)) AS 'actual_delivery_time'
                    FROM olist_customers_dataset c
                    JOIN olist_orders_dataset o ON
                    c.customer_id = o.customer_id),
                    sellerOrder AS (
                    SELECT DISTINCT i.order_id, s.seller_state
                    FROM olist_order_items_dataset i
                    JOIN olist_sellers_dataset s
                    ON i.seller_id = s.seller_id)
                
                    SELECT co.order_id,
                     co.actual_delivery_time,
                     co.customer_state,
                     so.seller_state,
                     CASE
                        WHEN co.customer_state = so.seller_state THEN 1
                        ELSE 0
                    END AS is_same_state
                    FROM clientOrder co
                    JOIN sellerOrder so
                    ON so.order_id = co.order_id""")

geo_analysis = pd.read_sql_query(query, conn)

geo_analysis.to_sql('delivery_geo_analysis', conn, if_exists='replace', index=False)

conn.close()
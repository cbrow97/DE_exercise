from all_fields import *

df = generate_customer_fields()
df = create_txn_df(df) 
df = generate_txt_id(df) 
df = generate_txn_line_items(df)  
df = set_store_values(df)
df = set_purchase_info(df)
df = generate_cc_info(df)

#shuffle and save dataset
df.to_csv('transactions_full.csv').sample(frac=1)

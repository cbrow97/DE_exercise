from fact_table import *
from pandas as pd
df_source_txn_fact = df_source[fact_txn_source_fields].drop_duplicates().set_index('TransactionID')
factTXN = pd.concat([set_dim_keys(dim_cust_join_logic, create_cust_full_name), set_dim_keys(dim_store_join_logic), df_source_txn_fact], axis=1)
factTXN = factTXN.reset_index()
factTXN = factTXN.rename(columns={'index':'TransactionID'})

factTXN.to_csv("../factTables_csv/factTXN.csv", index=False)
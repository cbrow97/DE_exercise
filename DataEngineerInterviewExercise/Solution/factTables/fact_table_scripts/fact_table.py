# %%
import pandas as pd
import fact_table_config as fact_cfg
from join_logic import *


def create_cust_full_name(df):
    df['FullName'] = df['FirstName'] + ' ' + df['LastName']
    return df

def set_dim_keys(join_logic, *table_specific_transformations, index='TransactionID'):
    dim, cust_join_left_on, source, cust_join_right_on, cust_fields_to_keep = join_logic._asdict().values()

    for table_specific_transformation in table_specific_transformations:
        dim = table_specific_transformation(dim)    

    df = pd.merge(dim,
                  source,
                  left_on=cust_join_left_on,
                  right_on=cust_join_right_on)

    df = df[cust_fields_to_keep].drop_duplicates()
    return df.set_index([index])

df_source_txn_fact = df_source[fact_txn_source_fields].drop_duplicates().set_index('TransactionID')
factTXN = pd.concat([set_dim_keys(dim_cust_join_logic, create_cust_full_name), set_dim_keys(dim_store_join_logic), df_source_txn_fact], axis=1)
factTXN = factTXN.reset_index()
factTXN = factTXN.rename(columns={'index':'TransactionID'})

factTXN
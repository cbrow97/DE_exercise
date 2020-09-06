from dim_table_scripts.dim_table import *
import pandas as pd

df_source = pd.read_csv("transactions_full.csv")

dimCustomers = create_dim_table(df_source, dim_cfg.customer, spilt_name_field, id_field_name='CustomerID')
dimCustomers.to_csv('..\dimTables_csv\dimCustomers.csv', index=False)

dimStores = create_dim_table(df_source, dim_cfg.store, clean_store_addresses, expand_region_abrvs, id_field_name='StoreID')
dimStores.to_csv('..\dimTables_csv\dimStores.csv', index=False)

dimProducts = create_dim_table(df_source, dim_cfg.product, id_field_name='ProductID')
dimProducts.to_csv('..\dimTables_csv\dimProducts.csv', index=False)


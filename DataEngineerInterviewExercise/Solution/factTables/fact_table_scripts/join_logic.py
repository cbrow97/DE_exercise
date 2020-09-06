import pandas as pd
import fact_table_config as fact_cfg
from collections import namedtuple

#Read in files
df_source = pd.read_csv("../transactions_full.csv")
dimCustomers = pd.read_csv("../dimCustomers.csv")
dimProducts = pd.read_csv("../dimProducts.csv")
dimStores = pd.read_csv("../dimStores.csv")

#Create join logic object
join_logic_args = namedtuple('join_logic', 'left_df left_on right_df right_on fields_to_keep')

#Set customer join logic
cust_join_left_on = ['FullName', 'Email', 'City', 'ZipCode']
cust_join_right_on = ['cstName', 'Email', 'City', 'Zip']
cust_fields_to_keep = ['TransactionID', 'CustomerID']
dim_cust_join_logic = join_logic_args(dimCustomers, cust_join_left_on, df_source, cust_join_right_on, cust_fields_to_keep)

#Set store join logic
store_join_left_on = ['StoreName', 'ZipCode']
store_join_right_on = ['Name', 'ZipCode_2']
store_fields_to_keep = ['TransactionID', 'StoreID']
dim_store_join_logic = join_logic_args(dimStores, store_join_left_on, df_source, store_join_right_on, store_fields_to_keep)

#Set product join logic
product_join_left_on = ['ProductName', 'Description', 'Category']
product_join_right_on = ['ItemName', 'Description', 'Category']
product_fields_to_keep = ['TransactionID', 'ProductID']
dim_product_join_logic = join_logic_args(dimProducts, product_join_left_on, df_source, product_join_right_on, product_fields_to_keep)

#Transaction fact table fields from source
fact_txn_source_fields = ['TransactionID', 'Amount', 'PurchaseDate']

#Transaction line item fact table fields from source
fact_txn_line_item_source_fields = ['TransactionID', 'Quantity']
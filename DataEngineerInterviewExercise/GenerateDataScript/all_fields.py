import pandas as pd
from collections import namedtuple
import numpy as np
import random
import names
import string
import pycountry
import datetime
import rand_val_funcs as rnd
import fake_data as fd

def generate_customer_fields(num_customers=100):
    email_suffixes = ['@gmail.com', '@yahoo.com', '@aol.com', '@hotmail.com', '@comcast.net', '@msn.com']
    cities = ['Seattle', 'Spokane', 'Olympia', 'Tacoma', 'Bellevue', 'Bellingham',
             'Portland', 'Salem', 'Bend', 'Eugene', 'Oregon City', 'Medford',
             'Los Angeles', 'San Diego', 'San Francisco', 'Sacramento', 'San Jose']
    area_codes = [360, 509, 425, 206, 253, 541, 458, 503, 209, 213, 714, 510, 707]
    df = pd.DataFrame(index=range(0, num_customers))

    for i in range(0, len(df) + 1):
        
        df.loc[i, 'cstName'] = names.get_full_name()
        df.loc[i, 'Email'] = str(df.loc[i, 'cstName']).replace(' ', random.choice(['_', '', '-', random.choice(string.ascii_letters)])) \
                                                    + str(np.random.randint(0, 1000)) \
                                                    + random.choice(email_suffixes)
        df.loc[i, 'City'] = random.choice(cities)
        df.loc[i, 'Zip'] = str(np.random.randint(30000, 99999))
        df.loc[i, 'PhoneNumber'] = str(random.choice(area_codes)) + str(np.random.randint(1000000, 9999999))
        df.loc[i, 'Country'] = random.choice(list(pycountry.countries)).name
        df.loc[i, 'CreateDate'] = rnd.generate_random_date(date_format='%b/%d/%Y')
    return df

def create_txn_df(df_customers, txn_count_max=6):
    for i in range(0, len(df_customers)):
        #create a random number of line item rows for the transaction and append to df 
        for row in range(0, np.random.randint(txn_count_max)):
            df_customers = df_customers.append(df_customers.loc[i, :], ignore_index=True)

    return df_customers

def generate_txt_id(df_txn, unique_field='cstName'):
    unique_txns = df_txn[unique_field].unique()
    for unique_val in unique_txns:
        for i in df_txn[df_txn[unique_field]==unique_val].index:
            df_txn.loc[i, 'TransactionID'] = str(np.random.randint(10000, 99999)) + '-' + str(np.random.randint(1000, 9999)) 
            df_txn.loc[i, 'PurchaseDate'] = rnd.generate_random_date(start_date=datetime.date(2019, 1, 1))

    return df_txn

def generate_txn_line_items(df, line_item_max=6):
    for i in range(0, len(df)):
        for row in range(0, np.random.randint(line_item_max)):
            df = df.append(df.loc[i, :], ignore_index=True)

    return df

def set_store_values(df, unique_field='TransactionID'):
    unique_vals = df[unique_field].unique()

    for val in unique_vals:
        current_store = random.choice(list(fd.stores.values()))
        df.loc[df[unique_field] == val, 'Name'] = current_store.name 
        df.loc[df[unique_field] == val, 'Region'] = current_store.region
        df.loc[df[unique_field] == val, 'ZipCode_2'] = current_store.zip_code
        df.loc[df[unique_field] == val, 'StreetAddress'] = current_store.street_address
        
    return df      

def set_purchase_info(df, unique_field='TransactionID', summed_amount_field=True):
    unique_vals = df[unique_field].unique()

    for val in unique_vals:
        for i in df[df[unique_field] == val].index:
            current_product = random.choice(list(fd.products.values()))
            
            df.loc[df.index == i, 'ItemName'] = current_product.item_name 
            df.loc[df.index == i, 'Description'] = current_product.description
            df.loc[df.index == i, 'Category'] = current_product.category

            qty = np.random.randint(1, 6)
            df.loc[df.index == i, 'ItemPrice'] = current_product.price
            df.loc[df.index == i, 'LineItemAmount'] = df.loc[df.index == i, 'ItemPrice'] * qty
            df.loc[df.index == i, 'Quantity'] = qty     

    if summed_amount_field:
        df= pd.merge(df, 
                     df.groupby('TransactionID', as_index=False)['LineItemAmount'].sum().rename(columns={'LineItemAmount':'Amount'}),
                     on='TransactionID')

    return df

def generate_cc_info(df, unique_field='TransactionID'):
    unique_vals = df[unique_field].unique()

    for val in unique_vals:
        df.loc[df[unique_field] == val, 'CCNumber'] = str(np.random.randint(4, 6)) + ''.join([str(np.random.randint(9)) for num in range(0, 15)])
        df.loc[df[unique_field] == val, 'CardSecurityCode'] = str(np.random.randint(100, 999))

    return df



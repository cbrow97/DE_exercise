import pandas as pd
import dim_table_scripts.dim_table_config as dim_cfg
from collections import namedtuple
import us
import string

def spilt_name_field(df):
    df[['FirstName', 'LastName']] = df['FirstName'].str.split(expand=True)
    return df


def clean_store_addresses(df):
    df['StreetAddress'] = df['StreetAddress'].str.translate(str.maketrans('', '', string.punctuation))
    return df

def expand_region_abrvs(df):
    df['Region'] = df['Region'].apply(lambda x: us.states.lookup(x).name)
    return df

def create_dim_table(df, field_info, *table_specific_transformations, order_columns=True, id_field_name='ID'):
    #TODO -

    #Create lists of the prod_fields and source_fields only if the fields are not NA in source data
    prod_fields, source_fields = zip(*[(prod_f, src_f) for prod_f, src_f in list(field_info._asdict().items()) if src_f != 'NA'])
    df = df.loc[:, source_fields].drop_duplicates().reset_index(drop=True)
    
    #Rename the source columns to the prod column names
    df.columns = prod_fields

    #Use the reset index value as the dimTable ID
    df[id_field_name] = df.index

    #If any exist, process table specific transformation functions
    for table_specific_transformation in table_specific_transformations:
        df = table_specific_transformation(df)
    
    #If a field order list is passed, reorder the columns
    if order_columns: df = df[list(field_info._fields)]
    return df

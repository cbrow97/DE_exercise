from collections import namedtuple

#Dim customer fields
dim_cust_fields = namedtuple('dimCustomer', 'CustomerID FirstName LastName Email City ZipCode PhoneNumber FavCountry CreateDate')
customer = dim_cust_fields('NA', 'cstName', 'NA','Email', 'City', 'Zip', 'PhoneNumber', 'Country', 'CreateDate')

#Dim product fields
dim_product_fields = namedtuple('dimProduct', 'ProductID ProductName Description Category')
product = dim_product_fields('NA', 'ItemName', 'Description', 'Category')

#Dim store fields
dim_store_fields = namedtuple('dimProduct', 'StoreID StoreName StreetAddress ZipCode Region')
store = dim_store_fields('NA', 'Name', 'StreetAddress', 'ZipCode_2', 'Region')
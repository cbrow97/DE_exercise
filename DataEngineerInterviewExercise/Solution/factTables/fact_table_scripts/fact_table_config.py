from collections import namedtuple

#Fact transactions fields
fact_txn_fields = namedtuple('factTXN', 'TransactionID PurchaseDate CustomerID StoreID, TransactionAmount')
transaction = fact_txn_fields('TransactionID', 'PurchaseDate', 'CustomerID', 'StoreID', 'Amount')

#Fact transaction line items fields
fact_txn_item_fields = namedtuple('factTXNItems', 'TransactionID LineItemID ProductID Quantity')
transaction_item = fact_txn_item_fields('TransactionID', 'NA', 'ProductID', 'Quantity')


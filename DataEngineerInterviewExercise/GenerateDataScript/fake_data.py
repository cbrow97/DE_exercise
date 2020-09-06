from collections import namedtuple

product_fields = namedtuple('products', 'item_name description category price')
products = {
    'product_1'  :  product_fields('cactus', 'a beautiful prickly', 'plants', 10),
    'product_2'  :  product_fields('seeds', 'misc plant seeds', 'plants', 15),
    'product_3'  :  product_fields('green algae', '', 'plants', 2),
    'product_4'  :  product_fields('fern', 'has leaves', 'plants', 25),
    'product_5'  :  product_fields('peace lily', 'white pedal', 'plants', 100),

    'product_6'  :  product_fields('coke', '12 oz', 'beverage', 1.25),
    'product_7'  :  product_fields('coke', '16 oz', 'beverage', 2.95),
    'product_8'  :  product_fields('coke', '24 oz', 'beverage', 4.50),
    'product_9'  :  product_fields('water', '4 oz', 'beverage', 0.95),
    'product_10' :  product_fields('water', '6 oz', 'beverage', 1.95),
    'product_11' :  product_fields('water', '24 oz', 'beverage', 2.95),


    'product_12' :  product_fields('chips', 'generic chip', 'food', 2.00),
    'product_13' :  product_fields('fruit', 'farmers market generic', 'food', 5.00),
    'product_14' :  product_fields('bread', 'single sliced', 'food', 4),
    'product_15' :  product_fields('sandwich', 'premade', 'food', 12.44),
    'product_16' :  product_fields('candy', 'variety pack', 'food', 3.25),
    'product_17' :  product_fields('cereal', '12 oz bag', 'food', 4),

    'product_18' :  product_fields('tissues', '', 'toiletries', 5.00),
    'product_19' :  product_fields('tooth paste', '', 'toiletries', 2.30),
    'product_20' :  product_fields('', '', 'toiletries', 10000),

}

store_fields = namedtuple('stores', 'name region zip_code street_address')
stores = {
    'store_1'  :  store_fields('West Port Goods', 'WA', '98788', '8052 Adipiscing, Street'),
    'store_2'  :  store_fields('The Corner Store', 'Washington', '98000', '8516 Amet St.'),
    'store_3'  :  store_fields('Not Just Groceries', 'CA', '97888', '1437 Sed, Av.'),
    'store_4'  :  store_fields('Wholesome', 'California', '98182', '4942 Ac Rd.'),
    'store_5'  :  store_fields('Authentic Shoppe', 'OR', '96587', '5111 Penatibus Rd'),
    'store_6'  :  store_fields('The Full Cart', 'Oregon', '93455', '5342 Ligula. Ave'),
    'store_7'  :  store_fields('Healthy Treats', 'WA', '91222', '8390 Integer St'),
    'store_8'  :  store_fields('Yummy Store', 'WA', '98001', '9128 Egestas Avenue'),
}

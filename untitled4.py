# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rWl2YGBhW_xae-Ktc3JJh4o6-KwiOaWg
"""

items = {'azeitona': {'price': 9.45,   'stock': 6, 'code':123},
         'leite':  {'price': 3.34,   'stock': 0,'code':1231},
         'açúcar': {'price': 2.12, 'stock': 32,'code':1233},
         'farinha':   {'price': 4.67,   'stock': 15,'code':12335},
         'fermento':   {'price': 1.88,   'stock': 15,'code':12337},
         'vinagre':   {'price': 5.56,   'stock': 15,'code':12340},
        }

bar=int(input("enter barcode:"))
sum = 0
price =[]
products =[]
for key in items:
    if items[key]['code'] == int(bar):
        print("item found")
        print (key)
        print ("price: %s" % items[key]['price'])
        print ("stock: %s" % items[key]['stock'])
        print ("Barcode: %s" % items[key]['code'])
        price.append(items[key]['price'])
        products.append(key)

        print(price)
        print(products)
        print("..............................................")
        while True:

            choice = input("scan another item?y/n")
            if choice =='n':
                for cost in price:
                    sum += cost
                    print("Total cost:",sum)
                    print("..............................................")


            if choice =='y':


                bar=int(input("enter barcode:"))


                for key in items:

                    if items[key]['code'] == int(bar):
                        print("item found")
                        print (key)
                        print ("price: %s" % items[key]['price'])
                        print ("stock: %s" % items[key]['stock'])
                        print ("Barcode: %s" % items[key]['code'])
                        price.append(items[key]['price'])
                        products.append(key)
                    #print(price)
import json

import openpyxl


"price_list": [
        {
            "item_description": "Product 1",
            "sku": "19010",
            "ean": "123456789012",
            "variants": [
                "M",
                "White"
            ],
            "qty": "1",
            "price": "970,40",
            "retail_price": "1261,52"
        },

book = openpyxl.Workbook()

sheet = book.active
sheet ['A1'] = 'item_description'
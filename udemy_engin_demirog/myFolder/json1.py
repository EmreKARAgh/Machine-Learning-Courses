# -*- coding: utf-8 -*-

import json


data = '{"firstName":"Emre", "lastName":"Kara"}'
js1 = json.loads(data)

print("js1:")
print(js1)
print(js1["firstName"])
print(js1["lastName"])

customer= {
        "firstName":"Emre",
        "lastName":"Kara"
        }
js2 = json.dumps(customer)

print("\n\njs2:")
print(js2)



import os
import sys

sys.path.append(os.path.realpath(''))
from product_API import productAPI


def test(type):
    api = productAPI()
    if type == "setup":
        return api.create_data()
    elif type == "query":
        category = input('Please Enter your category (watch/wine): ')
        filters = input('Please Enter your filters, separated by , (e.g brand:Rolex,diameter:44mm): ')
        return api.search_data(category, filters)
    else: return "Please specify valid action: setup or query"

method = input('Do you want to create new data or search data (setup/query): ')
results = test(method)
print(results)




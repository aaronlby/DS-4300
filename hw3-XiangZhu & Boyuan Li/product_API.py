from pymongo import MongoClient

class productAPI:
    def __init__(self):
        self.client = MongoClient()

    def create_data(self):
        self.client.drop_database("product_db")
        # establish a database
        db = self.client['product_db']

        # create a collection
        products_collection = db["products"]

        datalist = [
            {"category": "watch", "diameter": "44mm", "brand": "Rolex", "dial_color": "Green", 'availability':'Out of stock', 'price':'$9,000'},
            {"category": "watch", "diameter": "43mm", "brand": "Tommy Hilfiger", "dial_color": "Beige", 'availability':'Available', 'price':'$200'},
            {"category": "watch", "diameter": "42mm", "brand": "Rolex", "dial_color": "Black", 'availability':'Out of stock', 'price':'$8,500'},
            {"category": "watch", "diameter": "42mm", "brand": "Tissot", "dial_color": "Silver", 'availability':'Available', 'price':'$2,000'},
            {"category": "watch", "diameter": "42mm", "brand": "G-SHOCK", "dial_color": "White", 'availability':'Available', 'price':'$500'},
            {"category": "watch", "diameter": "42mm", "brand": "G-SHOCK", "dial_color": "Blue", 'availability':'Out of stock', 'price':'$300'},
            {"category": "watch", "diameter": "44mm", "brand": "Tommy Hilfiger", "dial_color": "Black", 'availability':'Available', 'price':'$400'},
            {"category": "wine", "winery": "Château Lafite-Rothschild", "type": "Cahrdonnay", "year_bottled": "1982", 'availability':'Out of stock', 'price':'$12,000'},
            {"category": "wine", "winery": "Erath", "type": "Pinot Noir", "year_bottled": "2000", 'availability':'Out of stock', 'price':'$100'},
            {"category": "wine", "winery": "Château Lafite-Rothschild", "type": "Cahrdonnay", "year_bottled": "1999", 'availability':'Available', 'price':'$200'},
            {"category": "wine", "winery": "Erath", "type": "Pinot Noir", "year_bottled": "2006", 'availability':'Available', 'price':'$90'},
            {"category": "wine", "winery": "Dark Horse", "type": "Zinfandel", "year_bottled": "1999", 'availability':'Available', 'price':'$350'},
            {"category": "wine", "winery": "Erath", "type": "Zinfandel", "year_bottled": "2018", 'availability':'Available', 'price':'$800'}
        ]
        # Insert the data to the database
        products_collection.insert_many(datalist)
        data = products_collection.find()
        for x in data:
            # Display the data just inserted
            print(x)

    def search_data(self, category,filters):
        db = self.client['product_db']
        products_collection = db["products"]
        search_dict = {"category": category}
        filter_list = filters.split(',')
        for item in filter_list:
            x = item.strip()
            k = x.split(':')[0].strip()
            v = x.split(':')[1].strip()
            search_dict[k] = v

        result = products_collection.find(search_dict)

        if result.count() != 0:
            for r in result:
                print(r)
        else:
            print("No results found. Please use different inputs!")
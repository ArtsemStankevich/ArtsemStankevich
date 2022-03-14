import datetime
class Producty:
    def __init__(self):
        self.products = []

    @staticmethod
    def _get_datetime():
        return datetime.datetime.now()
    
    def add_product(self, prod, price, shop):
        self.products.append([prod, price, self._get_datetime(), shop])
    
    def show_products(self):
        for prod, price, date, shop in self.products:
            print(f'Product-{prod} price-{price} shop-{shop} date-{date}')
    
    def delete_product(self):
        self.products.pop(len(self.products)-1)
        

a = Producty()
a.add_product('Kasha', 10, 'Biedronka')
a.add_product('Piwo', 20, 'Green')
a.show_products()
a.delete_product()
a.show_products()
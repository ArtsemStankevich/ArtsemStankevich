import datetime
import requests
import json
api_key = 'c401c889626ad77d525f21da3006925a'
list_of_cites = []
list_of_objects_cites = []
list_of_objects_shops = []
def get_datetime():
    return datetime.datetime.now()

class Product:
    def __init__(self, product):
        self.product = product

class Shop():
    def __init__(self, name):
        self.shop_name = name
        self.shop = []

    def return_shop(self):
        return self.shop_name

    def add_product(self, prod):
        self.shop.append(prod)

    def show_products_in_shop(self):
        print(self.shop_name)
        number = 1
        for prod in self.shop:
            print(number,".", prod.product)
            number = number + 1

class City():
    def __init__(self, city):
        self.name_of_city = city
        self.shops_in_city = []
        list_of_cites.append(self.name_of_city)

    def return_city(self):
        return self.name_of_city

    def add_shop_to_city(self, shop):
        self.shops_in_city.append(shop)

    def show_shops_in_city(self):
        print(self.name_of_city)
        number = 1
        for shop in self.shops_in_city:
            print(number,".", shop.shop_name)
            number = number + 1
    
class Weather:
    def __init__(self, city):
        self.weather_in_city_name = city

    def _get_lat(self):
        api_city = f"http://api.openweathermap.org/geo/1.0/direct?q={self.weather_in_city_name}&limit=1&appid={api_key}"
        res_city = requests.get(api_city)
        data_city = json.loads(res_city.text)
        lat = data_city[0]["lat"]
        return lat

    def _get_lon(self):
        api_city = f"http://api.openweathermap.org/geo/1.0/direct?q={self.weather_in_city_name}&limit=1&appid={api_key}"
        res_city = requests.get(api_city)
        data_city = json.loads(res_city.text)
        lon = data_city[0]["lon"]
        return lon



    def weather_in_city(self):
        api_city = f"http://api.openweathermap.org/geo/1.0/direct?q={self.weather_in_city_name}&limit=1&appid={api_key}"
        res_city = requests.get(api_city)
        data_city = json.loads(res_city.text)
        lat = data_city[0]["lat"]
        lon = data_city[0]["lon"]
        api_weather = f'http://api.openweathermap.org/data/2.5/weather?lat={self._get_lat()}&lon={self._get_lon()}&appid={api_key}'
        res_weather = requests.get(api_weather)
        data_weather = json.loads(res_weather.text)
        self.description = data_weather['weather'][0]['description']
        temp = data_weather['main']['temp']
        self.speed = data_weather['wind']['speed']
        self.temp = int(temp) - 273

    def show_weather_in_city(self):
        print(f"Weather in city {self.weather_in_city_name} :")
        print("Temperature:", self.temp)
        print("Wind speed:", self.speed)
        print("Description:", self.description)


Kasha = Product("Kasha")
Makarony = Product("Makarony")
Piwo = Product("Piwo")
Krevetki = Product("Krevetki")
Chipsy = Product("Chipsy")

Biedronka = Shop("Biedronka")
Biedronka.add_product(Kasha)
Biedronka.add_product(Makarony)
Biedronka.add_product(Krevetki)
Zabka = Shop("Zabka")
Zabka.add_product(Kasha)
Zabka.add_product(Makarony)
Zabka.add_product(Piwo)
Zabka.add_product(Chipsy)

Gdansk = City("Gdansk")
list_of_objects_cites.append(Gdansk)
Gdansk.add_shop_to_city(Biedronka)
Gdansk.add_shop_to_city(Zabka)
Warsaw = City("Warsaw")
list_of_objects_cites.append(Warsaw)
Warsaw.add_shop_to_city(Biedronka)
Warsaw.add_shop_to_city(Zabka)
list_of_objects_shops.append(Biedronka)
list_of_objects_shops.append(Zabka)

shopping_list = [[]]
shopping_list_number = 0

Gdansk_weather = Weather("Gdansk")
Warsaw_weather = Weather("Warsaw")
Gdansk_weather.weather_in_city()
Warsaw_weather.weather_in_city()

print("In what city would you like to go?")

for city in list_of_cites:
    print(number, ".", city)
    number=number+1
Gdansk_weather.show_weather_in_city()
Warsaw_weather.show_weather_in_city()
number_of_city = input("Print a number of city")
number_of_city = int(number_of_city) - 1
list_of_objects_cites[number_of_city].show_shops_in_city()
shopping_list[shopping_list_number].append(list_of_objects_cites[number_of_city].return_city())
number_of_shop = input("Print a number of shop")
number_of_shop = int(number_of_shop) - 1
shopping_list[shopping_list_number].append(list_of_objects_shops[number_of_shop].return_shop())
list_of_objects_shops[number_of_shop].show_products_in_shop()
while True:
    product = input("Print name of product")
    shopping_list[shopping_list_number].append(product)
    end_list = input("If thats all print 1")
    if end_list == '1':
        break
shopping_list[shopping_list_number].append(get_datetime())
print(shopping_list)

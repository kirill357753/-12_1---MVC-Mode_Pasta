class Pasta:
    def __init__(self, name: str, ingredients: list, price: float, weight: float, additional_ingredients: list=None):
        self.__name = name  
        self.__ingredients = ingredients  
        self.__price = price  
        self.__weight = weight  
        self.__additional_ingredients = additional_ingredients if additional_ingredients is not None else []

    #Геттеры
    def get_name(self):
        return self.__name

    def get_ingredients(self):
        return self.__ingredients

    def get_get_price(self):
        return self.__price

    def get_weight(self):
        return self.__weight
    
    def get_additional_ingredients(self):
        return self.__additional_ingredients

    # Сеттеры
    def set_price(self, new_price):
        self.__price = new_price
        
    def weight(self, new_weight):
        self.__weight = new_weight
        
    def set_ingredient(self, new_ingredient: list):
        if type(new_ingredient) is list:
            self.__ingredients.clear()
            self.__ingredient.extend(new_ingredient)
        else:
            return "Ошибка не верный тип данных"

    def add_additional_ingredient(self, ingredient):
        if ingredient not in self.__additional_ingredients:
            self.__additional_ingredients.append(ingredient)

    def create_custom_pasta(self, custom_name, custom_ingredients, custom_price, custom_weight, custom_additional_ingredients):
        return Pasta(custom_name, custom_ingredients, custom_price, custom_weight, custom_additional_ingredients)

    

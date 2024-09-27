class PastaView:
    def __init__(self, controller):
        self.controller = controller

    def show_cafe_menu(self):
        print(self.controller.menu_cafe())
        
    def show_site_menu(self):
        print(self.controller.site_menu())
    
    def set_ingredients(self,user_right, new_ingredients):
        if type (new_ingredients) is not list:
            print("Неверный тип данных!")
        elif self.controller.set_price(user_right, new_price) == "banned":
            print("Нет права доступа")
        else:
            print(self.controller.set_ingredients(user_right, new_ingredients))
            
    def set_price(self,user_right, new_price):
        if new_price.isdigit() is False:
            print("Допустимы только циры!")
        elif self.controller.set_price(user_right, new_price) == "banned":
            print("Нет права доступа")
        else:
            print(self.controller.set_price(user_right, new_price))
    
    def set_weight(self,user_right, new_weight):
        if new_weight.isdigit() is False:
            print("Допустимы только циры!")
        elif self.controller.set_weight(user_right, new_weight) == "banned":
            print("Нет права доступа")
        else:
            print(self.controller.set_weight(user_right, new_weight))
            
    def set_picture(self,user_right, new_picture):
        if self.controller.set_picture(user_right, new_picture) == "banned":
            print("Нет права доступа")
        else:
            print(self.controller.set_picture(user_right, new_picture))
            
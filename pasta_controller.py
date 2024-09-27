class PastaController:
    def __init__(self, model):
        self.model = model

    def menu_cafe(self):
        pasta_data = (f"Паста :: {self.model.get_name()}\n"
                     f"Состав :: {self.model.get_ingredients()}\n"
                     f"Цена :: {self.model.get_price()}\n"
                     f"Вес :: {','.join(self.model.get_weight())}\n")
        return pasta_data
        
    def site_menu(self):
        pasta_data = (f"Паста :: {self.model.get_name()}\n"
                     f"Состав :: {','.join(self.model.get_ingredients())}\n"
                     f"Цена :: {self.model.get_price()}\n"
                     f"Вес :: {self.model.get_weight()}\n"
                     f"Фото :: {self.model.get_picture()}")
        return pasta_data
        
    def set_ingredients(self,user_right, new_ingredients):
        if user _right in  ["Admin", "IsStaff", "IsSuperuser"]:
            self.model.set_ingredients(new_ingredients)
            return "Новый рецепт!"
        else:
            return "banned"
            
    def set_price(self, user_right, new_price):
        if user _right in  ["Admin", "IsStaff", "IsSuperuser"]:
            price_int = int(new_price)
           self.model.set_price(new_price) 
           return "Цена изменена"
        else:
            return "banned"
        
    def set_weight(self,user_right, new_weight):
        if user _right in  ["Admin", "IsStaff", "IsSuperuser"]:
            self.model.set_weight(new_weight)
            return "Вес изменен"
        else:
            return "banned"
        
    def set_picture(self,user_right, new_picture):
        if user _right in  ["Admin", "IsStaff", "IsSuperuser"]:
            self.model.set_picture(new_picture)
            return "Картинка изменена"
        else:
            return "banned"
                     
        
        
        
        

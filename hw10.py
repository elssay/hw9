class Product:
    def __init__(self, title, calorific, cost):
        if Product.check_calorific(calorific) and Product.check_cost(cost) and Product.check_title(title):
            self.__title = title
            self.__calorific = calorific
            self.__cost = cost
        else:
           raise ValueError
    
    @staticmethod
    def check_title(title):
        if title:
            return True
        else:
            return False

    @staticmethod
    def check_calorific(calorific):
        return calorific > 0 
    @staticmethod
    def check_cost(cost):
        return cost > 0


    @property
    def title(self):
        return self.__title
    @property
    def calorific(self):
        return self.__calorific
    @property
    def cost(self):
        return self.__cost

    
class Ingredient(Product):
    def __init__(self, product, weight):
        if Ingredient.check_weight(weight):
            self.product = product
            self.__weight = weight
        else:
           raise ValueError
    
    @staticmethod
    def check_weight(weight):
        return weight > 0 
    
    @property
    def weight(self):
        return self.__weight
  
    def get_calorific(self):
        return self.weight / 100 * self.product.calorific
    def get_cost(self):
        return self.weight / 100 * self.product.cost

        
class Pizza(Product):
    def __init__(self, title, ingredient):
        self.ingredient = ingredient
        if self.check_title(title):
            self.__title = title    
        else:
            raise ValueError
        print('Пицца', self.__title,'-', self.get_calorific(), 'kkal,', self.get_cost(), 'руб' )
    def get_calorific(self):
        s=0
        for i in self.ingredient:
            s+= i.get_calorific()
        return s
    def get_cost(self):
        S=0
        for i in self.ingredient:
            S+= i.get_cost()
        return S


# Создаем продукты с указанием названия, калорийности продукта и его себестоимости
dough_product = Product('Тесто', 300, 20)
tomato_product = Product('Помидор', 50, 50)
cheese_product = Product('Сыр', 350, 120)

# Из продуктов создаем ингредиенты. Для каждого ингредиента указываем продукт, 
# из которого он состоит и вес продукта
dough_ingredient = Ingredient(dough_product, 100)
tomato_ingredient = Ingredient(tomato_product, 100)
cheese_ingredient = Ingredient(cheese_product, 100)

# Из ингредиентов создаем пиццу
pizza_margarita = Pizza('Маргарита', [dough_ingredient, tomato_ingredient, cheese_ingredient])
pizza_sheesy = Pizza('Сырная', [dough_ingredient, cheese_ingredient])
#выводим калорийность ингредиента:
print('Калорийность ингредиента :', tomato_ingredient.get_calorific())
#выводим себестоимость ингредиента:
print('Себестоимость ингредиента:', cheese_ingredient.get_cost())
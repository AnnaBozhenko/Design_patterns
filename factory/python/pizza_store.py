
class PizzaStore:
    def __init__(self, pizza_factory):
        self.pizza_factory = pizza_factory

    def set_pizza_factory(self, pizza_factory):
        self.pizza_factory = pizza_factory

    @classmethod
    def pack(cls):
        print("pizza is packed")

    @classmethod
    def cut(cls):
        print("pizza is cut")

    @classmethod
    def serve(cls):
        print("pizza is served")

    def order_pizza(self, pizza_type):
        pizza = self.pizza_factory.make_pizza(pizza_type)
        
        PizzaStore.pack()
        PizzaStore.cut()
        PizzaStore.serve()
        
        return pizza


class Pizza:
    def __init__(self, *args):
        self.cook()
    
    def cook(self): ...


class PepperoniPizza(Pizza):
    name = "Pepperoni pizza"

    def __init__(self, *args):
        super().__init__(args)

    def cook(self):
        print(f"{PepperoniPizza.name} is cooked")


class CheezePizza(Pizza):
    name = "Cheeze pizza"

    def __init__(self, *args):
        super().__init__(args)

    def cook(self):
        print(f"{CheezePizza.name} is cooked") 


class PizzaFactory:
    cooking_methods = {"pepperoni": PepperoniPizza,
                       "cheeze": CheezePizza}
    
    @classmethod
    def make_pizza(cls, pizza_type):
        cls.cooking_methods.get(pizza_type)()
        
        
# test
if __name__ == "__main__":
    uncle_dominico = PizzaFactory()
    franchescos_cafe = PizzaStore(uncle_dominico)
    order1 = franchescos_cafe.order_pizza("pepperoni")

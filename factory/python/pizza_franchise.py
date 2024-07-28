# Implement case when there are many stores of a franchise each featuring methods of cooking the same pizzas

from abc import ABC, abstractmethod 
from typing import List

RED_PEPPERS  = "Red Peppers"
ONIONS       = "Onions"
GARLIC       = "Garlic"
MUSHROOMS    = "Mushrooms"
BLACK_OLIVES = "Black Olives"
SPINACH      = "Spinach"
EGGPLANT     = "Eggplant"
OREGANO      = "Oregano"


class Dough:
    def __init__(self, name: str) -> None:
        self.name = name

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name


class Sauce:
    def __init__(self, name: str) -> None:
        self.name = name

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name


class Cheese:
    def __init__(self, name: str) -> None:
        self.name = name

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name


class Veggie:
    def __init__(self, name: str) -> None:
        self.name = name

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name


class Pepperoni:
    name = "Pepperoni"

    @classmethod
    def get_name(cls) -> str:
        return cls.name
    

class Clams:
    def __init__(self, name: str) -> None:
        self.name = name

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name


# Create ingredients' factory for each franchise Pizza store
class IngredientsFactory(ABC):
    @abstractmethod
    def dough(self) -> Dough: ...
    
    @abstractmethod
    def cheeses(self, *args) -> List[Cheese]: ...
    
    @abstractmethod
    def clams(self) -> Clams: ...
    
    @abstractmethod
    def veggies(self, *args) -> List[Veggie]: ...
    
    @abstractmethod
    def pepperoni(self) -> Pepperoni: ...
    
    @abstractmethod
    def sauce(self) -> Sauce: ...


class ChicagoIngredientsFactory(IngredientsFactory):
    def dough(self) -> Dough: 
        return Dough("Thick crust")
    
    def cheeses(self, args: List[str] | None = None) -> List[Cheese]:
        available_products = ["Mozzarella", "Parmesan"]
        if args:
            return [Cheese(name) for name in args if name in available_products]
        return [Cheese(product_name) for product_name in available_products]
    
    def clams(self) -> Clams: 
        return Clams("Clams")
    
    def veggies(self, args: List[str] | None = None) -> List[Veggie]: 
        available_products = [OREGANO, EGGPLANT, SPINACH, BLACK_OLIVES]
        if args:
            return [Veggie(name) for name in args if name in available_products]
        return [Veggie(product_name) for product_name in available_products]

    def pepperoni(self) -> Pepperoni: 
        return Pepperoni()

    def sauce(self) -> Sauce: 
        return Sauce("Plum tomato")


class NYCIngredientsFactory(IngredientsFactory):
    def dough(self) -> Dough: 
        return Dough("Thin crust")
    
    def cheeses(self, args: List[str] | None = None) -> List[Cheese]: 
        available_products = ["Reggiano"]
        if args:
            return [Cheese(name) for name in args if name in available_products]
        return [Cheese(product_name) for product_name in available_products]
    
    def clams(self) -> Clams: 
        return Clams("Fresh clams")
    
    def veggies(self, args: List[str] | None = None) -> List[Veggie]: 
        available_products = [GARLIC, MUSHROOMS, RED_PEPPERS, ONIONS]
        if args:
            return [Veggie(name) for name in args if name in available_products]
        return [Veggie(product_name) for product_name in available_products]

    def pepperoni(self) -> Pepperoni: 
        return Pepperoni()

    @classmethod    
    def sauce(cls) -> Sauce: 
        return Sauce("Marinara")
    

class Pizza(ABC):
    def __init__(self, ingredients_factory: IngredientsFactory) -> None:
        self.ingredients_factory = ingredients_factory

    def cook(self) -> None:
        self.prepare()
        self.bake()
        self.cut()
        self.box()

    @abstractmethod
    def prepare(self) -> None: ...

    def bake(self) -> None: 
        print("Baking for 20 minutes at 350...")

    def cut(self) -> None:
        print("Cutting on diagonal sectors...")

    def box(self) -> None:
        print("Packing pizza into a box...")

    @abstractmethod
    @classmethod
    def get_name(cls) -> str: ...
    

class CheesePizza(Pizza):
    def __init__(self, ingredients_factory: IngredientsFactory, veggies: List[str]) -> None:
        super().__init__(ingredients_factory)
        self.dough = self.ingredients_factory.dough()
        self.cheeses = self.ingredients_factory.cheeses()
        self.sauce = self.ingredients_factory.sauce()
        self.veggies = self.ingredients_factory.veggies(veggies) 
        
    def prepare(self) -> None:
        print(f"Tossing {self.dough.get_name()}...")
        print(f"Forming the base...")
        print(f"Smashing {self.sauce.get_name()}...")
        # dumb but honest way to use ingredients factory
        veggies = ', '.join([veggie.get_name() for veggie in self.veggies])
        # hytra sraka's way, so use of factory missed
        # veggies = ', '.join(veggies)
        print(f"Laying down {veggies}...")
        cheeses = ', '.join([cheese.get_name() for cheese in self.cheeses])
        print(f"Laying down {cheeses}...")

    def bake(self) -> None: 
        super().bake()

    def cut(self) -> None:
        super().cut()

    def box(self) -> None:
        super().box()
    

    @classmethod
    def get_name(cls) -> str:
        return "Cheese Pizza"


class VeggiePizza(Pizza):
    def __init__(self, ingredients_factory: IngredientsFactory, veggies: List[str]) -> None:
        super().__init__(ingredients_factory)
        self.dough = self.ingredients_factory.dough()
        self.sauce = self.ingredients_factory.sauce()
        self.veggies = self.ingredients_factory.veggies(veggies) 

    def prepare(self) -> None:
        print(f"Tossing {self.dough.get_name()}...")
        print(f"Forming the base...")
        print(f"Smashing {self.sauce.get_name()}...")
        veggies = ', '.join([veggie.get_name() for veggie in self.veggies])
        print(f"Laying down {veggies}...")

    def bake(self) -> None: 
        super().bake()

    def cut(self) -> None:
        super().cut()

    def box(self) -> None:
        super().box()

    @classmethod
    def get_name(cls) -> str:
        return "Veggie Pizza"


class ClamsPizza(Pizza):
    def __init__(self, ingredients_factory: IngredientsFactory) -> None:
        super().__init__(ingredients_factory)
        self.dough = self.ingredients_factory.dough()
        self.sauce = self.ingredients_factory.sauce()
        self.cheeses = self.ingredients_factory.cheeses()
        self.clams = self.ingredients_factory.clams() 

    def prepare(self) -> None:
        print(f"Tossing {self.dough.get_name()}...")
        print(f"Forming the base...")
        print(f"Smashing {self.sauce.get_name()}...")
        cheeses = ', '.join([cheese.get_name() for cheese in self.cheeses])
        print(f"Laying down {cheeses}...")
        print(f"Laying down {self.clams.get_name()}...")

    def bake(self) -> None: 
        super().bake()

    def cut(self) -> None:
        super().cut()

    def box(self) -> None:
        super().box()

    @classmethod
    def get_name(cls) -> str:
        return "Clams Pizza"


class PepperoniPizza(Pizza):
    def __init__(self, ingredients_factory: IngredientsFactory, veggies: List[str]) -> None:
        super().__init__(ingredients_factory)
        self.dough = self.ingredients_factory.dough()
        self.sauce = self.ingredients_factory.sauce()
        self.cheeses = self.ingredients_factory.cheeses()
        self.veggies = self.ingredients_factory.veggies(veggies)
        self.pepperoni = self.ingredients_factory.pepperoni() 

    def prepare(self) -> None:
        print(f"Tossing {self.dough.get_name()}...")
        print(f"Forming the base...")
        print(f"Smashing {self.sauce.get_name()}...")
        cheeses = ', '.join([cheese.get_name() for cheese in self.cheeses])
        print(f"Laying down {cheeses}...")
        veggies = ', '.join([veggie.get_name() for veggie in self.veggies])
        print(f"Laying down {veggies}...")
        print(f"Laying down {self.pepperoni.get_name()}...")

    def bake(self) -> None: 
        super().bake()

    def cut(self) -> None:
        super().cut()

    def box(self) -> None:
        super().box()

    @classmethod
    def get_name(cls) -> str:
        return "Pepperoni Pizza"


class PizzaStore(ABC):
    @classmethod
    @abstractmethod
    def order_pizza(cls, pizza_type: str) -> Pizza: ...

    @classmethod
    @abstractmethod
    def make_pizza(cls, pizza_type: str)-> Pizza: ...


class ChicagoPizzaStore(PizzaStore):
    @classmethod
    def order_pizza(cls, pizza_type: str) -> CheesePizza | VeggiePizza | PepperoniPizza | ClamsPizza:
        print("Greet client with a cup of coffee he wants")
        pizza = cls.make_pizza(pizza_type)
        return pizza
    
    @classmethod
    def make_pizza(cls, pizza_type: str) -> CheesePizza | VeggiePizza | PepperoniPizza | ClamsPizza:
        if pizza_type == "cheese":
            ingredients = ChicagoIngredientsFactory()
            pizza = CheesePizza(ingredients, veggies=[OREGANO])
        elif pizza_type == "veggie":
            ingredients = ChicagoIngredientsFactory()
            pizza = VeggiePizza(ingredients, veggies=[EGGPLANT, SPINACH, BLACK_OLIVES])
        elif pizza_type == "pepperoni":
            ingredients = ChicagoIngredientsFactory()           
            pizza = PepperoniPizza(ingredients, veggies=[EGGPLANT, SPINACH, BLACK_OLIVES])
        elif pizza_type == "clams":
            ingredients = ChicagoIngredientsFactory()
            pizza = ClamsPizza(ingredients)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza
    

class NYCPizzaStore(PizzaStore):
    @classmethod
    def order_pizza(cls, pizza_type:str) -> CheesePizza | VeggiePizza | PepperoniPizza | ClamsPizza:
        print("Greet client with a cup of freshly squeezed fruit juice he wants")
        pizza = cls.make_pizza(pizza_type)    
        return pizza
    
    @classmethod
    def make_pizza(cls, pizza_type: str) -> CheesePizza | VeggiePizza | PepperoniPizza | ClamsPizza:
        if pizza_type == "cheese":
            ingredients = NYCIngredientsFactory()
            pizza = CheesePizza(ingredients, veggies=[GARLIC])
        elif pizza_type == "veggie":
            ingredients = NYCIngredientsFactory()
            pizza = VeggiePizza(ingredients, veggies=[MUSHROOMS, ONIONS, RED_PEPPERS])
        elif pizza_type == "pepperoni":
            ingredients = NYCIngredientsFactory()           
            pizza = PepperoniPizza(ingredients, veggies=[MUSHROOMS, ONIONS, RED_PEPPERS])
        elif pizza_type == "clams":
            ingredients = NYCIngredientsFactory()
            pizza = ClamsPizza(ingredients)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza        


def run_pizza() -> None:
    chicago_order = {"Maryna": "cheese",
                     "Colombo": "veggie",
                     "Robert": "pepperoni",
                     "Fedyr": "clams"}
    
    chicago_pizzeria = ChicagoPizzaStore()
    print("Chicago's franchise")
    for client, pizza_type in chicago_order.items():
        pizza = chicago_pizzeria.order_pizza(pizza_type)
        print(f"{pizza.get_name()} for {client} is ready!")
        print()
    
    print("-"*30)
    print("New York City's franchise")
    print()

    nyc_order = {"Monican": "veggie",
                 "Ben": "cheese",
                 "Frank": "pepperoni",
                 "Susan": "clams"}
    nyc_pizzeria = NYCPizzaStore()
    for client, pizza_type in nyc_order.items():
        pizza = nyc_pizzeria.order_pizza(pizza_type)
        print(f"{pizza.get_name()} for {client} is ready!")
        print()
    

if __name__ == "__main__":
    run_pizza()
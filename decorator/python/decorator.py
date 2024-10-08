# Implement decorator pattern

from abc import ABC, abstractmethod

class Beverage(ABC):
    description = ""

    @classmethod
    def get_description(cls):
        return cls.description
    
    @classmethod
    @abstractmethod
    def cost(cls):
        pass

    
class DarkRoast(Beverage):
    description = "Dark Roast"
    
    @classmethod
    def get_description(cls):
        return super().get_description()
    
    @classmethod
    def cost(cls):
        return 0.99
    

class Espresso(Beverage):
    description = "Espresso"
    
    @classmethod
    def get_description(cls):
        return super().get_description()
    
    @classmethod
    def cost(cls):
        return 1.99
    

class HouseBlend(Beverage):
    def __init__(self):
        self.description = "House Blend"

    def get_description(self):
        return super().get_description()

    def cost(self):
        return 0.99
    

class Decaf(Beverage):
    def __init__(self):
        self.description = "Decaf"

    def get_description(self):
        return super().get_description()

    def cost(self):
        return 1.05


class CondimentDecorator(Beverage):
    description = ""

    def __init__(self, beverage):
        super().__init__()
        self.base_beverage = beverage

    def get_description(self):
        pass

    def cost(self):
        pass


class SteamedMilk(CondimentDecorator):
    description = "Steamed milk"

    def __init__(self, base_beverage):
        super().__init__(base_beverage)

    def get_description(self):
        return f"{self.base_beverage.get_description()}, {SteamedMilk.description}"
    
    def cost(self):
        return self.base_beverage.cost() + 0.10
    

class Soy(CondimentDecorator):
    description = "Soy"

    def __init__(self, base_beverage):
        super().__init__(base_beverage)

    def get_description(self):
        return f"{self.base_beverage.get_description()}, {Soy.description}"
    
    def cost(self):
        return self.base_beverage.cost() + 0.15
    

class Whip(CondimentDecorator):
    description = "Whip"
    def __init__(self, base_beverage):
        super().__init__(base_beverage)

    def get_description(self):
        return f"{self.base_beverage.get_description()}, {Whip.description}"
    
    def cost(self):
        return self.base_beverage.cost() + 0.10


class Mocha(CondimentDecorator):
    description = "Mocha"

    def __init__(self, base_beverage):
        super().__init__(base_beverage)

    def get_description(self):
        return f"{self.base_beverage.get_description()}, {Mocha.description}"
    
    def cost(self):
        return self.base_beverage.cost() + 0.20
    

"""Disadvantages
    - DRY-principle broken in 

"""
    

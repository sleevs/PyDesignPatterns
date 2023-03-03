from __future__ import annotations
from abc import ABC, abstractmethod



class Creator(ABC):
    
    @abstractmethod
    def factoryMethod(self):
        pass
    
    
    def operation(self) -> str :
        
        product = self.factoryMethod()
        result = f"Creator:  {product.action()}"
        return result
    
    


class CreatorTruck(Creator):
    
    
    def factoryMethod(self) -> Product :
        return ProductTruck()
    


class CreatorCar(Creator):
    
    
    def factoryMethod(self) -> Product :
        return ProductCar()




class CreatorMotorcycle(Creator):
    
    
    def factoryMethod(self):
        return ProductMotorcycle()



class CreatorBike(Creator):
    
    def factoryMethod(self):
        return ProductBike()



class Product (ABC):
    
    @abstractmethod
    def action(self) -> str :
        pass

    

    

class ProductTruck(Product):
    
    def action(self) -> str:
        return "DELIVERY WITH TRUCK"





class ProductCar(Product):

    def action(self) -> str:
        return "DELIVERY WITH CAR"


    

class ProductMotorcycle(Product):
    
    def action(self) -> str:
        return "DELIVERY WITH MOTORCYCLE "
    
    


class ProductBike(Product):
    
    def action(self) -> str:
        return "DELIVERY WITH BIKE"   
    

 

def clientCode(creator: Creator)->  None:
    
    print(creator.operation()) 
    
    

if __name__ == "__main__":
    
  
    clientCode(CreatorTruck())
    print("\n")
    clientCode(CreatorCar())
    print("\n")
    clientCode(CreatorMotorcycle())
    print("\n")
    clientCode(CreatorBike())
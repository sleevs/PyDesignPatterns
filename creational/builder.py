from __future__ import annotations
from flask import Flask
from abc import ABC, abstractmethod
from typing import Any



class ProductNotification():
    
    
    def __init__(self)-> None:
        self.itens =[]

    def add(self ,  item: Any)-> None:
        self.itens.append(item)

    def listItens (self)-> None:
        print(self.itens)



     
class Builder(ABC):
    
    
    @property
    @abstractmethod
    def notification(self) -> None:
        pass

    @abstractmethod
    def alert(self) -> None:
        pass
    
    @abstractmethod
    def message(self) -> None:
        pass
    
    @abstractmethod
    def dialog(self) -> None:
        pass
        
    
            
class ConcreteBuilder(Builder):
    
    
    def __init__(self) -> None:
        self.reset()
    
        
    def reset(self) -> None:
        self._productNotification = ProductNotification()    
    
    
    @property    
    def notification(self) -> ProductNotification:
        productNotification = self._productNotification
        self.reset()
        return productNotification     
        
        
        
    def alert(self)-> None:
        self._productNotification.add("ALERT")
        
        
    def message(self)-> None:
        self._productNotification.add("MESSAGE")
    
    
    def dialog(self)-> None:
        self._productNotification.add("DIALOG")    
    
    

class Director:
    
    def __init__(self) -> None:
        self._builder =None
        
     
    @property
    def builder(self) ->Builder:
        return self._builder 
        
    
    @builder.setter
    def builder(self , builder:Builder) -> None:
        self._builder = builder    
    
    
    def buildBasicProduct(self) -> None:
        self.builder.alert()
        
        
     
    def buildFullProduct(self) -> None:
        self.builder.alert()
        self.builder.message()
        self.builder.dialog()
        
         
    
    
    
    

if __name__ == "__main__":

    print("\n")
    print("MUNIZ SOARES ENGENHARIA DE SOFTWARE")
    print("BUILDER DESIGN PATTERN")
    print("\n")
    
    director = Director()
    builder = ConcreteBuilder()
    director.builder = builder
    
    
    print("BASIC NOTIFICATION")
    director.buildBasicProduct()
    builder.notification.listItens()
    print("\n")
    
    print("FULL NOTIFICATION")
    director.buildFullProduct()
    builder.notification.listItens()
    print("\n")
    
    #
    #the builder pattern can be useed without a director calss
    #
    
    print("CUSTOM NOTIFICATION")
    builder.dialog()
    builder.message()
    builder.notification.listItens()
    
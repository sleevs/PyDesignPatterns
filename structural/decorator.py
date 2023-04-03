from __future__ import annotations
from abc import ABC, abstractmethod


class Component :
    
    
    @abstractmethod
    def operation(self) -> str:
        pass




class ConcreteComponent(Component):
    
    def operation(self) -> str:
        return "ConcreteComponent"
    
    
    
    
    
    
class Decorator(Component):
    
    
    component_ : Component = None
    
    
    def __init__(self , component : Component) -> None:
            self.component_ = component
            
            
            
    
    def operation(self) -> str:
        
        print("DECORATOR --")
        return self.component_.operation()





class ConcreteDecorator(Decorator):
    
    
    
    component_ : Component = None
    
    
    def __init__(self, component: Component) -> None:
        super().__init__(component)
        self.component_ = component
        
        
        
    def operation(self) -> str:
        
        print("ConcreteDecorator")
        return self.component_.operation()
    
    
    
    
if __name__ == "__main__":
    
    
    print("JSNSOFTWARE - TEST DECORATOR PATTERN \ns")
    
    
    
    comp1 =  ConcreteComponent()
    
    print(comp1.operation())
    
    
    decor1 = Decorator(comp1)
    decor2 = ConcreteDecorator(decor1)
    
    print(decor2.operation())
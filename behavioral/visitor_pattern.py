
from __future__ import annotations
from typing import List
from abc import ABC , abstractmethod





class Visitor (ABC):
    
    
    @abstractmethod
    def visitorConcreteElementA(self , element : ConcreteElementA) -> None:
        pass
    
    @abstractmethod
    def visitorConcreteElementB(self , element : ConcreteElementB) -> None:
        pass
    

class Element(ABC):
    
    
    @abstractmethod
    def accept( self , visitor : Visitor)-> None:
        pass 
    
    
    
class ConcreteElementA(Element):
    
    
    def accept(self, visitor: Visitor) -> None:
        visitor.visitorConcreteElementA(self)
        
    
    def exclusiveMethodOfConcreteElementA(self) -> str:
        return "A" 
    
    


class ConcreteElementB(Element):
    
    
    def accept(self, visitor: Visitor) -> None:
        visitor.visitorConcreteElementB(self)
        
    
    def specialMethodOfConcreteElementB(self) -> str:
        return "B" 
    
    
    
    
class ConcreteVisitorA(Visitor):
    
    def visitorConcreteElementA(self, element: ConcreteElementA) -> None:
        print(f"{element.exclusiveMethodOfConcreteElementA()} + ConcreteVisitorA")
        
    
    def visitorConcreteElementB(self, element: ConcreteElementB) -> None:
        print(f"{element.specialMethodOfConcreteElementB} + ConcreteVisitorA")
        
        


    
class ConcreteVisitorB(Visitor):
    
    def visitorConcreteElementA(self, element: ConcreteElementA) -> None:
        print(f"{element.exclusiveMethodOfConcreteElementA()} + ConcreteVisitorB")
        
    
    def visitorConcreteElementB(self, element: ConcreteElementB) -> None:
        print(f"{element.specialMethodOfConcreteElementB} + ConcreteVisitorB")
        
        
        
        

def cliendCode(elements : List[Element], visitor : Visitor) -> None:
    
        for element in elements:
            element.accept(visitor)
            
            


if __name__ == "__main__":
    
    elements = [ConcreteElementA() , ConcreteElementB()]
    
    va = ConcreteVisitorA()
    cliendCode(elements,va)
    
    print("\n")
    
    vb = ConcreteVisitorB()
    cliendCode(elements, vb)
    
    

from __future__ import  annotations 

from abc import ABC , abstractmethod

from typing import List





class Component (ABC):
    
    def getParent(self) -> Component:
        return self._parent
    
    
    
    def setParent(self , parent : Component) :
        self._parent = parent
    
    

    @abstractmethod
    def operation(self) -> str :
        pass
    
    
    
    def add(self , component : Component) -> None:
        pass
    
    
    
    def remove(self , component : Component) -> None:
        pass
    
    
    def isComposite(self) -> bool:
        return False 
    
    
    
    

class Leaf(Component):
    
    def operation(self) -> str:
        return " LEAF - OPERATION() "
    
    
    

class Composite (Component):
    
    def __init__(self) -> None:
        
        self._children : List[Component] = []
        
    
    def operation(self) -> str:
        
        result = []
        
        for child in self._children:
            result.append(child.operation())
        return f"BRAANCH ({''.join(result)})"
    
    
    
    
    def add(self , component : Component) -> None:
            self._children.append(component)
            component.parent = self
    
    
    
    def remove(self , component : Component) -> None:
            self._children.remove(component)
            component.parent = None
    
    
    def isComposite(self) -> bool:
        return True 
        
    
    
        
    
    
if __name__ == "__main__":
    
    print("APP COMPOSITE STRUCTURAL PATTERN")
    
    
    simple = Leaf()
    print(simple.operation())
    
    
    tree = Composite()
    
    tree.add(simple)
    
    print(tree.operation())
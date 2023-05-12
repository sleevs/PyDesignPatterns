from __future__ import annotations 
from collections.abc import Iterable , Iterator
from typing import Any , List



class ConcreteIterator(Iterator):
    
        position: int = None
        reverse: bool = False
        
        def __init__ (self , collection: ConcreteCollection , reverse:bool = False) ->None:
            self.collection =collection
            self.reverse = reverse
            self.position = -1 if reverse else 0
            
        
        def __next__(self):
        
            try:
                value = self.collection[self.position]
                self.position += -1 if self.reverse else 1
                
            except IndexError:
                
                raise StopIteration()
            
            return value 
            
    
    
    
class ConcreteCollection(Iterable):
    
    
    def __init__ (self, collection: List[Any] = []) -> None:
        self.collection = collection 
        
    
    def __iter__(self) -> ConcreteIterator:
        
        return ConcreteIterator(self.collection)
    
    
    def gerReverseIterator(self) -> ConcreteIterator:
        return ConcreteIterator(self.collection , True)
    
    
    def addItem (self, item: Any):
        self.collection.append(item)
    
    
    
    
    
    
if __name__ == '__main__':
    


    collection = ConcreteCollection()
    
    collection.addItem("BRASIL - BRASILIA")
    collection.addItem("CHILE - SAN TIAGO")
    collection.addItem("BOLIVIA - LA PAZ - SUCRE")
    collection.addItem("PERU - LIMA")
    collection.addItem("URUGUAI - MONTEVIDEO")
    collection.addItem("ARGENTINA - BUENOS AIRES")
    collection.addItem("VENEZUELA - CARACAS")
    collection.addItem("SURINAME - PARAMARIBO")
    collection.addItem("COLOMBIA - BOGOTÁ")
    collection.addItem("GUYANA - GEORGETOWN")
    collection.addItem("ECUADOR - QUITO")
    collection.addItem("PARAGUAI - ASSUNÇÃO")
    collection.addItem("ARUNA - ORANJESTAD")
    collection.addItem("GUIANA FRANCESA - CAIENA")
    collection.addItem("TRINIDADE E TOBAGO - PORTO ESPANHA")
    collection.addItem("CURAÇAU - WILLEMSTAD")
    
    print("\n".join(collection))



from __future__ import annotations
from abc import ABC , abstractmethod
from typing import List





class Strategy(ABC):
    
    
    @abstractmethod
    def doAlgorithm(self , data: List):
        pass
    



class Context():
    
    def __init__(self , strategy : Strategy)-> None: 

        self._strategy = strategy
        
    
    @property
    def strategy(self) -> Strategy:
    
        return self._strategy
    
    
    @strategy.setter
    def strategy(self , strategy: Strategy) -> None:
        
        self._strategy = strategy
        
    
    def doSomeBusinessLogic(self) -> None:
        
        print(" CONTEXT : SORTING DATA USING STRATEGY")
        
        resultado = self.strategy.doAlgorithm(["BRASIL","ARGENTINA","VENEZUELA" , "URUGAUAI","PARAGUAI","CHILE", "COLOMBIA", "BOLIVIA", "PERU","EQUADOR","GUIANA FRANCESA","SURINAME","GUIANA" ])
        print(" - ".join(resultado))
        
        
        


class ConcreteStrategyA(Strategy):
    
    
    def doAlgorithm(self, data: List):
        return sorted(data)
    


class ConcreteStrategyB(Strategy):
    
    def doAlgorithm(self, data: List):
        return reversed(sorted(data))
    
    
if __name__ == "__main__":
    
    
    
    print("CLIENTE : STRATEGY IS SET TO NORMAL SORTING \n")
    context = Context(ConcreteStrategyA())
    context.doSomeBusinessLogic()
    print("\n")
    
    
    print("CLIENTE : STRATEGY IS SET TO REVERSED SORTING \n")
    context = Context(ConcreteStrategyB())
    context.doSomeBusinessLogic()
    print("\n")
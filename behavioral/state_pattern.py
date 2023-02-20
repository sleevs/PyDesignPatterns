
from __future__ import annotations
from abc import ABC , abstractmethod


class Context:
    
    
    _state = None
    
    def __init__ (self, state: State) -> None:
        self.transmitionTo(state)
        
    
    def transmitionTo(self, state : State):
        print("\n")
        print(f"Context: Transmition to {type(state).__name__} \n")
        self._state = state
        self._state.context = self
        
        
    def request(self):
        self._state.handle()
        
        



class State(ABC):

    @property    
    def context(self) -> Context:
        return self._context
        
    
    @context.setter
    def context(self , context: Context) -> None:
        self._context = context
        
    
    @abstractmethod
    def handle(self) -> None:
        pass
    
    
    
    
class ConcreteStateProcessando(State):
    
    def handle(self) -> None:
        print("State Processando Handler Request")
        print("ConcreteStateProcessando  WANT TO CHANGE THE STATE OF THE CONTEXT \n")
        self.context.transmitionTo(ConcreteStateConcluido())
    
    

    
class ConcreteStateConcluido(State):
    
    def handle(self) -> None:
        print("State Concluido Handler Request")
        print("ConcreteStateConcluido  WANT TO CHANGE THE STATE OF THE CONTEXT \n")
        self.context.transmitionTo(ConcreteStateProcessando())
    
    
    

if __name__ == "__main__":
    
    context = Context(ConcreteStateProcessando())
    context.request()
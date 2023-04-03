from __future__ import  annotations 

from abc import ABC , abstractmethod


class ImplementationIF(ABC):


    @abstractmethod
    def operationImplementation(self) -> str :
        pass    
    
    

class ConcreteImplementationA(ImplementationIF):
    

    def operationImplementation(self) -> str:
        return " ConcreteImplementationA  operationImplementation"





class ConcreteImplementationB(ImplementationIF):
    

    def operationImplementation(self) -> str:
        return " ConcreteImplementationB  operationImplementation"








class Abstraction:
    
    def __init__ (self , implementationIF :  ImplementationIF) -> None :
        self.implementationIF = implementationIF
        
        
    def operation(self) -> str:
        
        return f"ABSTRACTION BASE OPERATION {self.implementationIF.operationImplementation()}"
    
    
    
    
    
class RefinedAbstraction(Abstraction):
    
    def operation(self) -> str:
        return f"RefinedAbstraction {self.implementationIF.operationImplementation()}"
        
        
        
if __name__ == "__main__":
    
    print("TESTE APP BRIDGE \n")
    
    
    impl =  ConcreteImplementationA()
    abs = Abstraction(impl)
    print(abs.operation())
    print("\n")
    
    impl =  ConcreteImplementationB()
    abs = RefinedAbstraction(impl)
    print(abs.operation())
    
    
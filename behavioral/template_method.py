from abc import ABC , abstractmethod



class AbstracClass(ABC):
    
   # 
   #TEMPLATE METHOD DEFINES THE SKELETON OF AN ALGORITHM
   #  
    def templateMethod(self)-> None:
        
        self.baseOperation()
        self.primitiveOperation1()
        self.baseOperation2()
        self.primitiveOperation2()
        self.hook()
        self.baseOperation3()
        
            

    def baseOperation(self) -> None:
        print(" abstract class :  BASE OPERATION 1 \n")  
        
    def baseOperation2(self) -> None:
        print(" abstract class :  BASE OPERATION 2 \n")
        
    def baseOperation3(self) -> None:
        print(" abstract class :  BASE OPERATION 3 \n")          
            
    #these operations have to be implemented in subclass
    @abstractmethod
    def primitiveOperation1(self) -> None:
        pass
    
    @abstractmethod
    def primitiveOperation2(self) -> None:
        pass


        
    def hook(self) -> None:
            pass
        
        
        
        
class ConcreteClass(AbstracClass):
    
    def primitiveOperation1(self) -> None:
         print(" CONCRETE CLASS : IMPLEMENTS PRIMITIVE OPERATION 1 \n")
    

    def primitiveOperation2(self) -> None:
         print(" CONCRETE CLASS : IMPLEMENTS PRIMITIVE OPERATION 2 \n")
    


def clientCode(abstraClass : AbstracClass) -> None:
    
    abstraClass.templateMethod()
    
    
if __name__ == "__main__":
    clientCode(ConcreteClass())
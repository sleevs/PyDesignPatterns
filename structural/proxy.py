from __future__ import annotations
from abc import ABC  , abstractmethod




class Subject(ABC):
    
    @abstractmethod
    def request(self) -> None :
        pass

    

class RealSubject(Subject):
    
    
    def request(self) -> None:
        
        print(" REALSUBJECT : HANDLER REQUEST")
       


class Proxy(Subject):
    
    
    def __ini__(self , realSubject: RealSubject) -> None:
        self._realSubject = realSubject 
        
     
        
    def request(self) -> None:
        print(realSubject.request())
        
        


if __name__ == "__main__":
    
    realSubject = RealSubject()
    
    proxy = Proxy(realSubject)
    
    print(proxy.request())
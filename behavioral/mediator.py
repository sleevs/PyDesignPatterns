from __future__ import annotations
from abc import ABC





class Mediator(ABC):
    
    
    def notify(self , sender:object , event:str) -> None:
        pass
    
    
    
        
    

class ConcreteMediator(Mediator):
    
    def __init__(self, colleague1: ConcreteColleague1 , colleague2: ConcreteColleague2) -> None:
        self._colleague1 = colleague1
        self._colleague1.mediator = self
        self._colleague2 = colleague2
        self._colleague2.mediator = self
        
    
    def notify(self , sender:object , event: str) -> None:
        
        if event == "A":
            
            self._colleague2.executeC()
        elif event == "C":
            
            self._colleague1.executeA
            self._colleague2.executeD


class Colleague:
    
    
    def __init__(self , mediator: Mediator =None) -> None:
        
        self._mediator = mediator
        
    @property
    def mediator(self) -> Mediator:
        return self._mediator
    
    @mediator.setter
    def mediator(self , mediator: Mediator) -> None:
        self._mediator = mediator
        
        
        
        

class ConcreteColleague1(Colleague):
    
    def executeA(self) -> None:
        print("EXECUTE A")
        self.mediator.notify(self,"A")
        
    def executeB(self) -> None:
        print("EXECUTE B")
        self.mediator.notify(self,"B")    
        
        


class ConcreteColleague2(Colleague):
    
    def executeC(self) -> None:
        print("EXECUTE C")
        self.mediator.notify(self,"C")
        
    def executeD(self) -> None:
        print("EXECUTE D")
        self.mediator.notify(self,"D")    
    
    

if __name__ == '__main__':
    
    print("MUNIZ SOARES ENGENHARIA DE SOFTWARE")
    
    
    mediatorTest1 = ConcreteColleague1()
    mediatorTest2 = ConcreteColleague2()
    
    mediator = ConcreteMediator(mediatorTest1 ,mediatorTest2)
    
    mediatorTest1.executeA()
    
    mediatorTest2.executeD()
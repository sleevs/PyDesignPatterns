from __future__ import annotations
from abc import ABC , abstractmethod


class Command(ABC):
    
    
    @abstractmethod
    def execute(self) -> None:
        pass
    

        
class ConcreteCommand(Command):
    
    
    def __init__ (self, receiver: Receiver , payload: str)-> None:
        self.payload = payload
        self.receiver = receiver
        
        
    def execute(self) -> None:
        self.receiver.action()
        print(f"CONCRETE COMMAND EXECUTING : {self.payload}")
        


class Receiver:
    
    def action(self)-> None:
        print("RECEIVER EXECUTING ACTION")
        


class Invoker:
    
    
    def __init__(self, command: Command) ->None:
        self.command = command
        
        
        
    def invoker(self) ->None:
        self.command.execute()
        
        
        

if __name__ == '__main__':
    
    
    receiver = Receiver()
    command = ConcreteCommand(receiver ,"SOME OPERATION")
    invoker = Invoker(command)
    
    invoker.invoker()
    
        
        


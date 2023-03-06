from __future__ import annotations
from abc import ABCMeta, abstractmethod
import copy


'''

SECURITY ANALISYS

give : some context , setup data such hardware data
when : some action is carried out or event that initiates the scenario
then : defines the result or outcome of particular set of 
        observable consequences shold obtain
        
#broken access crontol
#cryptographic failures
#injection
#insecure design
#security misconfiguration
#vulnerable and outdated components 
#indentification and authentication failures
#software and data integrity failure  
#security loggin and monitoring failures
#server-side request forgery


'''



class Prototype(metaclass =ABCMeta):
    
    def __init__ (self):
        self.id = None
        self.name = None
        self.type = None
        self.description = None
        
    @abstractmethod
    def action(self):
        pass
    
    
    def getId(self):
        return self.id
    
    
    def getName(self):
        return self.name
    
    
    def getType(self):
        return self.type
    
    
    def getDescription(self):
        return self.description
    
    
    def clone(self):
        return copy.copy(self)
    
    
     
    def setId(self , sid):
       self.id = sid
       
    def setName(self , sname):
        self.name = sname
        
    def setType(self, stype):
        self.type = stype
        
    def setDescription(self, sdescription):
        self.description = sdescription
    
    
    
    
class TesteA(Prototype):
        
        def __init__(self):
            super().__init__()
            self.type = "PROTOTYPE TESTE A"
            
            
        def action(self):
            print("TESTE A")
            
            

    
class TesteB(Prototype):
        
        def __init__(self):
            super().__init__()
            self.type = "PROTOTYPE TESTE B"
            
            
        def action(self):
            print("TESTE B")
            
            

class PrototypeCache:
    
    cache = {}
    
    @staticmethod
    def getAction(sid):
        TESTE = PrototypeCache.cache.get(sid , None)
        return TESTE.clone()
            
   
    @staticmethod
    def load():
        testeA = TesteA()
        testeA.setId("1")
        PrototypeCache.cache[testeA.getId()] = testeA
        
        
        testeB = TesteB()
        testeB.setId("13")
        PrototypeCache.cache[testeB.getId()] = testeB
        
        
        

if __name__ == "__main__":
    
    print("JSN SOFTWARE") 
    
    PrototypeCache.load()
    
    prototype1 = PrototypeCache.getAction("13")   
    print(prototype1.getType())
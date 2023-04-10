from __future__ import annotations
from abc import ABC , abstractmethod
from typing import Dict
import json 




class Flyweight:
    
    
    
    def __init__(self , sharedState : str) -> None:
        self._sharedState =  sharedState
    
    
    
    def operation(self , uniqueState : str) -> None:
        
        shared = json.dumps(self._sharedState)
        unique = json.dumps(uniqueState)
        print(f" SHARED ({shared}) UNIQUE ({unique})")
        
        
    

class FlyewinghtFactory:


    flyweightMap : Dict[str , Flyweight] = {}
    
    def __init__(self , initFlyweightMap : Dict ) -> None:
        
        for status in initFlyweightMap:
            self.flyweightMap[self.getKey(status)] = Flyweight(status)
            
    
    def getKey(self , status: Dict) -> None:
        return "".join(sorted(status))
    
    
    def getFlyweight(self , sharedStatus) -> Flyweight:
        
        key = self.getKey(sharedStatus)
        
        if not self.flyweightMap(key):

            print("FLYWEIGHT FACTORY - CREATE NEW ONE")
            self.flyweightMap[key] = Flyweight(sharedStatus)
        else:
            print(" FLYWEIGHT FACTORY REUSING EXISTING FLYWEIGHT")
        
        return self.flyweightMap[key]
            
            
        
    def listFlyweights(self) -> None:
        count = len (self.flyweightMap)
        print(f"QUANTITY {(count)} FLYWEIGHTS \n")
        print("\n".join(map(str, self.flyweightMap.keys())), end="")
    
"""
    def add(
        factory: FlyewinghtFactory ,id:str )-> None:
    
         fly = factory.getFlyweight(id )
         fly.operation(id)
"""         
            
            

if __name__ == "__main__":
    
    print("DESIGN PATTERN FLYWEIGHT")
    
    
    factory = FlyewinghtFactory([
        ["13"],
        ["22"],
        ["51"],
        ["11"],
    ])
    
    factory.listFlyweights()
    
   
    
    

    
    
    
    
    
    
    
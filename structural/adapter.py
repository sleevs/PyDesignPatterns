
class Target:
    
    
    
    def request(self) -> str:
        return "TARGET BEHAVIOR"
    
    
    
class Adaptee :
    
    
    def specific_request(self) -> str:
        
        return "ADAPTEE BEHAVIOR"
    
    
class Adapter(Target , Adaptee ):
    
    
    def request(self) -> str:
        
        return f"ADAPTER REQUEST OPERATION : {self.specific_request()}"
    
    
    
if __name__ == "__main__":
    
    target = Target()
    
    print(target.request())
    
    adapter = Adapter()
    
    print(adapter.request())
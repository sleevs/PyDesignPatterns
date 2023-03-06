import plotly as py


class SingletonMeta(type):
    
    _instances = {}
    
    def __call__(cls, *args, **kwags):
        
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwags)
            cls._instances[cls] = instance
        return cls._instances[cls]
    



class Singleton(metaclass=SingletonMeta):
    
    
    def businessLogic(self):
        print("OPERATION BUSINESS LOGIC \n")
    

    
if __name__ == "__main__":
    
    print("JSNSOFTWARE \n")
    
    s1 = Singleton()
    s2 = Singleton()
    
    print(id(s1))
    s1.businessLogic()
    
    print(id(s2))
    s2.businessLogic()
    
    if id(s1) == id(s2):
        print("BOTH CONTAIN THE SAME INSTANCE")
    else:
        print("BOTH CONTAIN DIFFERENT INSTANCE")
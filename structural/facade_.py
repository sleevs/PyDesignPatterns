from __future__ import annotations
from flask import Flask , request

import requests


app = Flask (__name__)




class Facade:

    def __init__(self , subsystem1: Subsystem1 , subsystem2 : Subsystem2) -> None:
        

        self.subsystem1 = subsystem1 or subsystem1()
        self.subsystem2 = subsystem2 or subsystem2()


    def operation(self) -> str :

        result = []
        result.append('FACADE INITIALIZES SUBSYSTEMS :')
        result.append(self.subsystem1.operation_1())
        result.append(self.subsystem2.operation_1())
        
        result.append('FACADE ORDER SUBSYSTEMS TO PERFORM THE ACTION :')
        result.append(self.subsystem1.operation_y())
        result.append(self.subsystem2.operation_x())

        return '\n'.join(result)




class Subsystem1:

    def operation_1(self) -> str :
        return 'SUBSYSTEM1: READY'
    
    def operation_y(self) -> str :
        return 'SUBSYSTEM1: GO! '
    


class Subsystem2:

    def operation_1(self) -> str :
        return 'SUBSYSTEM2: GET READY'
    
    def operation_x(self) -> str :
        return 'SUBSYSTEM2: FIRE! '


def clientCode (facade: Facade) -> None :

    print(facade.operation() , end='')




@app.route('/teste')
def teste():
        
    sub1 = Subsystem1()
    sub2 = Subsystem2()
    facade = Facade(sub1 , sub2)
    return "TESTE FACADE PATTERN \n"   + facade.operation()


@app.route('/teste2')
def getModels():
    
    #requests.get("http://127.0.0.1:3001/models")
   # parsed = requests.json()
   # print(parsed)
    return  requests.get("http://127.0.0.1:3001/models").content
      
      
  
        
if __name__ == '__main__' :

    app.run(debug=True)


sub1 = Subsystem1()
sub2 = Subsystem2()
facade = Facade(sub1 , sub2)
clientCode(facade)

   
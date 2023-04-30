from __future__ import annotations
from abc import ABC  , abstractmethod
from flask import Flask
import requests
from rabbitmq_pika_flask import RabbitMQ

# init app
#app = Flask(__name__)

# send message
#@app.route('/teste', methods=['GET'])
#def process():
#    return "MUNIZ SOARES ENGENHARIA DE SOFTWARE"


class Handler(ABC):
    
    @abstractmethod
    def handle(self , request)-> Optional[str]:
        pass
    
    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass
    


class AbstractHandler(Handler):
    
    _next: Handler = None
        
    def set_next(self , handler: Handler) -> Handler:
        self._next = handler
        return handler
    
        
    @abstractmethod
    def handle(self , request : Any)-> str:
        
        if self._next:
            return self._next.handle(request)
        return None

class CardPayment(AbstractHandler):
    
    
    def handle(self , request: Any)-> str:
        if request == "CREDITCARD":
            return f"CARD PAYMENT :{request}"
        else:
            return super().handle(request)
    
    
    
class TransferPayment(AbstractHandler):
    
    
    def handle(self , request: Any)-> str:
        if request == "TRANSFER":
            return f"TRANSFER PAYMENT :{request}"
        else:
            return super().handle(request)
    


class CashPayment(AbstractHandler):
    
    
    def handle(self , request: Any)-> str:
        if request == "CASH":
            return f"CASH PAYMENT :{request}"
        else:
            return super().handle(request)
       


class DigitalPayment(AbstractHandler):
    
    
    def handle(self , request: Any)-> str:
        if request == "DIGITAL":
            return f"DIGITAL PAYMENT :{request}"
        else:
            return super().handle(request)
       


    
if __name__ == '__main__':

    print("MUNIZ SOARES ENGENHARIA DE SOFTWARE \n") 
    
    transfer = TransferPayment()
    digital = DigitalPayment()
    cash =  CashPayment()
    card = CardPayment()
    
    
    list ={"TRANSFER","CASH","CARD","DIGITAL"}
    
    for transaction in list:
        
        result = cash.handle(transaction)
        result = transfer.handle(transaction)
        result = digital.handle(transaction)
        result = card.handle(transaction)
        
        if result:
         print(result)   
        else:    
         print(transaction)   
        


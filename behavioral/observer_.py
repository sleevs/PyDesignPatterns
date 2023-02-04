from __future__ import annotations
from abc import ABC , abstractclassmethod
from random2  import randrange
from typing import List


class Subject(ABC):

    @abstractclassmethod  
    def attach(self , observer : Observer)-> None :

        pass

    @abstractclassmethod  
    def detach(self , observer : Observer)-> None :

        pass


    @abstractclassmethod  
    def notify(self)-> None :

        pass


class Observer(ABC):

    @abstractclassmethod  
    def update(self , subject : Subject)-> None :

        pass


class ConcreteSubject(Subject):

    _status: int = None

    _observers : List[Observer] =[]

 
    def attach(self , observer : Observer)-> None :
        print("SUBJECT ATTACHED AN OBSERVER")

        self._observers.append(observer)

  
    def detach(self , observer : Observer)-> None :

        self._observers.remove(observer)


    def notify(self)-> None :

         print("SUBJECT NOTIFY OBSERVER") 
         for observer in self._observers:
             observer.update(self)

    def bussinesLogic(self) -> None :

        print("SUBJECT : DOING SOMETHING IMPORTANT")
        self._status = randrange(0 , 10)

        print("SUBJECT : MY STATUS HAS CHANGED TO :{self._status}")
        self.notify()



class ConcreteObserverA(Observer):

    def update(self , subject :Subject) -> None :
        if subject._status < 3 :
            print("OBSERVER A : REACTED TO EVENT" )




class ConcreteObserverB(Observer):

    def update(self , subject :Subject) -> None :
        if subject._status == 0 or subject._status >= 2 :
            print("OBSERVER B : REACTED TO EVENT" )



if __name__ == "__main__" :

  subject = ConcreteSubject()

  observer_a = ConcreteObserverA()
  subject.attach(observer_a)

  observer_b = ConcreteObserverB()
  subject.attach(observer_b)

  subject.bussinesLogic()

  subject.detach(observer_a)

  subject.bussinesLogic()
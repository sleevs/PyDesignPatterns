
class Memento:
    
    def __init__(self, state):
        self._state = state
        
    
    def getState(self):
        return self._state
    

class Originator:
    
    
    
    def __init__(self):
        self._state = None
        
    
    def setState(self, state):
        print(f"ORIGINATOR {state}")
        self._state = state
        
    
    def create(self):
        print("ORIGINATOR: CREATE MEMENTO....")
        return Memento(self._state)
    
    
    def restore(self, memento):
        print(f"ORIGINATOR RESTORE STATE: {self._state}")
        self._state = memento.getState()
        
        
    def __str__(self):
        return f"CURRENT STATE {self._state}"
    
    
    
class Caretaker:
    
    def __init__(self):
        self.mementos =[]
        
        
    def addMemento(self, memento):
        print("CARETAKER ADD MEMENTO TO LIST")
        self.mementos.append(memento)
        
        
    def getMemento(self, index):
        return self.mementos[index]
    
    
    
if __name__ == '__main__':
    
    print("MOMENT")
    
    
    originator = Originator()
    
    caretaker = Caretaker()
    
    
    originator.setState("STATE 1")
    caretaker.addMemento(originator.create())
    
    originator.setState("STATE 2")
    caretaker.addMemento(originator.create())
    
    originator.setState("STATE 3")
    caretaker.addMemento(originator.create())
    
    
    originator.restore(caretaker.getMemento(2))
  
    print(originator)  
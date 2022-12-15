from Memento import Memento
import copy

class CareTaker:
    def __init__(self):
        self.memento_list = []
        self.index = 0
    def add(self, state):
        self.memento_list.append(copy.copy(state))

    def undo(self):
        self.index -= 1
        if (self.index < - len(self.memento_list)):
            print("Cannot undo anymore!")
            self.index += 1
            return self.memento_list[self.index]
        return self.memento_list[self.index]
# public class CareTaker {
#    private List<Memento> mementoList = new ArrayList<Memento>();
#
#    public void add(Memento state){
#       mementoList.add(state);
#    }
#
#    public Memento get(int index){
#       return mementoList.get(index);
#    }
# }
class Queue:
    def __init__(self):
        self.List = list()
    
    def push(self, item):
        self.List.append(item)
    
    def pop(self):
        temp = self.List[0]
        self.List = self.List[1:]
        return temp
    
    def is_empty(self):
        return len(self.List) == 0
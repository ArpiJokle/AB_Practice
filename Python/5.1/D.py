class Programmer:
    def __init__(self, name, Status="Junior"):
        self.name = name
        self.Status = Status
        self.worked_time = 0
        self.rises = 0
        self.Money = 0
    
    def work(self, time):
        self.worked_time += time
        if self.Status == "Junior":
            self.Money += time * 10
        if self.Status == "Middle":
            self.Money += time * 15
        if self.Status == "Senior":
            self.Money += time * (20 + self.rises)
    
    def rise(self):
        if self.Status == "Junior":
            self.Status = "Middle"
        elif self.Status == "Middle":
            self.Status = "Senior"
        else:
            self.rises += 1
    
    def info(self):
        return self.name + ' ' + str(self.worked_time) + 'ק. ' + str(self.Money) + "עדנ."
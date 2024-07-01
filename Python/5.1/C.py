class RedButton:
    def __init__(self):
        self.Clicks = 0
    
    def click(self):
        self.Clicks += 1
        print("Тревога!")
    
    def count(self):
        return self.Clicks

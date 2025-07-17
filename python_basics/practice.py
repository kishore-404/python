class car:
    def __init__(self , make ,model ,year):
        self.make = make
        self.model=model
        self.year=year
    def display_info(self):
        print(f"Car {self.year} {self.make} {self.model}")
        
car1 = car(2004,"bugati","tn75")
car1.display_info()
car2 = car(2025,"BMW","tn25")
car2.display_info()
class Car:

    def __init__(self, regno, no_gears):
        self.regno = regno
        self.no_gears = no_gears
        self.is_started = False
        self.gear = 0

    def start(self):
        if self.is_started:
            print(f"Car with reg - {self.regno} already started")
        else:
            print(f"Car with reg - {self.regno} started")
            self.is_started = True
    
    def change(self):
        if self.is_started:
            if self.gear < self.no_gears :
                self.gear += 1
                print(f"Car with reg - {self.regno} gear changed to {self.gear}")
            else:
                print("You are in the top gear!!")
        else:
            print("Car is stopped cannt start")
        
    def stop(self):
        if self.is_started:
            print(f"Car with reg - {self.regno} stopped")
        else:
            print(f"Car with reg - {self.regno} not yet started")
        
        
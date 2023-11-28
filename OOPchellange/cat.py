class cat:
    def __init__(self , name , type , color , age , steps , run ):
        self.name  = name 
        self.type  = type 
        self.color = color 
        self.age   = age 
        self.steps = steps 
        self.run   = run 
        
    def catStep(self):
        print(f"Name is {self.name} .. Type is {self.type} .. color is {self.color} .. age = {self.age} month and can walk {self.steps} steps per seconds")
        
    def catRun(self):
        print(f"Name is {self.name} .. Type is {self.type} .. color is {self.color} .. age = {self.age} month and can run {self.run} steps per seconds")

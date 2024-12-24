class robot:
    def __init__(self , name ,model) :
        self.name=name 
        self.age=model
    def company (self, company  ):
        return f"{self.name } is from {company}"
    def processor (self):
        return f"{self.name } is now processing "
object1 = robot("LinuxV",14)        
object2 = robot("AiApply9",12)
    
print (f"{object1.name} is a {object1.age}th gen model")
print (f"{object2.name} is a {object2.age}th gen model")

print(object1.company("Nvidia"))
print(object1.processor())
print(object2.company("Xerxes"))
print(object2.processor())


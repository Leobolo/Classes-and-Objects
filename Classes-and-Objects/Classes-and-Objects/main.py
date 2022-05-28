
class Student:import enforce


    # [assignment] Skeleton class. Add your code here
    name= String()
    tracks= OneOf()
    age=Number()
    score=Division()
    def __init__(self, name:str, age:int, tracks:str, score:float):
        self.name = str(name)
        self.age = int(age)
        self.tracks = str(tracks)
        self.score = float(score)
   
      
    def change_name(self,name):
        self.name = name
    def change_age(self,age):
        self.age = age
    def add_track(self,tracks):
        self.tracks = tracks
    def get_score(self):
        return self.score


Bob = Student(name= 5, age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
#Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()

print(Student)
print(Bob.age)
print(Bob.name)
print(Bob.get_score())
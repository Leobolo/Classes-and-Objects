
class Student:
    # [assignment] Skeleton class. Add your code here
    
    
    def __init__(self, name:str, age:int, tracks:str, score:float):
        self.name = str(name)
        self.age = int(age)
        self.tracks = list(tracks)
        self.score = float(score)
   
      
    def change_name(self,new_name):
        self.name = new_name
    def change_age(self,new_age):
        self.age = new_age
    def add_track(self,new_tracks):
        self.tracks.append(new_tracks)
    def get_score(self):
        return self.score


Bob = Student(name= "Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()

print(Student)
print(Bob.age)
print(Bob.name)
print(Bob.get_score())
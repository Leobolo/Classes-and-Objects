
class Student:
    # [assignment] Skeleton class. Add your code here
    
    
    def __init__(self, name:str, age:int, tracks:str, score:float):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score
        
         if not type(name) is str:
          raise TypeError("Only strings are allowed")
      
        if not type(age) is int:
          raise TypeError("Only integers  are allowed")
      
        if not type(tracks) is list:
          raise TypeError("Only list are allowed")
      
        if not type(score) is float:
          raise TypeError("Only float are allowed")
      
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

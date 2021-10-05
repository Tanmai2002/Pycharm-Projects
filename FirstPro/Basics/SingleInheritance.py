from Basics.classesmethodAsConsr import Players as ply
class GoalKeeper(ply):
    def __init__(self,PlayersName,Salary):
        self.name=PlayersName
        self.salary=Salary
        self.position="GoalKeeper"

    def xyz(self):
        print("Hiiiiiii")


tan=GoalKeeper("tanu",5000)
print(tan.__dict__) #{'name': 'tanu', 'salary': 5000, 'position': 'GoalKeeper'}

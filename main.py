from tinydb import TinyDB, Query
db = TinyDB("todo.json")
tasks = Query

def createTask():
    
    title = input("Enter task title: ")
    descr = input("Enter task's description: ")
    start_time = input("Enter starting time: ")
    end_time = input("Enter ending time: ")
    compl = False

    db.insert({"title": title,
                "description":descr,
                  "start time": start_time,
                    "end time": end_time,
                      "completion":compl,
                      })


def updateTask():
    ttle = input("update title: ")

    db.update({"title":ttle, })
    db.all()

def deleteTask():
    db.remove(tasks.title < 6)
    db.all()

while True:
    user_input = input("""
Welcome to the Task Manager;
1.Create new tasks:
2.Update the tasks:
3.Delete tasks:
4.Quit task manager:                  
    """).strip()

    # print(user_input)
    
    if user_input == "1":
        createTask()
    elif user_input == "2":
        updateTask()
    elif user_input == "3":
        deleteTask()
    else:
        print("Exit")
        break

import json
import datetime


class Employee(object):
    
    def __init__(self,emp_name,emp_id):
        self.employee = {}
        self.employee["tasks"] = []
        self.employee["emp_name"] = emp_name
        self.employee["emp_id"] = emp_id
        self.employee["login_time"]=str(datetime.datetime.now())

    def add_task(self,task_title,task_description):
        self.task ={}
        self.task["task_title"]=task_title
        self.task["task_description"]=task_description
        self.task["start_time"] = str(datetime.datetime.now())

    def end_task(self, task_success):
        self.task["end_time"] = str(datetime.datetime.now())
        self.task["task_success"] = task_success
        self.employee["tasks"].append(self.task)


    def logout(self):
        self.employee["logout_time"] = str(datetime.datetime.now())
        filename = f"{self.employee['emp_name']}_{str(datetime.datetime.now().date())}.json"
        with open(filename,"w")as f:
            f.write(json.dumps(self.employee))
emp = Employee("ibrahim",123)
emp.add_task("task 1","task compeleted")
emp.end_task(True)
emp.logout()
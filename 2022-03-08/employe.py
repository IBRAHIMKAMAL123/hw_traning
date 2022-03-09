from datetime import datetime
import json


task=[]
class Employee:
    def __init__(self,emplye_name,emplye_id):
        self.emplye_name = emplye_name
        self.emplye_id = emplye_id

    def login_time(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M")

    def task_start(self,task_title,task_description):
        return task_title,task_description

    def start_task_time(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M")

    def task_end(self,task_sucess):
        return task_sucess

    def end_task_time(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M")


    def logout_time(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M")



employee_details =Employee('Ibrahim' , 123)        
task_title1 ,task_description1 = employee_details.task_start('JSON','A JSON file is a file that stores simple data structures and objects in JavaScript Object Notation (JSON) format')
task_title2 ,task_description2 = employee_details.task_start('DATA MINING','Data mining is a process used by companies to turn raw data into useful information.')
task_title3 ,task_description3 = employee_details.task_start('BIG DATA','data that is so large fast or complex that its difficult or impossible to process using traditional methods')
task_sucess1=employee_details.task_end('True')
task_sucess2=employee_details.task_end('false')
task_sucess3=employee_details.task_end('True')
task1 ={
'task_title':task_title1,
    'task_description':task_description1,
    'start_time':employee_details.start_task_time(),
    'end_time':employee_details.end_task_time(),
    'task_sucess':task_sucess1
}
task2 ={
'task_title':task_title2,
    'task_description':task_description2,
    'start_time':employee_details.start_task_time(),
    'end_time':employee_details.end_task_time(),
    'task_sucess':task_sucess2
}
task3 ={
'task_title':task_title3,
    'task_description':task_description3,
    'start_time':employee_details.start_task_time(),
    'end_time':employee_details.end_task_time(),
    'task_sucess':task_sucess3
}
task.append(task1)
task.append(task2)
task.append(task3)

emp = {
    "emp_name":employee_details.emplye_name,
    "emp_id":employee_details.emplye_id,
    "login_time":employee_details.login_time(),
    "logout_time":employee_details.logout_time(),
    "task":task
}
print(emp)
with open("employe.json", "w") as fp:
    json.dump(emp,fp)

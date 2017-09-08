## _*_codig:UTF-8_*_

class employee:
    def __init__(self,lastname, name, age ):
        self.lastname = lastname
        self.name = name
        self.age = age

    def __str__(self):
        return "{},{},{}".format(self.lastname,self.name,self.age)


class EmployeeList(list):


    def AddNewEmployee (self,emp):

        for emptemp in self:
            if emptemp.name == emp.name:
                raise EmployeeDouble ('This is not authorized insert',emp.name)
        self.append(emp)


    def DisplayEmployee(self):
        for ligne in self:
            print('User name:{} lastname: {} age: {}'.format(ligne.name,ligne.lastname,ligne.age))



class EmployeeDouble (Exception):
    def __init__(self,message,name):
        self.message = message
        self.name = name

    def __str__(self):
        return "Error:{}, the user {} already exist".format(self.message,self.name)











'''
res = list()

flag = True
while flag:
    name = input('type name')
    lastname = input('type lastname')
    age = input('type age')
    ObjtEmployee = employee (name=name,lastname=lastname,age=age)
    for employee in res:
        if employee.name == employee.name:
            raise EmployeeDouble ('Employe already included')
        else:
            res.append(ObjtEmployee)
    tracker =str(input('do you need more employees?'))
    if tracker == "No":
        flag=False



for employee in res:
    print(employee.name)


'''
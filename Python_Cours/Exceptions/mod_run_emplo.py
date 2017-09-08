from Exceptions.Employees import employee,EmployeeList,EmployeeDouble

def main ():
    try:
        container = EmployeeList()
        data = open('C:\\Users\\axu30\\Documents\\GitHub\\CBB\\Python_Cours\\Files\\Employees')
        for item in data:
            res = item.split(',')
            ObjtEmp = employee (name=res[0], lastname=res[1],age=res[2])
            container.AddNewEmployee(ObjtEmp)

    except EmployeeDouble as v:
        print(v)

    finally:
        EmployeeList.DisplayEmployee(container)


if __name__ == "__main__":
    main()
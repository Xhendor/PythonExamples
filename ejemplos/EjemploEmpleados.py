class Employee:
  'Common base class for all employees'
  empCount = 0

  def __init__(self, name, salary):
    self.name = name
    self.salary = salary
    Employee.empCount += 1

  def toSadPesos(self):
    conversion = self.salary * 18.60
    print("Tu salario in pesos: " + str(conversion))

  def displayCount(self):
    print("Total Employee %d" % Employee.empCount)

  def displayEmployee(self):
    print("Name : ", self.name, ", Salary: ", self.salary)


emp1 = Employee("Jaimito", 5600)
print("Nombre:" + emp1.name)
emp1 = Employee("Ramuel", 5600)
print("Nombre:" + emp1.name)
emp1 = Employee("Antonio", 5600)
print("Nombre:" + emp1.name)
print(emp1.toSadPesos())

print(Employee.empCount)

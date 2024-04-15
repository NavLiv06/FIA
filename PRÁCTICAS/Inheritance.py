# Simple Inheritance

# Parent class
class Parent:
	def parentFunc(self):
		print("Este es el padre")

# Child class
class Child(Parent):
	def childFunc(self):
		print("Este es el hijo")

hijo = Child()
hijo.parentFunc()
hijo.childFunc()

print()

# Multiple inheritance

# Parent class1
class Mother:
	mothername = ""

	def mother(self):
		print(self.mothername)

# Parent class2
class Father:
	fathername = ""

	def father(self):
		print(self.fathername)

# Child class
class Son(Mother, Father):
	def parents(self):
		print("Nombre del padre :", self.fathername)
		print("Nombre de la madre :", self.mothername)

hijo2 = Son()
hijo2.fathername = "Carl"
hijo2.mothername = "Jenni"
hijo2.parents()

print()

# Multilevel inheritance

# Level1 class
class Grandfather3:
	def __init__(self, grandfathername):
		self.grandfathername = grandfathername

# Level2 class
class Father3(Grandfather3):
	def __init__(self, fathername, grandfathername):
		self.fathername = fathername
		# Se utiliza el constructor de la clase abuelo para asignar
        # el nombre del abuelo dede esta clase
		Grandfather3.__init__(self, grandfathername)

# Child class
class Son3(Father3):
	def __init__(self, sonname, fathername, grandfathername):
		self.sonname = sonname
		# Se utiliza el constructor de la clase padre para asignar
        # el nombre del padre desde esta clase
		Father3.__init__(self, fathername, grandfathername)

	def print_name(self):
		print('Nombre del abuelo :', self.grandfathername)
		print("Nombre del padre :", self.fathername)
		print("Nombre del hijo :", self.sonname)

hijo3 = Son3('Sebastian', 'Carl', 'Yepeto')
print(hijo3.grandfathername)
hijo3.print_name()

print()

# Hierarchical inheritance
# Parent class
class Parent4:
	def parentFunc(self):
		print("Este es el padre")

# Child1 class
class firstChild4(Parent4):
	def child1Func(self):
		print("Este es el primer hijo")

# Child2 class
class secondChild4(Parent4):
	def child2Func(self):
		print("Este es el segundo hijo")

firstHijo4 = firstChild4()
secondHijo4 = secondChild4()
firstHijo4.parentFunc()
firstHijo4.child1Func()
secondHijo4.parentFunc()
secondHijo4.child2Func()

print()

# Multipath inheritance
# Class1
class School:
	def func1(self):
		print("Este alumno esta inscrito en la escuela")

# Class2
class Student1(School):
	def func2(self):
		print("Estudiante 1")

# Class3
class Student2(Student1, School):
	def func3(self):
		print("Estudiante 2")

estudiante = Student2()
estudiante.func1()
print("Esta relacionado con:")
estudiante.func2()

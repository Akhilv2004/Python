class Student:
    def readData(self):
        self.rollno = int(input("Enter roll number: "))
        self.mark1 = float(input("Enter marks for subject 1: "))
        self.mark2 = float(input("Enter marks for subject 2: "))

    def computeTotal(self):
        self.total = self.mark1 + self.mark2

    def printDetails(self):
        print(f"Roll No: {self.rollno}, Mark1: {self.mark1}, Mark2: {self.mark2}, Total: {self.total}")

student = Student()
student.readData()
student.computeTotal()
student.printDetails()

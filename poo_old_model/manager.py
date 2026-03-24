from employee import Employee

class Manager(Employee):
     def __init__(self, name, emp_id, hourly_rate, department):
         super().__init__(name, emp_id, hourly_rate)
         self._department = department

     def get_department(self):
         return self._department

     def set_department(self, department):
         self._department = department

     def calculate_salary(self):
         # Assuming managers have a 10% bonus on salary
         base_salary = super().calculate_salary()
         bonus = base_salary * 0.10
         return base_salary + bonus
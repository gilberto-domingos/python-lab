from employee import Employee

class Engineer(Employee):
     def __init__(self, name, emp_id, hourly_rate, team):
         super().__init__(name, emp_id, hourly_rate)
         self._team = team

     def get_team(self):
         return self._team

     def set_team(self, team):
         self._team = team

     def calculate_salary(self):
         # Assuming engineers have a 5% bonus on their salary
         base_salary = super().calculate_salary()
         bonus = base_salary * 0.05
         return base_salary + bonus
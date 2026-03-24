class Employee:
    def __init__(self, name, emp_id, hourly_rate):
        self._name = name
        self._emp_id = emp_id
        self._hourly_rate = hourly_rate
        self._hours_worked = 0

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_emp_id(self):
        return self._emp_id

    def set_emp_id(self, emp_id):
        self._emp_id = emp_id

    def get_hourly_rate(self):
        return self._hourly_rate

    def set_hourly_rate(self, hourly_rate):
        self._hourly_rate = hourly_rate

    def get_hours_worked(self):
        return self._hours_worked

    def set_hours_worked(self, hours):
        self._hours_worked = hours

    def calculate_salary(self):
        return self._hourly_rate * self._hours_worked

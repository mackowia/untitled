class Employee:
    def __init__(self, first_name, last_name, rate_per_hour):
        self.firts_name = first_name
        self.last_name = last_name
        self.rate_per_hour = rate_per_hour
        self.salary_to_pay = 0
        # self.time= 0

    def register_time(self, time):
        if time > 8:
            self.salary_to_pay += 8 * self.rate_per_hour + \
                                 (time - 8 ) * 2 * self.rate_per_hour
           #self. time = ... to samo tylko bez "*self.rate_per_hour"
        else:
            self.salary_to_pay += time * self.rate_per_hour
            #self.time= time

    def pay_salary(self):
        result = self.salary_to_pay
       #result = self.time * self.rate_per_hour
        self.salary_to_pay = 0
       #self.time = 0
        return result



    #def print_info(self):
     #   print(f"Pracwnik {self.first_name, self.last_name} był w pracy {self.time} i zarobił {self.sallary_to_pay} PLN")

    #def test_product_init():
     #   employee = Employee("Jan", "Nowak", 100)
      #  assert employee.first_name == "Jan"
       # assert employee.last_name == "Nowak"
        #assert employee.rate_per_hour == 100

if __name__ == '__main__':
    employee = Employee("Jan", "Nowak", 100)
    employee.register_time(5)
    print(employee.pay_salary())
    print(employee.pay_salary())
    employee.register_time(10)
    print(employee.pay_salary())
    employee.register_time(5)
    employee.register_time(5)
    print(employee.pay_salary())
    #employee.print_info()
class Person:
    def __init__(self, name, money, mood, health_rate):
        self.name = name
        self.money = money
        self.mood = mood
        self.health_rate = health_rate

    def sleep(self, hours):
        if hours == 7:
            self.mood = "Happy"
        elif hours < 7:
            self.mood = "Tired"
        else:
            self.mood = "Lazy"

    def eat(self, meals):
        if meals == 3:
            self.health_rate = 100
        elif meals == 2:
            self.health_rate = 75
        elif meals == 1:
            self.health_rate = 50

    def buy(self, items):
        self.money -= 10 * items



class Car:
    def __init__(self, name, fuel_rate, velocity):
        self.name = name
        self.fuel_rate = self.set_fuel_rate(fuel_rate)
        self.velocity = self.set_velocity(velocity)

    def set_velocity(self, velocity):
        return max(0, min(200, velocity))

    def set_fuel_rate(self, fuel_rate):
        return max(0, min(100, fuel_rate))

    def run(self, velocity, distance):
        self.velocity = self.set_velocity(velocity)
        fuel_needed = (distance // 10) * 10 

        if self.fuel_rate >= fuel_needed:
            self.fuel_rate -= fuel_needed
            print(f"Car ran {distance} km at {self.velocity} km/h.")
            self.stop(0)
        else:
            max_distance = (self.fuel_rate // 10) * 10
            print(f"Car ran {max_distance} km at {self.velocity} km/h before stopping.")
            self.fuel_rate = 0
            self.stop(distance - max_distance)

    def stop(self, remaining_distance):
        self.velocity = 0
        if remaining_distance == 0:
            print("The car has arrived at the destination.")
        else:
            print(f"The car stopped with {remaining_distance} km remaining due to low fuel.")


class Employee(Person):
    def __init__(self, name, money, mood, health_rate, emp_id, car, email, salary, distance_to_work):
        super().__init__(name, money, mood, health_rate)
        self.id = emp_id
        self.car = car
        self.email = email
        self.salary = self.set_salary(salary)
        self.distance_to_work = distance_to_work

    def set_salary(self, salary):
        return max(1000, salary)

    def work(self, hours):
        if hours == 8:
            self.mood = "Happy"
        elif hours < 8:
            self.mood = "Lazy"
        else:
            self.mood = "Tired"

    def drive(self, distance, velocity):
        print(f"{self.name} is driving {distance} km at {velocity} km/h.")
        self.car.run(velocity, distance)

    def refuel(self, gas_amount):
        self.car.fuel_rate = min(100, self.car.fuel_rate + gas_amount)
        print(f"Refueled car. Current fuel rate: {self.car.fuel_rate}%")

    def send_mail(self, to, subject, body):
        print(f"Sending mail to: {to}\nSubject: {subject}\n{body}")


class Office:
    def __init__(self, name):
        self.name = name
        self.employees = {}

    def hire(self, employee):
        self.employees[employee.id] = employee
        print(f"{employee.name} has been hired.")

    def fire(self, emp_id):
        if emp_id in self.employees:
            print(f"{self.employees[emp_id].name} has been fired.")
            del self.employees[emp_id]
        else:
            print("Employee not found.")

    def get_all_employees(self):
        return list(self.employees.values())

    def get_employee(self, emp_id):
        return self.employees.get(emp_id, None)

    def check_lateness(self, emp_id, arrival_time):
        employee = self.get_employee(emp_id)
        if employee:
            expected_time = 9  
            if arrival_time > expected_time:
                print(f"{employee.name} is late.")
            else:
                print(f"{employee.name} is on time.")


car = Car("Fiat 128", 50, 60)
samy = Employee("Samy", 1000, "Neutral", 80, 1, car, "samy@iti.com", 5000, 30)
iti = Office("ITI")
iti.hire(samy)
samy.drive(30, 80)
samy.refuel(40)
iti.check_lateness(samy.id, arrival_time=9)


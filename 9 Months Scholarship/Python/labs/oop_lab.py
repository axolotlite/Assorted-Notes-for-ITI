

class Person:
    def __init__(self, name, money, mood, healthRate):
        self.name = name
        self.money = money
        self.mood = mood
        self.healthRate = healthRate

    def sleep(self,time):
        match time:
            case 7:
                self.mood = "happy"
            case 6 | 5 | 4 | 3 | 2 | 1 | 0:
                self.mood = "tired"
            case _:
                self.mood = "lazy"
        print(f"sleep result: {self.mood}")
    def eat(self, meals):
        match meals:
            case 3:
                self.healthRate = 100
            case 2:
                self.healthRate = 75
            case 1:
                self.healthRate = 50
        print(f"eat result: {self.healthRate}")
    def buy(self, items):
        while money >= 0 and items != [] :
            money -= 10
            items.pop()
        elif money == 0:
            print("you've run out of money, you cannot purchase anything else...")
        print(f"remaining money: {self.money}")

class Employee(Person):
    def __init__(self, name, money, mood, healthRate, eid, car, email, salary, distanceToWork ):
        self.super().__init__(name,money,mood,healthRate)
        self.eid = eid
        self.car = car
        self.email = email
        self.salary = salary
        self.distanceToWork = distanceToWork
    def work(self, time):
        match time:
            case 8:
                self.mood = "happy"
            case 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0:
                self.mood = "lazy"
            case _:
                self.mood = "tired"
        print("work")
    def drive(self, distance):
        self.car.run(distance,100)
        print("drive")
    def refuel(self, gasAmount):
        self.car.add_fuel(gasAmount)
        print("refuel")
    def send_email(self):
        print("send_email")

class Office:
    def __init__(self, name, employees):
        self.name = name
        self.__employees = employees
        employeesNum += len(employees)
    @classmethod
    def change_emps_num(num):
        Office.employeesNum = num
    def get_all_employees(self):
        return self.__employees
    def get_employee(self, eid):
        for employee in self.__employees:
            if eid == employee.eid:
                return employee
        return None
    def hire(self, employee):
        Office.employeesNum+=1
        self.employees.append(self.__employee)
        print(f"hired {employee.name}")
    def fire(self, eid):
        Office.employeesNum -=1
        employee = self.get_employee(eid)
        if employee == None:
            print("eid doesn't exit")
            return
        self.employees.remove(self.__employee)
        print(f"fired {employee.name} from the office")
    @staticmethod
    def calculate_lateness(targetHour, moveHour, distance, velocity):
        """
        int: targetHour (assumed arrival time)
        int: moveHour (assumed departure time)
        int: distance (distance between employee and office)
        int: velocity (the speed of the employees car)

        time will be calculate in hours
        """
        time = int(distance / velocity)
        difference = targetHour - (moveHour + time)
        return difference
        if difference > 0:
            return True
        elif difference < 0:
            return False
        return None
    def check_lateness(self, eid, arrivalHour):
        if 9 - arrivalHour > 0:
            self.reward(10)
        elif 9 - arrivalHour < 0:
            self.deduct(10)
    def deduct(self, eid, deduction):
        employee = self.get_employee(eid)
        if employee == None:
            print("eid doesn't exist")
            return
        employee.salary -= deduction
        print(f"deducted {deduction} from employee {employee.name}")
    def reward(self, eid, reward):
        employee = self.get_employee(eid)
        if employee == None:
            print("eid doesn't exist")
            return
        employee.money += reward
        print(f"rewarded {employee.name} by giving him an extra {reward}")

class Car:
    def __init__(self, name, fuelRate, velocity):
        self.name = name
        self.__fuelRate = self.set_fuel(fuelRate)
        self.__velocity = self.set_velocity(velocity)
    def deplete(self):
        if self.__fuelRate <= 0:
            self.stop("fuel tank is empty...")
            self.__fuelRate = 0
            return False
        self.__fuelRate-= 1
        return True
    def set_fuel(self, fuelRate):
        if fuelRate >= 100:
            self.__fuelRate = 100
        elif fuelRate < 0:
            self.__fuelRate = 0
        else:
            self.__fuelRate = fuelRate
    def add_fuel(self, gasAmount):
        self.set_fuel(self.__fuelRate + gasAmount)
    def set_velocity(self, velocity):
        if velocity >= 200:
            self.__velocity = 200
        elif velocity < 0:
            self.__velocity = 0
        else:
            self.__velocity == velocity
    def run(self, velocity, distance):
        """
        int: velocity is in km/hr
        int: distance is in kms
        fuelrate loss is 1% for each kilometer
        """
        while self.deplete() and distance:
            self.set_velocity(velocity)
            distance-=1
            self.deplete()
        else:
            self.stop("arrived at destination")

    def stop(self,notification):
        self.set_velocity(0)
        print(f"stop reason {notification}")


from datetime import date

# TASK 2

class Worker():
    workers = list()

    def __init__(self, name, age, salary):
        self.number = len(Worker.workers) + 1
        self.name = name
        self.age = age
        self.salary = salary
        Worker.workers.append(self)

    def avg_salary():
        try:
            salary_sum = sum(worker.salary for worker in Worker.workers)
            number_of_workers = len(Worker.workers) 
            return salary_sum/number_of_workers
        except ZeroDivisionError:
            return 0

    def avg_salary_before_30():
        try:
            filtered_list = list(filter(lambda worker: date.today().year - worker.age < 30, Worker.workers))
            salary_sum = sum(worker.salary for worker in filtered_list)
            number_of_workers = len(filtered_list) 
            return salary_sum/number_of_workers
        except ZeroDivisionError:
            return 0
        

    def avg_salary_after_30():
        try:
            filtered_list = list(filter(lambda worker: date.today().year - worker.age >= 30, Worker.workers))
            salary_sum = sum(worker.salary for worker in filtered_list)
            number_of_workers = len(filtered_list) 
            return salary_sum/number_of_workers
        except ZeroDivisionError:
            return 0

    def compare_salary():
        return f'Salary for workers younger than 30 is {avg_salary_before_30} and for older is {avg_salary_after_30}'

    def __str__(self):
        return f'{self.number} {self.name} {self.age} {self.salary}'

Worker('Adam', 1983, 1500)
Worker('Anna', 1981, 1700)
Worker('Błażej', 1990, 1800)
Worker('Beata', 1992, 1600)
Worker('Czesław', 1980, 2000)
Worker('Cecylia', 1983, 2100)
Worker('Daniel', 1976, 1900)

for worker in Worker.workers:
    print(worker)

avg_salary = Worker.avg_salary()
avg_salary_before_30 = Worker.avg_salary_before_30()
avg_salary_after_30 = Worker.avg_salary_after_30()
print(avg_salary)
print(avg_salary_before_30)
print(avg_salary_after_30)
print(Worker.compare_salary())
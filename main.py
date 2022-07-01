from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime, date, time


def main():
    print(str(datetime.today())[:10])
    calculate_salary()
    get_employees()


if __name__ == "__main__":
    main()

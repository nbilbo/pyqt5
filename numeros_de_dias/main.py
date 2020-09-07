from PyQt5.QtCore import QDate, Qt

other_date = QDate(1945, 5, 7)
print(f'Days in month {other_date.month()}: {other_date.daysInMonth()}')
print(f'Days in year {other_date.year()}: {other_date.daysInYear()}')
print('\n')

current_year = QDate.currentDate()
last_year = QDate(2018, 12, 21)
new_year = QDate(2021, 1, 1)

dayspassed = last_year.daysTo(current_year)
print(f'{dayspassed} days have passed between {last_year.toString(Qt.ISODate)} and {current_year.toString(Qt.ISODate)}')

daysuntil = current_year.daysTo(new_year)
print(f'There are {daysuntil} days ultil {new_year.toString(Qt.ISODate)}')

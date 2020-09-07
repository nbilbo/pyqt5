from PyQt5.QtCore import QDate, QTime, QDateTime, Qt


now = QDate.currentDate()

print('--Current date--')
print(now.toString(Qt.ISODate))
print(now.toString(Qt.DefaultLocaleLongDate))

print('--Date and time--')
datetime = QDateTime.currentDateTime()
print(datetime.toString(Qt.ISODate))
print(datetime.toString(Qt.DefaultLocaleLongDate))

print('--Time--')
time = QTime.currentTime()
print(time.toString(Qt.ISODate))
print(time.toString(Qt.DefaultLocaleLongDate))

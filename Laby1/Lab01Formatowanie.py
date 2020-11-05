from datetime import datetime
date='{:%Y-%m-%d %H:%M}'.format(datetime(2020, 10, 29, 14, 0))
print(date)

number='{:{}{sign}{}.{}}'.format(1.99, '>', 10, 2, sign='+')
print(number)

tekst='{:{align}{width}}'.format('Robię przykłady formatowania', align='^', width='14')
print(tekst)

numbers_data= [5, 11, 13, 12, 14, 41]
date2='{d[4]} {d[5]}'.format(d=numbers_data)
print(date2)

text='{first} {last}'.format(first='Hello', last='Pycharm!')
print(text)


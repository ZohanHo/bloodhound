def func():
    c = 2+2
    print(c)

#func()  - так запустится


""" 
В момент первого импортирования модуля происходит выполнение ф-ций модуля
Eсли мы хотим что бы код был запущен только тогда когда модуль запускается вручную, а не когда он импортируется, то
 вызывать его ф-ции нужно только после условия  if __name__ == "__main__": 
"""


if __name__ == "__main__":
    func()

""" 
Данной конструкции ф-ция func не запустится пос ле того как мы его импортировали в файле runModule.py, 
если вызвать ф-цию до условия  if __name__ == "__main__": то ф-ция запустится
"""
Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

======= RESTART: C:/Users/User/OneDrive/เดสก์ท็อป/Python 101/writefile.py ======
ดินสอ 10 บาทปากกา 10 บาท
ยางลบ 10 บาท
สมุดวาดรูป 6 บาท
กบเหลา 3 บาท

box = []
box.append('ปากกา')
box.append('ดินสอ')
box.append('ยางลบ')
print(box)
['ปากกา', 'ดินสอ', 'ยางลบ']
print(box[1])
ดินสอ
print(box[0])
ปากกา
print(box[2])
ยางลบ
print(box[-1])
ยางลบ
print(box[-2])
ดินสอ
print(box[-3])
ปากกา
print(box[-4])
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    print(box[-4])
IndexError: list index out of range
brand = {'pen':['lamy','Pentel','Fiber-castel'],'Pencil':['hourse','staedtler'],'eraser':'ยางลบ2สีไทย'}
brand = {'pen':['lamy','Pentel','Fiber-castel'],'Pencil':['hourse','staedtler'],'eraser':'ยางลบ2สี'}
print(brand['pen'])
['lamy', 'Pentel', 'Fiber-castel']
print(brand['pen'][1])
Pentel
print(brand['pencil'][0])
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    print(brand['pencil'][0])
KeyError: 'pencil'
print(brand['pencil'][0])
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    print(brand['pencil'][0])
KeyError: 'pencil'
print(brand['eraser'][0])
ย
print(brand['eraser'])
ยางลบ2สี
print(brand['Pencil'][0])
hourse
print(brand['Pencil'][1])
staedtler
print(box)
['ปากกา', 'ดินสอ', 'ยางลบ']
print(len(box))
3
print(brand.keys())
dict_keys(['pen', 'Pencil', 'eraser'])
print(brand.values())
dict_values([['lamy', 'Pentel', 'Fiber-castel'], ['hourse', 'staedtler'], 'ยางลบ2สี'])
for b in box:
    print(b)

    
ปากกา
ดินสอ
ยางลบ
for br in brand.keys():
    print(br)

    
pen
Pencil
eraser
for br in brand.values():
    print(br)

    
['lamy', 'Pentel', 'Fiber-castel']
['hourse', 'staedtler']
ยางลบ2สี
for br in brand:
...     print(br)
... 
...     
pen
Pencil
eraser
>>> for br in brand.times():
...     print(br)
... 
...     
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    for br in brand.times():
AttributeError: 'dict' object has no attribute 'times'
>>> for br in brand.items():
...     print(br)
... 
...     
('pen', ['lamy', 'Pentel', 'Fiber-castel'])
('Pencil', ['hourse', 'staedtler'])
('eraser', 'ยางลบ2สี')
>>> len(brand)
3

print ('โปรแกรมให้สำหรับค่าซื้อบ้าน')
members = {}
for i in range (5):
    key = input('กรุณากรอกชื่อ: ')
    value = input ('กรุณากรอกอายุ: ')
    members[key] = value
    if int(value) >= 60:
        print('คุณได้ส่วนลด 15%')
    else:
        print('คุณได้ส่วนลด 10%')   

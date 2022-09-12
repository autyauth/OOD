""""
เขียนโปรแกรมสำหรับหา หรม. ของเลข 2 ตัว

****ห้ามใช้คำสั่ง len, for, while, do while หรือ *****

หมายเหตุ ฟังก์ชันต้องมี parameter แค่เพียง 2 ตัว

บทนิยาม

ตัวหารร่วมมาก หรือ ห.ร.ม. (อังกฤษ: greatest common divisor: gcd) ของจำนวนเต็มสองจำนวนซึ่งไม่เป็นศูนย์พร้อมกัน คือจำนวนเต็มที่มากที่สุดที่หารทั้งสองจำนวนลงตัว
"""
def gcd(x , y):
    if x == 0 and y == 0:
        return 'Error! must be not all zero.'
    if y == 0:
        return x
    else:
        return gcd(y, x%y)
    # หารร่วมมาก ของ 2 เลข เลขที่ 1 มากกว่า เลขที่ 2 แปลว่ายังไงค่ามากสุดที่ของ ห.ร.ม. คือเลขที่ 2 ก็เลย
    # x/y = (k*y + x)/y
    # 18/12 = (1*12+6)/12 ->-> 1 + 6/12 ->-> 6/12 = (0*12+6)/12
    # gcd(y,x%y) ก็จะสลับกันหารแล้วเอาเศษจนกว่าจะเหลือ 0 ถ้าเหลือ 0แปลว่าได้ หรม แล้ว
    # ห.ร.ม 18 12
    # 12, 18%12=6
    # 6 , 12%6=0
    # แปลว่า y จะเหลือ 0 แล้วจะได้ ห.ร.ม คือ x=6
input = input("Enter Input : ").split(" ")
if input[0] < input[1]:
    x = input[0]
    input[0] = input[1]
    input[1] = x
if input[0] == '0' and input[1] == '0':
    print(str(gcd(abs(int(input[0])),abs(int(input[1])))))
else:
    print('The gcd of '+ input[0] +' and '+input[1]+' is : '+str(gcd(abs(int(input[0])),abs(int(input[1])))))
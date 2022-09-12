""""
นักศึกษาจะได้รับ Input เป็น list<int> ของดาวเคราะห์น้อย
สำหรับดาวเคราะห์น้อยแต่ละดวงนั้น ค่าสัมบูรณ์ จะแสดงขนาดของมัน และเครื่องหมายแสดงถึงทิศทางของมัน (ถ้าเลขเป็นบวกแสดงว่าวิ่งไปทางขวา ,ลบทางซ้าย) โดยที่ดาวเคราะห์น้อยแต่ละดวงเคลื่อนที่ด้วยความเร็วเท่ากัน

ค้นหาสถานะของดาวเคราะห์น้อยหลังจากการชนกันทั้งหมด

1.หากดาวเคราะห์น้อยสองดวงมาพบกันดวงที่เล็กกว่าจะระเบิด

2.ถ้าทั้งสองมีขนาดเท่ากันทั้งคู่จะระเบิด

3.ดาวเคราะห์น้อยสองดวงที่เคลื่อนที่ไปในทิศทางเดียวกันจะไม่มีวันพบกัน

****ห้ามใช้คำสั่ง for, while, do while*****

หมายเหตุ ฟังก์ชันมี parameter ได้ไม่เกิน 2 ตัว

def asteroid_collision(asts):
    #Code Here

x = input("Enter Input : ").split(",")
x = list(map(int,x))
print(asteroid_collision(x))

Enter Input : -2, -1, 1, 2
[-2, -1, 1, 2]

Enter Input : -2, 1, 1, -2
[-2, -2]

Enter Input : 1, 1, -2, -2
[-2, -2]

Enter Input : 10, 2, -5
[10]

Enter Input : 8, -8
[]

Enter Input : 2,-2,3,4
[3, 4]

Enter Input : 4,2,3,-3
[4, 2]

"""
def asteroid_collision(asts,index):
    if asts == []:
        return []
    elif index+1 == len(asts):
        return asts
    else:
        if asts[index] < 0: # ปัจจุบันลบ
            if index == 0: # ถ้าปัจจุบันเป็นตัวแรกให้ขยับ เพราะเราจะเช็คการระเบิดทางซ้าย
                return asteroid_collision(asts,index+1)
            else:
                if asts[index-1] < 0: # ฝั่งซ้ายลบให้เราข้ามตัวแรก 
                    return asteroid_collision(asts, index + 1)
                #ซ้ายเป็นบวก แล้วปัจจุบันลบ ก็ต้องเช็คว่าทางซ้ายใหญ่หรือเล็กวกว่าหรือเท่ากัน
                else:
                    if asts[index-1] < asts[index]*(-1) : # แล้วปัจจุบันใหญกว่าให้pop ซ้าย
                        asts.pop(index-1)
                        return asteroid_collision(asts,0)
                   
                    elif asts[index-1] > asts[index]*(-1): # แล้วปัจจุบันใหญเล็กให้pop ปัจจุบัน
                        asts.pop(index)
                        return asteroid_collision(asts,0)
                    
                    elif asts[index-1] == asts[index]*(-1): # เท่ากับให้ระเบิดคู่
                        asts.pop(index)
                        asts.pop(index)
                        return asteroid_collision(asts,0)    
        elif asts[index] > 0: # ปัจจุบันบวก
            if asts[index+1] > 0: # แล้วขวาบวกให้ขยับไปอีก
                return asteroid_collision(asts, index + 1) 
            else:
                if asts[index] > asts[index+1]*(-1):
                    asts.pop(index+1)
                    return asteroid_collision(asts,0)
                    
                elif asts[index] < asts[index+1]*(-1):
                    asts.pop(index)
                    return asteroid_collision(asts,0)
                   
                elif asts[index] == asts[index+1]*(-1):
                    asts.pop(index)
                    asts.pop(index)
                    return asteroid_collision(asts,0)
    
x = input("Enter Input : ").split(",")
x = list(map(int,x))
print(asteroid_collision(x,0))
# print(x)
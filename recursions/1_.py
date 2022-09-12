"""""
จงเขียนฟังก์ชั่นที่แสดงผลเลข 1 จนถึง n

และฟังก์ชั่นที่แสดงผลเลขตั้งแต่ n จนถึง 1

โดยแสดงผลตามตัวอย่าง

****ห้ามใช้คำสั่ง len, for, while, do while, split*****

หมายเหตุ ฟังก์ชันต้องมี parameter แค่เพียง 1 ตัว

def print1ToN(n):
    #code here

def printNto1(n):
    #code here

n = int(input("Enter Input : "))

print1ToN(n)
printNto1(n)

Enter Input : 6
1 2 3 4 5 6 6 5 4 3 2 1 

Enter Input : -1
1 1 

Enter Input : 1
1 1 

"""

def print1ToN(n):
    if n > 1:
        print1ToN(n-1)
        print(n,end=" ")               
    if n <= 1:
        print(1,end=" ")
    #นับ 1 ถึง n เลยก็ต้องเรียกซ้ำโดยใช้ n-1 ก่อน ทำให้ตัวแรกจะปริ้นก่อนจะเป็น 1 
    # จากนั้นจะเป็น 2 3 4 5 ไปเรื่อยๆ เพราะตัวก่อนหน้าจะเป็น n - (k-1) ; k คือจำนวนรอบที่เรียกซ้ำ 
def printNto1(n):
    if n > 1:
        print(n,end=" ")
        printNto1(n-1)
    else:
        print(1,end=" ")
    # ส่วนอันนี้จะปริ้น n ถึง 1 ก็เลยให้ปริ้นก่อนทำซ้ำ เพราะว่าจะได้ปริ้น n ที่มีค่ามากสุดก่อน 
    # จากนั้นเรียกซ้ำก็จะปริ้น n-1 ไปเรื่อยๆจนถึง 1
       

n = int(input("Enter Input : "))

print1ToN(n)
printNto1(n)



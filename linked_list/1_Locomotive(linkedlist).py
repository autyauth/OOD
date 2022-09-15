""""
มีรถไฟอยู่ขบวนหนึ่ง โดยรถไฟนั้นจะมีหมายเลขกำกับตู้แต่ละตู้อยู่และรถไฟก็มีหัวรถจักรอยู่

แต่หัวรถจักรดันไปต่อกับตู้รถไฟอยู่ พี่ต้องการให้น้อง ๆ ทำการแบ่งขบวนรถไฟออก

โดยให้หัวรถจักรอยู่ข้างหน้าสุด และส่วนตู้ที่เหลือให้ทำการต่อกับตู้สุดท้ายโดยไม่มีการเปลี่ยนลำดับของตู้

ซึ่งพี่จะให้หมายเลข 0 แทนเป็นหัวรถจักร ส่วน หมายเลขอื่นจะเป็นตู้รถไฟ

เช่น 2 <- 3 <- 1 <- 0 <- 4 <- 5 <- 6

เป็น 0 <- 4 <- 5 <- 6 <- 2 <- 3 <- 1 ( ให้ใช้ singly linked list)


 *** Locomotive ***
Enter Input : 2 3 1 0 4 5 6
Before : 2 <- 3 <- 1 <- 0 <- 4 <- 5 <- 6
After : 0 <- 4 <- 5 <- 6 <- 2 <- 3 <- 1


 *** Locomotive ***
Enter Input : 5 4 3 2 1 0 9 8 7 6
Before : 5 <- 4 <- 3 <- 2 <- 1 <- 0 <- 9 <- 8 <- 7 <- 6
After : 0 <- 9 <- 8 <- 7 <- 6 <- 5 <- 4 <- 3 <- 2 <- 1

 *** Locomotive ***
Enter Input : 1 0
Before : 1 <- 0
After : 0 <- 1

*** Locomotive ***
Enter Input : 0 1 2 3 4 5 6 7 8 9
Before : 0 <- 1 <- 2 <- 3 <- 4 <- 5 <- 6 <- 7 <- 8 <- 9
After : 0 <- 1 <- 2 <- 3 <- 4 <- 5 <- 6 <- 7 <- 8 <- 9

 *** Locomotive ***
Enter Input : 1 2 3 0
Before : 1 <- 2 <- 3 <- 0
After : 0 <- 1 <- 2 <- 3


 *** Locomotive ***
Enter Input : 2 0 1
Before : 2 <- 0 <- 1
After : 0 <- 1 <- 2

"""
class LinkedList:
    class Node:
        def __init__(self, data, next = None):
            self.data = data
            if next == None:
                self.next = None
            else:
                self.next = next
                
        def  __str__(self):
            return str(self.data)
    def __init__(self):
        self.head = None   
    def append(self, data):
        node = self.Node(data)
        if self.head == None:
            self.head = node
        else:
            t = self.head 
            # ตัวแปร ที่มี pointer ชี้ไปยัง node หัว 
            while t.next != None: # t ที่ชี้ไปยังตัวถัดไปของ node ปัจจุบัน
            # ถ้า node ต่อไปก็ให้ t ชี้ไปยัง node ต่อไป ทำไปเรื่อยๆ จนเจอ node สุดท้ายที่ไม่มี next
                t = t.next # t ชี้ไปยัง t ตัวต่อไป
            # เมื่อเจอ next ของ node สุดท้ายที่เป็น None หรือไม่มี next ให้ next ของ node สุดท้ายขี้ไปยัง node ที่เพิ่มเข้ามา                
            t.next = node  # t ตัวที่ผ่านมาก็จะสร้าง next ที่ชี้ไปยัง node ต่อไป วนทำซ้ำเรื่อยๆจนครบ
            # node ที่พึ่งสร้างมาต่อเป็น node สุดท้าย ดังนั้นทางก็ต้องเป็น node ที่พึ่งสร้าง
    def printList(self):
        t = self.head
        while t.next != None:
            print(t.data,end=" <- ")
            t = t.next
        if t.next == None:
            print(t)
    def switch(self):
        print('Before : ',end="")
        self.printList()
        t = self.head
        if t.data != 0:
            while t.next != None:
                t = t.next
                if t.data == 0:
                    new_head = t
            # หา 0 ให้เจอเพื่อเก็บไว้เป็นหัวใหม่
            t.next = self.head
            while t.next.data != 0:
                t = t.next
            t.next = None
            # หา t.next ว่าเป็น 0 ไหม ถ้าใช่ก็ตัดตัวชี้ทิ้ง
            self.head = new_head  
            # เราค่อยสร้างหัวใหม่ที่ 0 
            
        print('After : ',end="")
        self.printList()
# list = [4,3,1,0,4,5,6]
# list = [5,4,3,2,1,0,9,8,7,6]
# list = [0,1,2,3,4,5]
# list = [1,2,3,0]
# list = [2,0,1]
lists = LinkedList()
list = input(' *** Locomotive ***\nEnter Input : ').split(" ")
for number in list:
    number = int(number)
    lists.append(number)
lists.switch()


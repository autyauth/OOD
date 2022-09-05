""""ให้น้องๆเขียนโปรแกรมโดยรับ input 2 แบบ โดยใช้ QUEUE ในการแก้ปัญหา



E  <value>  ให้นำ value ไปใส่ใน QUEUE และทำการแสดงผลค่าที่ทำการ enqueue และ index ของตัวที่ทำการเพิ่มเข้าไป

D                 ให้ทำการ dequeue ตัวที่อยู่หน้าสุดของ Queue ออกและแสดงตัวเลขที่เอาออกและแสดงขนาดของ Queue

                    หลังจากทำการ dequeue แล้ว

*** ในตอนสุดท้ยถ้าหากใน Queue ยังมี Value อยู่ให้แสดงผลออกมา  ถ้าหากไม่มีแล้วให้แสดงคำว่า  Empty ***


Enter Input : E 10,E 20,E 30,E 40,D,D
Add 10 index is 0
Add 20 index is 1
Add 30 index is 2
Add 40 index is 3
Pop 10 size in queue is 3
Pop 20 size in queue is 2
Number in Queue is :  ['30', '40']

-------------------------------------------------------------------------

Enter Input : E 10,E 20,E 30,E 40,D,E 50,E 60,D,D,D,D,D,D
Add 10 index is 0
Add 20 index is 1
Add 30 index is 2
Add 40 index is 3
Pop 10 size in queue is 3
Add 50 index is 3
Add 60 index is 4
Pop 20 size in queue is 4
Pop 30 size in queue is 3
Pop 40 size in queue is 2
Pop 50 size in queue is 1
Pop 60 size in queue is 0
-1
Empty

-------------------------------------------------------------------------

Enter Input : D,D,D,D,D
-1
-1
-1
-1
-1
Empty

-------------------------------------------------------------------------

Enter Input : D,E 99,D,D,E 88,D,D,E 12,E 13,E 86
-1
Add 99 index is 0
Pop 99 size in queue is 0
-1
Add 88 index is 0
Pop 88 size in queue is 0
-1
Add 12 index is 0
Add 13 index is 1
Add 86 index is 2
Number in Queue is :  ['12', '13', '86']


"""
class Queue:
    def __init__(self,list = None):
        if list == None:
            self.items = []
        else:
            self.items = list
    def deQueue(self):
        return self.items.pop(0)
    def enQueue(self,item):
        self.items.append(item)
    def isEmptry(self):
        return self.items == 0 
    def size(self):
        return len(self.items)

def the_next_queue(input):
    queue = Queue()
    
    for type_and_number in input:
        type_and_number = type_and_number.split(" ")
        type = type_and_number[0]
        if type == 'E':
            number = type_and_number[1]
            index = str(queue.size())
            queue.enQueue(number)
            print('Add '+ number +' index is '+ index)
        elif type == 'D':
            if queue.size() > 0:
                index = str(queue.size() - 1)
                number = queue.deQueue()
                print('Pop '+ str(number) +' size in queue is '+index)
            else:
                print(-1)
    if queue.size() > 0:

        print('Number in Queue is :  ' ,end ="")
        print(queue.items)
    else:
        print('Empty')
input = input('Enter Input : ').split(",")
the_next_queue(input)
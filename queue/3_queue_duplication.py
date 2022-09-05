""""
กฤษฎาได้มาทำงานพิเศษในช่วงปิดเทอมที่ร้านหนังสือการ์ตูนแห่งหนึ่ง  โดยเจ้าของร้านได้สั่งให้กฤษฎามาจัดหนังสือการ์ตูน Attack On Titan เพื่อที่จะวางขายในวันรุ่งขึ้น  โดยกฤษฎาได้จัดหนังสือไปเรื่อยๆจนรู้สึกเบื่อหน่าย  จึงได้คิดเกมสนุกๆขึ้นมานั่นคือ  ในชั้นหนังสือจะมีแค่ด้านหน้ากับด้านหลังที่จะใส่หนังสือเข้าไปได้เรื่อยๆ และจะนำหนังสือออกได้แค่ด้านหน้า และใส่หนังสือเพิ่มได้แค่ด้านหลัง  โดยเมื่อเล่นเกมนี้ไปเรื่อยๆ กฤษฎาก็ลืมว่าในชั้นหนังสือนั้นมีหนังสือซ้ำกันหรือไม่  กฤษฎาเลยอยากให้คุณเขียนโปรแกรม Python เพื่อมาช่วยกฤษฎาคิดว่ามีหนังสือซ้ำกันในชั้นนั้นหรือไม่

Input :
จะแบ่งเป็น 2 ฝั่งแบ่งด้วย /   คือ ซ้าย : เป็นหนังสือที่มีอยู่ในชั้นอยู่แล้ว  ขวา : จะแบ่งเป็น 2 ส่วน คือ D กับ E
D                -> เป้นการนำหนังสือด้านหน้าออกจากชั้น
E <value>   -> เป็นการนำหนังสือ Attack On Titan เล่มที่ value เข้าชั้นหนังสือจากด้านหลัง

Enter Input : 1 2 7 2 4 6 8/E 5,D,D,E 1,E 3,D
NO Duplicate



"""
class Queue:
    def __init__(self,list = None):
        if list == None:
            self.items = []
        else:
            self.items = list
    def enQueue(self, item):
        self.items.append(item)
    def deQueue(self):
        return self.items.pop(0)
    def size(self):
        return len(self.items)
    def isEmpty(self):
        return len(self.items) == 0
        
def queue_duplication(input):
    queue = Queue()
    # '1 2 7 2 4 6 8/E 5,D,D,E 1,E 3,D'
    
    # add or take out queue
    input = input.split("/")
    numbers = input[0]
    numbers = numbers.split(" ")
    list_arragement = input[1]
    list_arragement = list_arragement.split(",")
    # add list in queue
    for number in numbers:
        number = int(number)
        queue.enQueue(number)
    # add or take out queue
    
    for type_and_number in list_arragement:
        type_and_number = type_and_number.split(" ")
        type = type_and_number[0]
        if type == 'E':
            number = type_and_number[1]
            number = int(number)
            queue.enQueue(number)
        elif type == 'D' and not queue.isEmpty():
            queue.deQueue()
    # check duplicate
    # size 5 , 0-4 ,1-4
    k=1
    s = 'NO Duplicate'
    for i in range(0,queue.size()):
        for j in range(k,queue.size()):
            if queue.items[i] == queue.items[j]:
                    # print(queue.isItem(i),end = "        ")
                    # print(queue.isItem(j))
                s = 'Duplicate'
                break
            else:
                s = 'NO Duplicate'
        k+=1
        if s == 'Duplicate':
            break
    print(s)
    # print(queue.isItems())
queue_duplication(input('Enter Input : '))
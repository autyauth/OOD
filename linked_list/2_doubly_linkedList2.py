""""
ให้เขียนคลาสของ Doubly Linked List ซึ่งมีเมท็อดดังนี้

1. def __init__(self): สำหรับสร้าง linked list

2. def __str__(self): return string แสดง ค่าใน linked list

3. def str_reverse(self): return string แสดง ค่าใน linked list จากหลังมาหน้า

4. def isEmpty(self): return list นั้นว่างหรือไม่

5. def append(self, data): add node ที่มี data เป็น parameter ข้างท้าย linked list

6. def insert(self, index, data): insert data ใน index ที่กำหนด

7. def remove(self, data): remove & return node ที่มี data

 - การแทรกในที่นี้ จะเป็นการนำข้อมูลใหม่ที่ต้องการมาใส่แทนที่ตำแหน่งของข้อมูลเดิมและย้ายข้อมูลเดิมไปต่อหลังข้อมูลใหม่ 

คำแนะนำเพิ่มเติม เพื่อความง่ายในการเขียนโค้ดและไม่ต้องเขียนspecial caseเยอะๆ ให้ลองใช้ Dummy Node ดูนะครับ(หากสงสัยการใช้งาน Dummy Node สอบถามพี่ๆTA หรือ https://youtu.be/XgUIjTQ1HjA )

โดยรูปแบบ Input มีดังนี้
1. append       ->  A
2. add_before -> Ab
3. insert          ->   I
4. remove       ->  R

*******ให้ใช้ class Node ในการทำ Linked List ห้ามใช้ list*********
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


Enter Input : A 3,A 4,Ab 0,I 1:2
linked list : 3
reverse : 3
linked list : 3->4
reverse : 4->3
linked list : 0->3->4
reverse : 4->3->0
index = 1 and data = 2
linked list : 0->2->3->4
reverse : 4->3->2->0


Enter Input : I -1:0,I 10:10,I 0:0
Data cannot be added
linked list : 
reverse : 
Data cannot be added
linked list : 
reverse : 
index = 0 and data = 0
linked list : 0
reverse : 0


Enter Input : R 0,A 1,A 1,A 2,R 1
Not Found!
linked list : 
reverse : 
linked list : 1
reverse : 1
linked list : 1->1
reverse : 1->1
linked list : 1->1->2
reverse : 2->1->1
removed : 1 from index : 0
linked list : 1->2
reverse : 2->1


Enter Input : R 0, I -1:0, Ab 0, A 1, R 0, I 0:0, A 99, I 3:59, I 0:0, R 99, A 10
Not Found!
linked list : 
reverse : 
Data cannot be added
linked list : 
reverse : 
linked list : 0
reverse : 0
linked list : 0->1
reverse : 1->0
removed : 0 from index : 0
linked list : 1
reverse : 1
index = 0 and data = 0
linked list : 0->1
reverse : 1->0
linked list : 0->1->99
reverse : 99->1->0
index = 3 and data = 59
linked list : 0->1->99->59
reverse : 59->99->1->0
index = 0 and data = 0
linked list : 0->0->1->99->59
reverse : 59->99->1->0->0
removed : 99 from index : 3
linked list : 0->0->1->59
reverse : 59->1->0->0
linked list : 0->0->1->59->10
reverse : 10->59->1->0->0


Enter Input : I 0:0,R 0,A 0,A 1,R 0,R 1,Ab 0, Ab 1, R 1, R 0,A 1, Ab 0,R 0,R 1
index = 0 and data = 0
linked list : 0
reverse : 0
removed : 0 from index : 0
linked list : 
reverse : 
linked list : 0
reverse : 0
linked list : 0->1
reverse : 1->0
removed : 0 from index : 0
linked list : 1
reverse : 1
removed : 1 from index : 0
linked list : 
reverse : 
linked list : 0
reverse : 0
linked list : 1->0
reverse : 0->1
removed : 1 from index : 0
linked list : 0
reverse : 0
removed : 0 from index : 0
linked list : 
reverse : 
linked list : 1
reverse : 1
linked list : 0->1
reverse : 1->0
removed : 0 from index : 0
linked list : 1
reverse : 1
removed : 1 from index : 0
linked list : 
reverse : 


Enter Input : I 1:1,I 0:0,I 0:1,I 0:2,I 3:-1,I -1:-1,I 10:5,I 2:0
Data cannot be added
linked list : 
reverse : 
index = 0 and data = 0
linked list : 0
reverse : 0
index = 0 and data = 1
linked list : 1->0
reverse : 0->1
index = 0 and data = 2
linked list : 2->1->0
reverse : 0->1->2
index = 3 and data = -1
linked list : 2->1->0->-1
reverse : -1->0->1->2
Data cannot be added
linked list : 2->1->0->-1
reverse : -1->0->1->2
Data cannot be added
linked list : 2->1->0->-1
reverse : -1->0->1->2
index = 2 and data = 0
linked list : 2->1->0->0->-1
reverse : -1->0->0->1->2




"""
class Double_linked_list:
    class Node:
        def __init__(self, data):
            self.data = data 
            self.prev = None
            self.next = None
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        self.index = 0
    def __str__(self):
        s = ''
        i = 0
        for data_in_list in self.iter():
            s += str(data_in_list)
            i += 1
            if self.size > i:
                s += '->'
        return s
    def str_reverse(self):
        s = ''
        i = 0
        for data_in_list in self.iter_reverse():
            s += str(data_in_list)
            i += 1
            if self.size > i:
                s += '->'
        return s

    def iter(self):
        t = self.head
        while t:
            data_in_list = t.data
            t = t.next
            yield data_in_list

    def iter_reverse(self):
        t = self.tail
        while t:
            data_in_list = t.data
            t = t.prev
            yield data_in_list

    def append(self, data):
        new_node = self.Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
    def isEmpty(self):
        return self.size == 0
    def insert(self, index, data):
        new_node = self.Node(data)
        dummy_node = self.head
        i = 0
        
        if index == 0 and self.size == 0 :
            print('index = '+ str(index) +' and data = '+str(data))
            self.append(data)                           # หาก insert(0,?) แปลว่า ไม่มี Node ใน list เลยต้องสร้าง node ใหม่
            return
        elif index == 'Ab' and self.size == 0:
            self.append(data)                           
            return
        elif self.size == 0 and index != 0:
            print('Data cannot be added')               # หาก insert(0,?) แปลว่า ไม่มี Node ใน list เลยต้องสร้าง node ใหม่
            return
        
        while dummy_node != None:
            if index == 'Ab':
                new_node.next = self.head
                dummy_node.prev = new_node
                self.head = new_node
                self.size += 1
                
                break
            elif index == 0:
                new_node.next = self.head
                dummy_node.prev = new_node
                self.head = new_node
                self.size += 1
                print('index = '+ str(index) +' and data = '+str(data))
                break
            elif i == index:
                before_insert_node = dummy_node.prev  # after_insert_node = dummby_node 
                new_node.prev = before_insert_node
                new_node.next = dummy_node            # node ที่จะแทรกใหม่เราต้องชี้ไปยัง node ระหว่างที่จะแทรก
                before_insert_node.next = new_node    # จากนั้นค่อยโยง node ระหว่างที่จะแทรกมายัง node ที่แทรกใหม่
                dummy_node.prev = new_node
                self.size += 1
                print('index = '+ str(index) +' and data = '+str(data))
                break
            elif self.size == index:
                print('index = '+ str(index) +' and data = '+str(data))
                self.append(data)
                break
            elif index < 0 or index > self.size:
                print('Data cannot be added')
                break
            i += 1
            dummy_node = dummy_node.next
    def remove(self, data):
        dummy_node = self.head
        index = 0
        while dummy_node != None:
            if self.head.data == data:
                if self.size >1:
                    self.head = dummy_node.next
                    self.head.prev = None
                    self.size -= 1
                    print('removed : '+str(data)+' from index : '+str(index))
                    return dummy_node
                elif self.size == 1:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                    self.size -= 1
                    print('removed : '+str(data)+' from index : '+str(index))
                    return dummy_node
            elif self.size == index+1:
                
                while dummy_node.next != None:
                    dummy_node = dummy_node.next
                dummy_node2 = dummy_node
                dummy_node = dummy_node.prev
                self.tail = dummy_node
                dummy_node.next = None
                self.size -= 1
                print('removed : '+str(data)+' from index : '+str(index))
                return dummy_node2
            elif dummy_node.data == data:
                before_thisNode = dummy_node.prev
                next_thisNode = dummy_node.next
                before_thisNode.next = next_thisNode
                next_thisNode.prev = before_thisNode
                self.size -= 1
                print('removed : '+str(data)+' from index : '+str(index))
                return dummy_node
            
            index += 1
            dummy_node = dummy_node.next
        print('Not Found!')

def linked_list(strs):
    double_linked_list = Double_linked_list()
    list = strs.split(",")
    for type_and_number in list:
        type_and_number = type_and_number.split(" ")
        if type_and_number[0] == '':
            type_and_number.remove('')
        type = type_and_number[0]
        number = type_and_number[1]
        
        
        if type == 'A':
            number = int(number)
            double_linked_list.append(number)
            
            print('linked list : ' ,end="")
            print(double_linked_list)
            print('reverse : ' ,end="")
            print(double_linked_list.str_reverse())
        elif type == 'Ab':
            number = int(number)
            double_linked_list.insert('Ab',number)
            # print('index = '+ str(index) +' and data = '+str(number))
            print('linked list : ' ,end="")
            print(double_linked_list)
            print('reverse : ' ,end="")
            print(double_linked_list.str_reverse())
        elif type == 'I':
            number = number.split(":")
            index = int(number[0])
            number = int(number[1])
            double_linked_list.insert(index,number)
            
            print('linked list : ' ,end="")
            print(double_linked_list)
            print('reverse : ' ,end="")
            print(double_linked_list.str_reverse())
        elif type == 'R':
            number = int(number)
            double_linked_list.remove(number)
            print('linked list : ' ,end="")
            print(double_linked_list)
            print('reverse : ' ,end="")
            print(double_linked_list.str_reverse())       

# list = [1,2,3,4,5,6,7,8,9]
# linked_list('A 3,A 4,Ab 0,I 1:2')
# linked_list('I -1:0,I 10:10,I 0:0')
# linked_list('R 0,A 1,A 1,A 2,R 1')
# linked_list('I 0:0,R 0,A 0,A 1,R 0,R 1,Ab 0, Ab 1, R 1, R 0,A 1, Ab 0,R 0,R 1')
input = input('Enter Input : ')
linked_list(input) 
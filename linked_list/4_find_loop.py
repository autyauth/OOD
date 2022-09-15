""""
ให้ตรวจสอบว่า linked list มีการวนซ้ำหรือไม่ และ แสดงผลลัพธ์ตามตัวอย่าง

โดยมีการรับ input ดังนี้

1. append ->   A <int> คือ เพิ่มข้อมูลต่อท้าย linked list

2. set_next -> S <index1(int):index2(str)> คือการ set node.next ของ node index ที่1 ให้ชี้ไป node index ที่2

ซึ่งหากไม่มี  node index ที่1 ใน linked list ให้แสดง error และหากไม่มี node index ที่2 ใน linked list ให้ทำการ append nodeใหม่เข้าไปใน linked list โดยมี value = index2


Enter input : A 0,A 1,S 2:0
0
0->1
Error! {index not in length}: 2
No Loop
0->1



Enter input : A 0,A 1,S 0:2
0
0->1
index not in length, append : 2
No Loop
0->1->2



Enter input : A 0,A 1,S 1:0
0
0->1
Set node.next complete!, index:value = 1:1 -> 0:0
Found Loop



Enter input : S 0:0
Error! {list is empty}
No Loop
Empty



Enter input : A 0,A 3,A 5,A 7,A 9,S 2:0
0
0->3
0->3->5
0->3->5->7
0->3->5->7->9
Set node.next complete!, index:value = 2:5 -> 0:0
Found Loop


Enter input : A 0,A 1,A 2,S 0:2
0
0->1
0->1->2
Set node.next complete!, index:value = 0:0 -> 2:2
No Loop
0->2



Enter input : S 0:0,A 0,A 0,A 0,S 0:5,S 0:3,A 5,S 2:1
Error! {list is empty}
0
0->0
0->0->0
index not in length, append : 5
Set node.next complete!, index:value = 0:0 -> 3:5
0->5->5
Set node.next complete!, index:value = 2:5 -> 1:5
Found Loop



Enter input : S 0:0,A 0
Error! {list is empty}
0
No Loop
0


Enter input : A 0,A -1,A -1,S 2:2
0
0->-1
0->-1->-1
Set node.next complete!, index:value = 2:-1 -> 2:-1
Found Loop


"""

class Node:
    def __init__(self, data, next = None):
        self.data = data
        if next == None:
            self.next = None
        else:
            self.next = next
class Linked_list:
    def __init__(self):
        self.head = None
        self.size = 0
        self.check_loop = ''
    def __str__(self):
        s = ''
        temp = self.head
        if self.isEmpty():
            s = 'Empty'
        else:
            while temp:
                s +=  str(temp.data) + '->'
                temp = temp.next
            s = s.strip('->')
        return s
    def print_list(self):
        s = ''
        temp = self.head
        if self.isEmpty():
            s = 'Empty'
        else:
            while temp != None:
                s +=  str(temp.data) + '->'
                temp = temp.next
            s = s.strip('->')
        return s
    def isEmpty(self):
        return self.size == 0
    def check_node(self, data):
        temp_head = self.head
        if temp_head != None:
            while temp_head != None:
                if temp_head.data == data:
                    return True
                temp_head = temp_head.next
        return False
    

    def append(self, data):
        new_node = Node(data)
        temp_head = self.head
        if self.head == None:
            self.head = new_node
        else:
            while temp_head.next != None:
                temp_head = temp_head.next
            temp_head.next = new_node
        self.size += 1
    def set_next(self, index1, index2):      #set node ใน list ที่ index1 ชี้ไปยัง node ที่มี data นั้น
        temp_head = self.head 
        temp_head2 = self.head
        index = 0
        # node_data2 = Node(data2)
        s = ''
        s_checkLoop = ''
        if self.size <= 0:
            s = 'Error! {list is empty}' +'' #+ self.print_list()
            self.check_loop = 'No Loop'
        elif index1+1 > self.size or index1 < 0:
            s = 'Error! {index not in length}: '+str(index1) +''# + self.print_list()     
            self.check_loop = 'No Loop'
        elif index2 >= self.size and index1 <= self.size-1 and index1 >= 0:
            self.append(index2)
            s = 'index not in length, append : ' + str(index2) +''# + self.print_list()  
            self.check_loop = 'No Loop'       
        else: 
            # while dummy_head != None:
            #     if index == index2:
            #         temp_head2 = dummy_head 
            #         break
            #     index += 1
            #     dummy_head = dummy_head.next
            # dummy_head = self.head  
            # for i in range(0,index1):
            #     dummy_head = dummy_head.next
            # dummy_head.next = temp_head2
            # temp_head3 = temp_head2
            # while temp_head3 != None:
            #     temp_head3 = temp_head3.next 
            #     s = 'Set node.next complete!, index:value = '+ str(index1)+':'+ str(dummy_head.data) + ' -> '+ str(index) + ':'+str(index2) + '\nNo Loop\n' + self.print_list()

            #     if self.head == temp_head3:
            #         s = 'Set node.next complete!, index:value = '+ str(index1)+':'+ str(dummy_head.data) + ' -> '+ str(index) + ':'+str(index2) + '\nFound Loop'
            #         break

            for i in range(0,index1):
                temp_head = temp_head.next
            for i in range(0,index2):
                temp_head2 = temp_head2.next
            temp_head.next = temp_head2
            s = 'Set node.next complete!, index:value = '+ str(index1)+':'+ str(temp_head.data) + ' -> '+ str(index2) + ':'+str(temp_head2.data)+''
            if index1 >= index2:
                self.check_loop = 'Found Loop'
            else:
                self.check_loop = 'No Loop'
                
        print(s)
        return
        # มี index และ ข้อมูลนั้น
        # index1 ที่จะเอาไปชี้มันไม่มี 
        
        # node2 ที่มีข้อมูลที่จะชี้ไปหา ดันไม่มี ให้สร้างขึ้นเลย
s = input('Enter input : ')
# s = 'A 0,A 3,A 5,A 7,A 9,S 2:0'
# s = 'A 0,A 1,S 2:0'
# s = ''
list = s.split(",")
linked_list = Linked_list()
for i in list:
    i = i.split(" ")
    type = i[0]
    number = i[1]
    if type == 'A':
        number = int(number)
        linked_list.append(number)
        print(linked_list.print_list())
    elif type == 'S':
        number = number.split(":")
        index1 = int(number[0])
        index2 = int(number[1])
        linked_list.set_next(index1, index2)

print(linked_list.check_loop)
if linked_list.check_loop == 'No Loop':
    print(linked_list.print_list()) 

# print(linked_list)
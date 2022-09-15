""""
ให้น้องๆใช้ Linked List (เขียนเป็น class)  ในการทำ Radix Sort  (มีอยู่ในสไลด์เรียน 2 หน้าสุดท้าย)  ในรูปแบบมากไปน้อย

โดยผลลัพธ์ให้ออกมาเป็นการทำ Radix Sort แบบจำนวนรอบน้อยที่สุด และแสดงผลในแต่ละรอบว่าได้ผลลัพธ์เป็นอย่างไร  3 บรรทัดสุดท้ายจะเป็น ( จำนวนรอบที่น้อยที่สุด , Data ก่อนทำ Radix Sort และ Data หลังทำ Radix Sort )

Enter Input : 64 8 216 512 27 729 0 1 343 125
------------------------------------------------------------
Round : 1
0 : 0 
1 : 1 
2 : 512 
3 : 343 
4 : 64 
5 : 125 
6 : 216 
7 : 27 
8 : 8 
9 : 729 
------------------------------------------------------------
Round : 2
0 : 8 1 0 
1 : 512 216 
2 : 729 125 27 
3 : 
4 : 343 
5 : 
6 : 64 
7 : 
8 : 
9 : 
------------------------------------------------------------
Round : 3
0 : 64 27 8 1 0 
1 : 125 
2 : 216 
3 : 343 
4 : 
5 : 512 
6 : 
7 : 729 
8 : 
9 : 
------------------------------------------------------------
Round : 4
0 : 729 512 343 216 125 64 27 8 1 0 
1 : 
2 : 
3 : 
4 : 
5 : 
6 : 
7 : 
8 : 
9 : 
------------------------------------------------------------
3 Time(s)
Before Radix Sort : 64 -> 8 -> 216 -> 512 -> 27 -> 729 -> 0 -> 1 -> 343 -> 125
After  Radix Sort : 729 -> 512 -> 343 -> 216 -> 125 -> 64 -> 27 -> 8 -> 1 -> 0


Enter Input : -123 456 -789 0 27 3645 133 -142 -5038594 15615 668 2 -1 72
------------------------------------------------------------
Round : 1
0 : 0 
1 : -1 
2 : 72 2 -142 
3 : 133 -123 
4 : -5038594 
5 : 15615 3645 
6 : 456 
7 : 27 
8 : 668 
9 : -789 
------------------------------------------------------------
Round : 2
0 : 2 0 -1 
1 : 15615 
2 : 27 -123 
3 : 133 
4 : 3645 -142 
5 : 456 
6 : 668 
7 : 72 
8 : -789 
9 : -5038594 
------------------------------------------------------------
Round : 3
0 : 72 27 2 0 -1 
1 : 133 -123 -142 
2 : 
3 : 
4 : 456 
5 : -5038594 
6 : 15615 3645 668 
7 : -789 
8 : 
9 : 
------------------------------------------------------------
Round : 4
0 : 668 456 133 72 27 2 0 -1 -123 -142 -789 
1 : 
2 : 
3 : 3645 
4 : 
5 : 15615 
6 : 
7 : 
8 : -5038594 
9 : 
------------------------------------------------------------
Round : 5
0 : 3645 668 456 133 72 27 2 0 -1 -123 -142 -789 
1 : 15615 
2 : 
3 : -5038594 
4 : 
5 : 
6 : 
7 : 
8 : 
9 : 
------------------------------------------------------------
Round : 6
0 : 15615 3645 668 456 133 72 27 2 0 -1 -123 -142 -789 -5038594 
1 : 
2 : 
3 : 
4 : 
5 : 
6 : 
7 : 
8 : 
9 : 
------------------------------------------------------------
5 Time(s)
Before Radix Sort : -123 -> 456 -> -789 -> 0 -> 27 -> 3645 -> 133 -> -142 -> -5038594 -> 15615 -> 668 -> 2 -> -1 -> 72
After  Radix Sort : 15615 -> 3645 -> 668 -> 456 -> 133 -> 72 -> 27 -> 2 -> 0 -> -1 -> -123 -> -142 -> -789 -> -5038594


Enter Input : -1 -9 -3 -6 -5 -4 -7 0 -8 -2 3 2 5 1 4 9 8 7 6
------------------------------------------------------------
Round : 1
0 : 0 
1 : 1 -1 
2 : 2 -2 
3 : 3 -3 
4 : 4 -4 
5 : 5 -5 
6 : 6 -6 
7 : 7 -7 
8 : 8 -8 
9 : 9 -9 
------------------------------------------------------------
Round : 2
0 : 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 
1 : 
2 : 
3 : 
4 : 
5 : 
6 : 
7 : 
8 : 
9 : 
------------------------------------------------------------
1 Time(s)
Before Radix Sort : -1 -> -9 -> -3 -> -6 -> -5 -> -4 -> -7 -> 0 -> -8 -> -2 -> 3 -> 2 -> 5 -> 1 -> 4 -> 9 -> 8 -> 7 -> 6
After  Radix Sort : 9 -> 8 -> 7 -> 6 -> 5 -> 4 -> 3 -> 2 -> 1 -> 0 -> -1 -> -2 -> -3 -> -4 -> -5 -> -6 -> -7 -> -8 -> -9



Enter Input : 15 -15
------------------------------------------------------------
Round : 1
0 : 
1 : 
2 : 
3 : 
4 : 
5 : 15 -15 
6 : 
7 : 
8 : 
9 : 
------------------------------------------------------------
Round : 2
0 : 
1 : 15 -15 
2 : 
3 : 
4 : 
5 : 
6 : 
7 : 
8 : 
9 : 
------------------------------------------------------------
Round : 3
0 : 15 -15 
1 : 
2 : 
3 : 
4 : 
5 : 
6 : 
7 : 
8 : 
9 : 
------------------------------------------------------------
2 Time(s)
Before Radix Sort : 15 -> -15
After  Radix Sort : 15 -> -15



Enter Input : -123456789 987654321 123456789 -987654321
------------------------------------------------------------
Round : 1
0 : 
1 : 987654321 -987654321 
2 : 
3 : 
4 : 
5 : 
6 : 
7 : 
8 : 
9 : 123456789 -123456789 
------------------------------------------------------------
Round : 2
0 : 
1 : 
2 : 987654321 -987654321 
3 : 
4 : 
5 : 
6 : 
7 : 
8 : 123456789 -123456789 
9 : 
------------------------------------------------------------
Round : 3
0 : 
1 : 
2 : 
3 : 987654321 -987654321 
4 : 
5 : 
6 : 
7 : 123456789 -123456789 
8 : 
9 : 
------------------------------------------------------------
Round : 4
0 : 
1 : 
2 : 
3 : 
4 : 987654321 -987654321 
5 : 
6 : 123456789 -123456789 
7 : 
8 : 
9 : 
------------------------------------------------------------
Round : 5
0 : 
1 : 
2 : 
3 : 
4 : 
5 : 987654321 123456789 -123456789 -987654321 
6 : 
7 : 
8 : 
9 : 
------------------------------------------------------------
Round : 6
0 : 
1 : 
2 : 
3 : 
4 : 123456789 -123456789 
5 : 
6 : 987654321 -987654321 
7 : 
8 : 
9 : 
------------------------------------------------------------
Round : 7
0 : 
1 : 
2 : 
3 : 123456789 -123456789 
4 : 
5 : 
6 : 
7 : 987654321 -987654321 
8 : 
9 : 
------------------------------------------------------------
Round : 8
0 : 
1 : 
2 : 123456789 -123456789 
3 : 
4 : 
5 : 
6 : 
7 : 
8 : 987654321 -987654321 
9 : 
------------------------------------------------------------
Round : 9
0 : 
1 : 123456789 -123456789 
2 : 
3 : 
4 : 
5 : 
6 : 
7 : 
8 : 
9 : 987654321 -987654321 
------------------------------------------------------------
Round : 10
0 : 987654321 123456789 -123456789 -987654321 
1 : 
2 : 
3 : 
4 : 
5 : 
6 : 
7 : 
8 : 
9 : 
------------------------------------------------------------
9 Time(s)
Before Radix Sort : -123456789 -> 987654321 -> 123456789 -> -987654321
After  Radix Sort : 987654321 -> 123456789 -> -123456789 -> -987654321



Enter Input : 0 0 0 0 0 0 0
------------------------------------------------------------
Round : 1
0 : 0 0 0 0 0 0 0 
1 : 
2 : 
3 : 
4 : 
5 : 
6 : 
7 : 
8 : 
9 : 
------------------------------------------------------------
0 Time(s)
Before Radix Sort : 0 -> 0 -> 0 -> 0 -> 0 -> 0 -> 0
After  Radix Sort : 0 -> 0 -> 0 -> 0 -> 0 -> 0 -> 0


"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    def __str__(self):
        return self.data
    def get_digit(number, digit):               #get digit from each digit
        for i in range(0,digit-1):
            number //= 10
        return number%10
class Linked_list:
    def __init__(self):
        self.head = self.tail = None
        self.size = 0
    def __str__(self):
        s = ''
        temp_head = self.head
        if not self.isEmpty():
            while temp_head != None:
                s += str(temp_head.data) + " "
                temp_head = temp_head.next
            s = s.strip(" ")
        return s
    def __getitem__(self,index):
        temp = self.head
        for i in range(index):
            temp = temp.next
        return temp.data
    def str2(self):
        s = ''
        temp_head = self.head
        if not self.isEmpty():
            while temp_head != None:
                s += str(temp_head.data) 
                temp_head = temp_head.next
                if temp_head != None:
                    s += ' -> '
            # s = s.strip('->')
        return s
    def isEmpty(self):
        return self.size == 0
    def append(self,data):
        new_node = Node(data)
        temp_head = self.head
        if self.head == None:
            self.head = new_node  
        else:
            while temp_head.next != None:
                temp_head = temp_head.next
            temp_head.next = new_node
        self.tail = new_node
        self.size += 1
    def pop(self):
        if not self.isEmpty():
            data = self.tail.data
            # self.head = self.head.next
            temp = self.head
            while temp.next.next != None:
                temp = temp.next
            self.tail = temp
            temp.next = None
        else:
            self.head = None
            self.tail = None
            data = None
        self.size -= 1
        return data
    def popHead(self):
        if not self.isEmpty():
            data = self.head.data
            self.head = self.head.next
        else:
            self.head = None
            self.tail = None
            data = None
        self.size -= 1
        return data
    def insertHead(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.tail = self.head
            self.head = new_node
        self.size += 1 
    def insert(self, data, index):
        new_node = Node(data)
        temp = self.head
        if index == 0:
            new_node.next = self.head
            self.head = new_node 
        else:
            for i in range(index-1):
                temp = temp.next
            
            new_node.next = temp.next
            temp.next = new_node
        self.size += 1
        
def get_digit(n, d):
    for i in range(0,d-1):
        n //= 10
    return n % 10
def get_max_digit(n):
    i = 0 
    while n > 0:
        n //= 10
        i+=1
    return i
def radix_sort(input):
    plus = 0
    L = Linked_list()
    max_digit = get_max_digit(max(input))
    round = 0
    for i in input:
        L.append(i)
    LL = Linked_list()
    for i in range(0,10):
        LL.append(Linked_list())
    
    # for i in range(1,max_digit+2+plus):
    while True:
        round += 1
        while not L.isEmpty():
            number = L.popHead()
            index_digit = get_digit(abs(number),round)
            if LL[index_digit].isEmpty():
                LL[index_digit].insertHead(number)
            else:
                # เช็คว่าเลขใน List มันมากกว่าไหม ถ้ามากกว่าให้ใส่หน้า
                for i in range(LL[index_digit].size):
                    if int(LL[index_digit][i]) <= int(number):
                        LL[index_digit].insert(number, i)
                        break
                    else:
                    # ถ้าเลขที่ใส่เข้ามาใหม่ดันมากกว่าทั้งหมดก็ให้มันใส่ด้านหลัง
                        if i == LL[index_digit].size -1:
                            LL[index_digit].append(number)
        print('------------------------------------------------------------\nRound : ' + str(round))
        for i in range(10):
            print(str(i)+" : "+ LL[i].__str__())
        done = True
        for i in range(1,10) :
            if not LL[i].isEmpty() :
                done = False
        for i in range(10):
            while not LL[i].isEmpty():
                L.append(LL[i].popHead())
        if done :
               return L,round-1 
    
print('Enter Input : ',end="")
input =  list(map(int, input().split(" ")))
before_sort = Linked_list()
for number in input:
    before_sort.append(number)
after_sort,round_sort = radix_sort(input)
print('------------------------------------------------------------\n' + str(round_sort) + ' Time(s)')
print('Before Radix Sort : ' + before_sort.str2())
print('After  Radix Sort : ' + after_sort.str2())